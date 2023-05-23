"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Time: O(N)
Space: O(MIN(M, N))
"""

def length_of_longest_substring(s: str) -> int:
    start = 0
    max_length = 0
    char_map = {}
    s = list(s)

    for end in range(len(s)):
        if s[end] in char_map:
            # update start index to latest appearance
            start = max(start, char_map[s[end]] + 1)
        # update char_map
        char_map[s[end]] = end
        # check max_length
        max_length = max(max_length, end - start + 1)

    return max_length

import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        s = "abcabcbb" # abc = 3

        self.assertEqual(length_of_longest_substring(s), 3)

    def test_case2(self):
        s = "abcabcvwxyz" # abcvwxyz = 8

        self.assertEqual(length_of_longest_substring(s), 8)

if __name__ == "__main__":
    unittest.main()

