'''
https://leetcode.com/problems/richest-customer-wealth/
Time: O(M * N)
Space: O(1) -> because we only track max_wealth and current_wealth

The approach is based on Kadane algorithm
'''

def maximum_wealth(accounts: list[list[int]]) -> int:
    max_wealth = 0
    for account in accounts:
        current_wealth = sum(account)
        max_wealth = max(max_wealth, current_wealth)
        
    return max_wealth

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        accounts = [[1,2,3],[3,2,1]]
        result = 6
        
        self.assertEqual(maximum_wealth(accounts), result)
        
    def test_program2(self):
        accounts = [[1,5],[7,3],[3,5]]
        result = 10
        
        self.assertEqual(maximum_wealth(accounts), result)
        

if __name__ == '__main__':
    unittest.main()
