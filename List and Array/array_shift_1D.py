#Link:https://www.youtube.com/watch?v=nJYFh4Dl-as

def shift_array(array, shift):
    result_array = [0] * len(array)
    for i in range(len(array)):
        result_array[(i + shift) % len(array)] = array[i]
        
    return result_array

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [1, 2, 3, 4]
        shift = 2
        
        result = [3, 4, 1, 2]
        
        self.assertEqual(shift_array(array, shift), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shift = 5
        
        result = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        
        self.assertEqual(shift_array(array, shift), result)
        
    def test_program3(self):
        array = [1, 2, 3, 4, 5, 6]
        shift = 1
        
        result = [6, 1, 2, 3, 4, 5]
        
        self.assertEqual(shift_array(array, shift), result)

if __name__ == '__main__':
    unittest.main()