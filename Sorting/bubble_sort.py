#Link: https://www.algoexpert.io/questions/Bubble%20Sort

#Time: O(N ^ 2)
#Space: O(1)

def bubble_sort(array):
    sorted_idx = len(array) - 1
    while sorted_idx > 0:
        for i in range(1, sorted_idx + 1):
            if array[i] < array[i - 1]:
                swap(array, i, i-1)
        sorted_idx -= 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [5, 3, 4, 2, 1]
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(bubble_sort(array), result)
        
    def test_program2(self):
        array = [6, 5, 4, 3, 2, 1]
        
        result = [1, 2, 3, 4, 5, 6]
        
        self.assertEqual(bubble_sort(array), result)
        
if __name__ == '__main__':
    unittest.main()