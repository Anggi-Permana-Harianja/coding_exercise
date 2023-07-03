"""
Cracking Coding Interview Q 1.1

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Time: O(c) where c is the size of character set
Space: O(1) because it will be constant number up to 26
"""

def unique_char(string: str) -> bool:
    # if set length > 26 it means there will be redundant
    if len(string) > 26: return False

    # using hash or dict or list to solve this
    dict_chars = {}
    for char in string:
        if char not in dict_chars:
            dict_chars[char] =  True
        else:
            return False

    return True

import unittest

class TestCases(unittest.TestCase):
    def test_case1(self):
        string = "abcdefg"

        self.assertEqual(unique_char(string), True)

    def test_case2(self):
        string = "aabcdefghijk"

        self.assertEqual(unique_char(string), False)

    def test_case3(self):
        string = "abcdefghijklmnopqrstuvwxyz"

        self.assertEqual(unique_char(string), True)

if __name__ == "__main__":
    unittest.main()
