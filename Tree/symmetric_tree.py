'''
https://leetcode.com/problems/symmetric-tree/

Time: O(N) because we traverse all nodes recursively
Space: O(N)

Hint: 
    - symmetric in this question means reflection where right == left, just like mirror
'''

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_reflective(root, root)
    
    def is_reflective(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        
        '''
        check left.val == right.val recurseively
        '''
        
        return (t1.val == t2.val) and self.is_reflective(t1.left, t2.right) and self.is_reflective(t1.right, t2.left)
        
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.is_symmetric(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        solution = Solution()
        
        result = False
        
        self.assertEqual(solution.is_symmetric(root), result)
        

if __name__ == '__main__':
    unittest.main()