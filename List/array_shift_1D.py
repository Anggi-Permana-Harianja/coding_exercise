#Link:https://www.youtube.com/watch?v=nJYFh4Dl-as

#Time: O(N)
#Space: O(N)

from typing import List

def shift_array(array: List[int], shift: int) -> List[int]:
    result_array = [0] * len(array)
    for i in range(len(array)):
        result_array[(i + shift) % len(array)] = array[i]
        
    return result_array

def shift_array_inplace(array: List[int], shift: int) -> List[int]:
    n = len(array)
    shift = shift % n

    # reverse all elements
    reverse_array(array, 0, n - 1)

    # reverse element 0 to shift
    reverse_array(array, 0, shift - 1)

    # reverse element shift to the end
    reverse_array(array, shift, n - 1)

    return array

def reverse_array(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array

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

    def test_program4(self):
        array = [1, 2, 3, 4]
        shift = 2
        
        result = [3, 4, 1, 2]
        
        self.assertEqual(shift_array_inplace(array, shift), result)

    def test_program5(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shift = 5
        
        result = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        
        self.assertEqual(shift_array_inplace(array, shift), result)
        
    def test_program6(self):
        array = [1, 2, 3, 4, 5, 6]
        shift = 1
        
        result = [6, 1, 2, 3, 4, 5]
        
        self.assertEqual(shift_array_inplace(array, shift), result)


if __name__ == '__main__':
    unittest.main()