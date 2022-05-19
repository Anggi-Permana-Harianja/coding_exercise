#Link: https://www.algoexpert.io/questions/Non-Constructible%20Change

#Time: O(n log n)
#Space: O(1)

#Hint: Sort the array first

def non_constuctible_change(coins: list) -> int:
    if not coins:
        return 1
    
    if len(coins) == 1 and coins[0] > 1:
        return 1
    elif len(coins) ==  1 and coins[0] == 1:
        return 2
    
    coins.sort()
    
    for i in range(len(coins) - 1):
        diff = coins[i + 1] - sum(coins[: i + 1])
        if diff > 1:
            return sum(coins[: i + 1]) + 1
        
    return sum(coins) + 1

import unittest 
class TestProgram(unittest.TestCase):
    def test_program1(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        
        result = 20
        
        self.assertEqual(non_constuctible_change(coins), result)
        
    def test_program2(self):
        coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
        
        result = 55
        
        self.assertEqual(non_constuctible_change(coins) ,result)
        
    def test_program3(self):
        coins = [10]
        
        result = 1
        
        self.assertEqual(non_constuctible_change(coins), result)
        
    def test_program4(self):
        coins = [1]
        
        result = 2
        
        self.assertEqual(non_constuctible_change(coins), result)
        
if __name__ == '__main__':
    unittest.main()