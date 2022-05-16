#Link: https://www.algoexpert.io/questions/Longest%20Peak

#Time: O(n)
#Space: O(1)

def longest_peak(array: list) -> int:
    longest_peak = 0
    if len(array) < 3:
        return 0
    if len(array) == 3 and array.index(max(array)) == 1:
        return 1
    
    #finding peak
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            peak_idx = i
            curr_peak = 1
            
            #expand left-side
            for k in range(peak_idx, 0, -1):
                if array[k] > array[k - 1]:
                    curr_peak += 1
                else:
                    break
                    
            #expand right-side
            for j in range(peak_idx + 1, len(array)):
                if array[j - 1] > array[j]:
                    curr_peak += 1
                else:
                    break
            
            longest_peak = max(longest_peak, curr_peak)
            
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
        
if __name__ == '__main__':
    unittest.main()