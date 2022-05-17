#Link: https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change

#Time: O(nd); n=total amount, d=number of denominations
#Space: O(n)

#Hint: similar to num_of_coins_for_change question (https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change)

def num_of_ways_to_make_change(n: int, denoms: list) -> int:
    num_ways = [0 for _ in range(n + 1)]
    num_ways[0] = 1
    
    for denom in denoms:
        for amount in range(1, len(num_ways)):
            if denom <= amount:
                num_ways[amount] += num_ways[amount - denom]
                
    return num_ways[-1]

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        n = 25
        denoms = [1, 5, 10, 25]
        
        result = 13
        
        self.assertEqual(num_of_ways_to_make_change(n, denoms), result)
        
    def test_program2(self):
        n = 12
        denoms = [2, 3, 7]
        
        result = 4
        
        self.assertEqual(num_of_ways_to_make_change(n, denoms), result)
        
    def test_program3(self):
        n = 7
        denoms = [2, 3, 4, 7]
        
        result = 3
        
        self.assertEqual(num_of_ways_to_make_change(n, denoms), result)
        
if __name__ == '__main__':
    unittest.main()