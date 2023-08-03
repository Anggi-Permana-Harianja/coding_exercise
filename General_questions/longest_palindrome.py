"""
Blind 75

https://leetcode.com/problems/longest-palindrome/description/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Time: O(N)
Space: O(1)

Hint:
    - if count(char) is even add the count
    - if count(char) is odd add the count - 1
    - if in the end, any odd count(char) is exists, the result + 1
"""

import unittest

def longest_palindrome(s: str) -> int:
    dict_ = {}
    has_odd_count = False
    longest_palindrome = 0

    # Count apperance
    for char in s:
        dict_[char] = dict_.get(char, 0) + 1

    # Run the logic
    for count in dict_.values():
        # If count is even
        if count % 2 == 0:
            longest_palindrome += count
        else:
            longest_palindrome += count - 1
            has_odd_count = True

    if has_odd_count:
        longest_palindrome += 1

    return longest_palindrome


class TestCases(unittest.TestCase):
    def test_case1(self):
        s = "abccccdd"

        return self.assertEqual(longest_palindrome(s), 7)

    def test_case2(self):
        s = "dacccccvad"

        return self.assertEqual(longest_palindrome(s), 9)

if __name__ == "__main__":
    unittest.main()