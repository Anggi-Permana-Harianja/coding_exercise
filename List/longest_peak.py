"""
Link: https://www.algoexpert.io/questions/Longest%20Peak

Time: O(n)
Space: O(1)
"""

import unittest
from typing import List

def left_slide(array: List, left_idx: int) -> int:
    while left_idx > 0 and array[left_idx - 1] < array[left_idx]:
        left_idx -= 1
    
    return left_idx

def right_slide(array: List, right_idx: int) -> int:
    while right_idx < len(array) - 1 and array[right_idx] > array[right_idx + 1]:
        right_idx += 1

    return right_idx

def longest_peak(array: list) -> int:
    longest_peak = 0
    n = len(array)
    i = 1 # start from 1st 

    while i < n - 1:
        # check if there is mountain
        if array[i - 1] < array[i] > array[i + 1]:
            # slide both ways and count peak
            left = left_slide(array, i - 1)
            right = right_slide(array, i + 1)
            
            # check the longest peak
            longest_peak = max(longest_peak, right - left + 1) # note why we decrease left and increase right

            # move i to potential peak
            i = right
        else:
            i += 1

    return longest_peak

class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        
        result = 6
        
        self.assertEqual(longest_peak(array), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4, 5, 1]
        
        result = 6
        
        self.assertEqual(longest_peak(array), result)
        
    def test_program3(self):
        array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
        
        result = 9
        
        self.assertEqual(longest_peak(array), result)

    def test_program4(self):
        array = [2,1,4,7,3,2,5]
        
        result = 5
        
        self.assertEqual(longest_peak(array), result)

if __name__ == '__main__':
    unittest.main()