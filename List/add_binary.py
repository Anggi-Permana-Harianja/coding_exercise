"""
Blind 75
https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

 
Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Time: O(N)
Space: O(N)
"""

import unittest

def add_binary(a: str, b: str) -> str:
    carry = 0
    result = []

    # Iterate from right to left
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry > 0:
        # Get the current value
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Calculate the sum and the carry
        total = digit_a + digit_b + carry

        # Update the carry
        carry = total //  2
        result.append(str(total % 2))

        i -= 1
        j -= 1

    return ''.join(result[::-1])

class TestCase(unittest.TestCase):
    def test_case1(self):
        a = "11"
        b = "1"

        return self.assertEqual(add_binary(a, b), "100")
    
    def test_case2(self):
        a = "1010"
        b = "1011"

        return self.assertEqual(add_binary(a, b), "10101")
    
if __name__ == "__main__":
    unittest.main()
