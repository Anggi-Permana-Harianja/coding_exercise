'''
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make,
 determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

Time: O(N)
Space: O(1)
'''

def can_reach_end(alist: int) -> bool:
    n = len(alist)
    i = 0
    while i < n:
        # if reach end return True
        if i == n - 1:
            return True
        
        #if first hop is 0 return False
        #or hop end on 0 but not yet reach end
        if alist[i] == 0:
            return False
        
        next_idx = i + alist[i]

        #if hop exceed or end at the end of list, return True
        if next_idx >= n:
            return True
        
        #if next is 0, return False
        if next_idx == 0:
            return False
        
        i = next_idx
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        alist = [2, 0, 1, 0]

        return self.assertEqual(can_reach_end(alist), True)
    
    def test_program2(self):
        alist = [1, 1, 0, 1]

        return self.assertEqual(can_reach_end(alist), False)
    
if __name__ == '__main__':
    unittest.main()