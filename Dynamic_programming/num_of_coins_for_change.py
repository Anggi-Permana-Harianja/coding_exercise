#Link: https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change

#Time: O (nd); n=target amount, d=number of denominations
#Space: O(n)

def min_num_of_coins_for_change(n: int, denoms: list) -> int:
    num_of_coins = [float('inf') for _ in range(n + 1)]
    num_of_coins[0] = 0
    
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                num_of_coins[amount] = min(num_of_coins[amount], 1 + num_of_coins[amount - denom])
                
    return num_of_coins[-1] if num_of_coins[-1] != float('inf') else -1

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        n = 9
        denoms = [3, 5]
        
        result = 3
        
        self.assertEqual(min_num_of_coins_for_change(n, denoms), result)
        
    def test_program2(self):
        n = 7
        denoms = [2, 4]
        
        result = -1
        
        self.assertEqual(min_num_of_coins_for_change(n, denoms), result)
        
    def test_program3(self):
        n = 135
        denoms = [39, 45, 130, 40, 4, 1]
        
        result = 3
        
        self.assertEqual(min_num_of_coins_for_change(n, denoms), result)
        
if __name__ == '__main__':
    unittest.main()