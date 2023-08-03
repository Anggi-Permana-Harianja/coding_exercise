"""
Blind 75

https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Time: O(N)
Space: O(N)

Hint:
    - We can use sorted() but the time will be O(N log N)
"""

import unittest

def valid_anagram(s1: str, s2: str) -> bool:
    # Return if the len is different
    if len(s1) != len(s2):
        return False
    
    s1_dict = {}
    s2_dict = {}

    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1

    for char in s2:
        s2_dict[char] = s2_dict.get(char, 0) + 1

    return s1_dict == s2_dict

class TestCases(unittest.TestCase):
    def test_case1(self):
        s1 = "anagram"
        s2 = "nagaram"

        return self.assertEqual(valid_anagram(s1, s2), True)
    
    def test_case2(self):
        s1 = "rat"
        s2 = "car"

        return self.assertEqual(valid_anagram(s1, s2), False)
    
if __name__ == "__main__":
    unittest.main()