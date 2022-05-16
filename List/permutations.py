#Link: https://www.algoexpert.io/questions/Permutations

#Time: O(n * n!)
#Space: O(n * n !)

def get_permutations(array: list) -> list:
    permutations = []
    helper_function(0, array, permutations)
    
    return permutations

def helper_function(i: int, array: list, permutations: list) -> None:
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            helper_function(i + 1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
    

    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [1, 2, 3, 4]
        
        result = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 3, 2], [1, 4, 2, 3], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 3, 1], [2, 4, 1, 3], [3, 2, 1, 4], [3, 2, 4, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1], [4, 2, 3, 1], [4, 2, 1, 3], [4, 3, 2, 1], [4, 3, 1, 2], [4, 1, 3, 2], [4, 1, 2, 3]]
        
        self.assertEqual(get_permutations(array), result)
    
    def test_program2(self):
        array = [1, 2, 3]
        
        result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
        
        self.assertEqual(get_permutations(array), result)
        
if __name__ == '__main__':
    unittest.main()

    

