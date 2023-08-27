"""
Blind 75
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Time: O(amount * num coins)
Space:O(amount)

Hint:
    - Create an array size of amount to store the minimum coin for that particular amount
"""

from typing import List
import unittest

def num_of_counts_for_change(coins: List[int], amount: int) -> int:
    # Initialize an array to store minimim coin for each amount
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    # Calculate the minimum change of coin for each amount from 1 to amount
    for i in range(1, amount + 1):
        for coin in coins:
            # Make sure we only coin < the particular amount
            # for example, it would be useless to count change
            # for $5 if we only have coin of $10
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If min_coins[amount] not change, there is no valid combination
    return min_coins[amount] if min_coins[amount] != float("inf") else -1

class TestCase(unittest.TestCase):
    def test_case1(self):
        coins = [1, 2, 5]
        amount = 11

        return self.assertEqual(num_of_counts_for_change(coins, amount), 3) # 2 coins of 5 and 1 coin of 1
    
    def test_case2(self):
        coins = [1, 2]
        amount = 5

        return self.assertEqual(num_of_counts_for_change(coins, amount), 3) # 2 coins of 2 and 1 coin of 1 instead of 5 coins of 1
    
if __name__ == "__main__":
    unittest.main()


