#Link: https://www.algoexpert.io/questions/Insertion%20Sort

#Time: O(n^2)
#Space: O(1)

def insertion_sort(array:list[int]) -> list[int]:
    curr_idx = 0
    while curr_idx < len(array):
        tmp_idx = curr_idx
        while tmp_idx > 0:
            if array[tmp_idx] < array[tmp_idx - 1]:
                swap(array, tmp_idx, tmp_idx - 1)
            tmp_idx -= 1
        curr_idx += 1
        
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [5, 3, 4, 2, 1]
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(insertion_sort(array), result)
        
    def test_program2(self):
        array = [5, 4, 3, 2, 1]
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(insertion_sort(array), result)
        
if __name__ == '__main__':
    unittest.main()