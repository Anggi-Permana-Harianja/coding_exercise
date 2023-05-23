"""
Link: https://www.algoexpert.io/questions/Longest%20Peak

Time: O(n)
Space: O(1)
"""

def longest_peak(array: list) -> int:
    longest_peak = 0
    n = len(array)
    i = 1 # start from 1st 

    while i < n - 1:
        # check if there is mountain
        if array[i - 1] < array[i] > array[i + 1]:
            left = i - 1
            right = i + 1
            
            # slide to the left, substract left
            while left > 0 and array[left] > array[left - 1]:
                left -= 1

            # slide to the right, add right
            while right < n - 1 and array[right] > array[right + 1]:
                right += 1
            
            # check the longest peak
            longest_peak = max(longest_peak, right - left + 1) # note why we decrease left and increase right

            # move i to potential peak
            i = right
        else:
            i += 1

    return longest_peak

import unittest
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