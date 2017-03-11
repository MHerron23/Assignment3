'''
Created on 11 Mar 2017

@author: Michael
'''
import numpy as np
import urllib.request
import re




def main():

    filename = input("Please enter the file name: ")#"http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
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
    
    print("Hello There")
    #test


if __name__ == '__main__':
    main()