#Link:https://www.youtube.com/watch?v=nJYFh4Dl-as

def shift_array(array, shift):
    #flattend the array
    flat_array = [val for sublist in array for val in sublist]
    
    #shift flat
    shifted_array = [0] * len(flat_array)
    for i in range(len(flat_array)):
        shifted_array[(i + shift) % len(flat_array)] = flat_array[i]
        
    #reconstruct back shifted_array
    results = []
    tmp = []
    cols = len(array[0])
    idx = 0
    for num in shifted_array:
        idx += 1
        tmp.append(num)
        
        if idx == cols:
            results.append(tmp)
            idx = 0
            tmp = []
            
    return results

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [[1, 2, 3], [4, 5, 6]]
        shift = 1
        
        result = [[6, 1, 2], [3, 4, 5]]
        
        self.assertEqual(shift_array(array, shift), result)
        
    def test_program2(self):
        array = [[1, 2, 3, 4], [5, 6, 7, 8]]
        shift = 1
        
        result = [[8, 1, 2, 3], [4, 5, 6, 7]]
        
        self.assertEqual(shift_array(array, shift), result)
        
if __name__ == '__main__':
    unittest.main()