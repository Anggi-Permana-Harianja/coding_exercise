"""
Blind 75

https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Time: O(N)
Space: O(N)

Hint: 
    - just compare original text with reverse text
"""

import unittest

def valid_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]

class TestCases(unittest.TestCase):
    def test_case1(self):
        s = "A man, a plan, a canal: Panama"

        return self.assertEqual(valid_palindrome(s), True)
    
    def test_case2(self):
        s = "race a car"

        return self.assertEqual(valid_palindrome(s), False)
    
    def test_case3(self):
        s = " "

        return self.assertEqual(valid_palindrome(s), True)
    
if __name__ == "__main__":
    unittest.main()
