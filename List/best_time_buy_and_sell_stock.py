"""
Blind 75

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Time: O(N)
Space: O(1)

Hint
    - Use Kadane algorithm

"""

def max_profit(prices:list[int]) -> int:
    max_profit = 0
    min_value = float('inf')
    
    for i in range(len(prices)):
        min_value = min(min_value, prices[i])
        max_profit = max(max_profit, (prices[i] - min_value))
        
    return max_profit


import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        prices = [7,1,5,3,6,4]
        
        result = 5
        
        self.assertEqual(max_profit(prices), result)
    
    def test_program2(self):
        prices = [7,6,4,3,1]
        
        result = 0
        
        self.assertEqual(max_profit(prices), result)
        
if __name__ == '__main__':
    unittest.main()