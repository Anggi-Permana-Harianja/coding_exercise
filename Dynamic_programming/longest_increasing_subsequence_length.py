'''
Suppose you have an array of n integers, and you want to find the length of the longest increasing subsequence (LIS) of the array. 
A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. 
An increasing subsequence is a subsequence in which the elements are in increasing order.

For example, consider the array arr = [3, 4, -1, 0, 6, 2, 3]. 
The longest increasing subsequence of this array is [3, 4, 6], which has a length of 3.

Suppose you have an array of n integers, and you want to find the length of the longest increasing subsequence (LIS) of the array. A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a subsequence in which the elements are in increasing order.

For example, consider the array arr = [3, 4, -1, 0, 6, 2, 3]. 
The longest increasing subsequence of this array is [-1, 0, 2, 3], which has a length of 4.

arr:  3  4 -1  0  6  2  3
dp:   1  2  1  2  3  3  4

Time: O(n^2)
Space: O(n)
'''

def longest_increasing_subsequence_length(arr: list) -> int:
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        arr = [3, 4, -1, 0, 6, 2, 3]

        result = 4 #[-1, 0, 2, 3]
        longest_increasing_subsequence_length(arr)

        return self.assertEqual(longest_increasing_subsequence_length(arr), result)
    
    def test_program2(self):
        arr = [1, 2, 3, 5, 4]

        result = 4 #[1, 2, 3, 4] or [1, 2, 3, 5]

        return self.assertEqual(longest_increasing_subsequence_length(arr), result)
    
if __name__ == '__main__':
    unittest.main()
