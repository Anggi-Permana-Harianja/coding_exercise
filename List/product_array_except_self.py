"""
Blind 75
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Time: O(N)
Space: O(N)

Hint:
    - use sliding window both ends and then multiple nums from left and right
"""

from typing import List
import unittest

def product_array_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n

    # Sliding left side
    left_product = 1
    for i in range(n):
        # Product
        left_products[i] = left_product
        left_product *= nums[i]

    # Sliding right side
    right_product = 1
    for i in range(n - 1, -1, -1):
        right_products[i] = right_product
        right_product *= nums[i]

    return [left_num * right_num for left_num, right_num in zip(left_products, right_products)]

class TestCase(unittest.TestCase):
    def test_case1(self):
        nums = [1, 2, 3, 4]

        return self.assertEqual(product_array_except_self(nums), [24, 12, 8, 6])
    
    def test_case2(self):
        nums = [-1, 1, 0, -3, 3]

        return self.assertEqual(product_array_except_self(nums), [0, 0, 9, 0, 0])
    
if __name__ == "__main__":
    unittest.main()
