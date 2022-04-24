#Link: Originally asked by Codility (https://stackoverflow.com/questions/63068610/finding-arithmetic-mean-of-subarrays-efficiently-in-an-array)

#Time: O(N * 2 ^ N)
#Space: O(N * 2 ^ N)

def mean_subsequence(array: list, mean: int) -> int:
    result = 0
    powerset = [[]]
    
    for num in array:
        len_ = len(powerset)
        for i in range(len_):
            subsequent = powerset[i]
            #check the mean
            tmp = [num] + subsequent
            if sum(tmp) / len(tmp) == mean:
                result += 1
            #update power set
            powerset.append([num] + subsequent)
            
    return result

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [2, 3, 5, 6]
        mean = 4
        
        result = 3
        
        self.assertEqual(mean_subsequence(array, mean), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4]
        mean = 2
        
        result = 3
        
        self.assertEqual(mean_subsequence(array, mean), result)
        
    def test_program3(self):
        array = [1, 2, 3, 4, 5, 6]
        mean = 3
        
        result = 9
        #[3], [4, 2], [5, 1], [5, 3, 1], [6, 2, 1], 
        #[4, 3, 2], [5, 4, 2, 1], [6, 3, 2, 1], [5, 4, 3, 2, 1]
        
        self.assertEqual(mean_subsequence(array, mean), result)
        
if __name__ == '__main__':
    unittest.main()