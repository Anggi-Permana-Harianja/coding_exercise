"""
Cracking Coding Interview 1.2

Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.

Time: O(N)
Space: O(N)

This can be solved with two approaches
- sort the string, and then compare if both are similar
- check if the two strings have identical character counts.
"""

import unittest

def sort_string(string: str) -> str:
    sorted_string = sorted(string)
    
    return ''.join(sorted_string)

def check_permutation_using_sorted(string1: str, string2: str) -> bool:
    # if len is different, definitely not permutation
    if len(string1) != len(string2): return False

    # compare sorted strings
    return sort_string(string1) == sort_string(string2)

def check_permutation_using_dict(string1: str, string2: str) -> bool:
    # if len is different, definitely not permutation
    if len(string1) != len(string2): return False

    dict_chars = {}
    # add all chars from string1 to a dict
    for char in string1:
        dict_chars[char] = dict_chars.get(char, 0) + 1

    # for string2 we deduct, if reach < 0 means not permutation
    for char in string2:
        if char not in dict_chars: return False # in case there is any char in string2 that not in string1
        dict_chars[char] -= 1
        if dict_chars[char] < 0: return False

    return True

class TestCases(unittest.TestCase):
    def test_case1(self):
        string1 = "listen"
        string2 = "silent"

        self.assertEqual(check_permutation_using_sorted(string1, string2), True)

    def test_case2(self):
        string1 = "listen"
        string2 = "silent"

        self.assertEqual(check_permutation_using_dict(string1, string2), True)

    def test_case3(self):
        string7 = "aabbaa"
        string8 = "ababba"

        self.assertEqual(check_permutation_using_dict(string7, string8), False)

    def test_case4(self):
        string7 = "aabbaa"
        string8 = "ababba"

        self.assertEqual(check_permutation_using_sorted(string7, string8), False)

if __name__ == "__main__":
    unittest.main()