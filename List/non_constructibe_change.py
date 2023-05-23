#Link: https://www.algoexpert.io/questions/Non-Constructible%20Change

#Time: O(n log n) because of sort
#Space: O(1)

#Hint: Sort the array first

def non_constuctible_change(coins: list) -> int:
    coins.sort()
    min_change = 0

    for denom in coins:
        if denom > min_change + 1:
            return min_change + 1
        min_change += denom

    return min_change + 1

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