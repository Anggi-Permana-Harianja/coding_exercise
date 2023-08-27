"""
Blind 75
https://leetcode.com/problems/maximum-product-subarray/description/

Another modification of Kadane, the difference is here we use multiply
which is negative number to take care differently than sum

Hint:
    - Use Kadane

Time: O(N)
Space: O(1) # We only store max_product, min_product
"""

from typing import List
import unittest

def maximum_product_subarray(arr: List[int]) -> int:
    if not arr:
        return 0
    
    result = max_product = min_product = arr[0]

    for i in range(1, len(arr)):
        # Handle negative by swapping
        if arr[i] < 0:
            max_product, min_product = min_product, max_product

        # Update max_product and min_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])

        # Update the result
        result = max(result, max_product)

    return result

class TestCase(unittest.TestCase):
    def test_case1(self):
        arr = [1, 2, 3, 4]

        return self.assertEqual(maximum_product_subarray(arr), 24)
    
    def test_case2(self):
        arr = [2, 3, -2, 4]

        return self.assertEqual(maximum_product_subarray(arr), 6)
    
    def test_case3(self):
        arr = [-2, 0, -1]

        return self.assertEqual(maximum_product_subarray(arr), 0)
    
if __name__ == "__main__":
    unittest.main()
