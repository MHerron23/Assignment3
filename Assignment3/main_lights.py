
import numpy as np

import urllib.request
import re


# Function to validate that the values are within the given range of the grid.
# If not present then manipulate the vales according to grid size and then pass on to calculate.
def validate_values(x1,y1,x2,y2,L):

    
    
    
    #Check for grid values
    if x2 >= x1 and y2 >= y1:
    
    #If values are negative then make them zero and make sure that values are not out of bounds.
    
        if x1 < 0:
            x1 = 0 
        elif x1 >= L:
            x1 = L-1
        else:
            x1 = x1
             
        if y1 < 0:
            y1 = 0
        elif y1 >= L:
            y1 = L-1
            
        if x2 < 0:
            x2 = 0
        elif x2 >= L:
            x2 = L-1
            
        if y2 < 0:
            y2 = 0
        elif y2 >= L:
            y2 = L-1        
    else:
        print("Invalid data for grid")
    return x1,y1,x2,y2,L
    
    
#Functions to turn lights ON/OFF/SWITCH




#Function to turn lights ON which are OFF
def turn_lights_ON(x1,y1,x2,y2,ledGrid):
    
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == False:
                ledGrid[row][col] = True
    return ledGrid


#Function to turn the lights OFF which are ON
def turn_lights_OFF(x1,y1,x2,y2,ledGrid):
    
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == True:
                ledGrid[row][col] = False
    return ledGrid

#Function to toggle values of lights ON->OFF/OFF->ON
def switch_lights(x1,y1,x2,y2,ledGrid):
    
    
       
    
    
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == True:
                ledGrid[row][col] = False
            elif ledGrid[row][col] == False:
                ledGrid[row][col] = True
                
    return ledGrid


#Function to count number of lights that are in ON state.
def count_lights_ON(ledGrid):
    count = 0
    for row in ledGrid:
        for col in row:
            if col == True:
                count += 1
    return count


# Main function which will call above all functions and will take input filename from command prompt.
def main():

    filename = input("Please enter the file name: ")#enter the file URL here
    print("Given file name:", filename)
    
    if filename.startswith('http'):
    # Open file from the given URL
        print("Opening file from the given url:", filename)
        file = urllib.request.urlopen(filename)
        filename = file.read().decode("utf-8")
        x = filename.split()
        str1 = ''.join(x[0])
    else:
        print("Invalid file supplied")
        
    #Calculate size of the grid
    print("Calculating grid size from the file.")  
    L = int(str1) 
    grid = [[False] * L for i in range(L)]
    ledGrid = np.array(grid)
     
     
    #save data of the file from web to lights.txt    
    with open ("lights.txt", "w") as text_file:
        text_file.write(filename)
        
    text_file.close()
      
    print("Calculating...")   
    filename = open("lights.txt", "r")
    x = filename.read()
    
    with open("lights.txt", "r") as f:
        
        for line in f.readlines()[1:]:     
            line = line.replace(',', ' ') 
            
            values = re.sub("[^\w]", " ",  line).split() 
            
            
            
            command = values[0] + " " + values[1]
            if command == "turn on":
                x1 = int(values[2])
                y1 = int(values[3])
                x2 = int(values[5])
                y2 = int(values[6])
                 
                
                result = validate_values(x1, y1, x2, y2, L)
                x1 = result[0]
                y1 = result[1]
                x2 = result[2]
                y2 = result[3]
                ledGrid = turn_lights_ON(x1, y1, x2, y2, ledGrid)
         
            elif command == "turn off":
                x1 = int(values[2])
                y1 = int(values[3])
                x2 = int(values[5])
                y2 = int(values[6])
                result = validate_values(x1, y1, x2, y2, L)
                x1 = result[0]
                y1 = result[1]
                x2 = result[2]
                y2 = result[3]
                ledGrid = turn_lights_OFF(x1, y1, x2, y2, ledGrid)
                 
            #Values[0] will be the first item in the line, if it is switch assign values
            elif values[0] == "switch":
                x1 = int(values[1])
                y1 = int(values[2])
                x2 = int(values[4])
                y2 = int(values[5])
                result = validate_values(x1, y1, x2, y2, L)
                x1 = result[0]
                y1 = result[1]
                x2 = result[2]
                y2 = result[3]
                ledGrid = switch_lights(x1, y1, x2, y2, ledGrid)
  
    print("The number of lights that are in ON state are: ", count_lights_ON(ledGrid))
        
    
if __name__ == "__main__":
    main()