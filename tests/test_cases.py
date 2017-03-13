import unittest
from Assignment3 import main_lights
import os.path
#from code.main_lights import validate_values,turn_lights_ON,turn_lights_OFF,switch_lights,count_lights_ON

class Test(unittest.TestCase):
    
    def test_setup(self):
        pass
    # Function to check if file is parsed correctly
    def test_file(self):
        
        line = "1000"
        with open('testing.txt', 'r') as f:
            first_line = f.readline()
            values = first_line.strip().split()
            x = values[0]
        self.assertEqual(line, x)
    # Function to check lights that are ON  
    def test_turn_on(self):
        
        self.assertEqual(main_lights.turn_lights_ON(0, 0, 2, 2, [[False, False, False], [False, False, False], [False, False, False]]), [[True, True, True], [True, True, True], [True, True, True]])

    # Function to check that lights are switched OFF
    def test_turn_off(self):
        
        self.assertEqual(main_lights.turn_lights_OFF(0, 0, 2, 2, [[True, True, True], [True, True, True], [True, True, True]]), [[False, False, False], [False, False, False], [False, False, False]])

    #Toggle function for ON and OFF lights.
    def test_switch(self):
        
        self.assertEqual(main_lights.switch_lights(0,0,2,2, [[True, False, True], [True, False, True], [True, False, True]]),[[False, True, False], [False, True, False], [False, True, False]])
    #Function for data validation
    def test_validate_values(self):
        self.assertEqual(main_lights.validate_values(-1, -2, 4, 4, 3), (0,0,2,2,3))
    #Function to count number of lights that are ON.
    def test_count_lights_ON(self):
        
        self.assertEqual(main_lights.count_lights_ON([[True, False, True], [True, False, True], [True, False, True]]), 6)
    
    
    #Function to check if input file is present
    def test_input_file(self):
        
        
        self.assertEqual(os.path.isfile("testing.txt"), True)


    
 
if __name__ == "__main__":
    
    unittest.main()