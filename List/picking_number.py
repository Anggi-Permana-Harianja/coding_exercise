"""
https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

Time: O(N)
Space: O(N)

Hint:
    - use frequency instead just loop
"""

def picking_numbers(arr: list[int]) -> int:
    max_len = 0
    # create freq table
    freq = [0] * (max(arr) + 1)

    # count frequency for each number
    for num in arr:
        # update freq table
        freq[num] += 1
    
    curr_len = freq[0]

    # compute longest subsequence by adding the appearance
    for i in range(len(freq)):
        curr_len += freq[i]
        print(curr_len)
        if curr_len > max_len:
            max_len = curr_len
            curr_len = 0
            
    return max_len

import unittest

class TestCases(unittest.TestCase):
    def test_case1(self):
        arr = [1, 2, 3, 4, 5]

        return self.assertEqual(picking_numbers(arr), 5)

    def test_case2(self):
        arr = [1, 3, 4, 6, 7, 8]

        return self.assertEqual(picking_numbers(arr), 3)
    
if __name__ == "__main__":
    unittest.main()
    