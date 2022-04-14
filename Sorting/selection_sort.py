#Link: https://www.algoexpert.io/questions/Selection%20Sort

#Time: O(N ^ 2)
#Space: O(1)

def selection_sort(array:list[int]) -> list[int]:
    curr_idx = 0
    while curr_idx < len(array):
        smallest_idx = curr_idx
        for i in range(smallest_idx + 1, len(array)):
            if min(array[smallest_idx], array[i]) == array[i]:
                smallest_idx = i
        swap(array, curr_idx, smallest_idx)
        curr_idx += 1
        
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    
import unittest
class Test_Program(unittest.TestCase):
    def test_program1(self):
        array = [5, 3, 4, 2, 1]
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(selection_sort(array), result)
        
    def test_program2(self):
        array = [5, 4, 3, 2, 1]
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(selection_sort(array), result)
        
if __name__ == '__main__':
    unittest.main()
    
    