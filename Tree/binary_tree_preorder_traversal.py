'''
https://leetcode.com/problems/binary-tree-preorder-traversal/

Time: O(N) because we traverse all nodes once
Space: O(N) we keep track all nodes

Hint:
    - DFS
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, result = [root], []
        
        while stack:
            curr_node = stack.pop(0)
            if curr_node:
                result.append(curr_node.val)
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)
                    
        return result
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        solution = Solution()
        
        result = [1, 2, 3]
        
        self.assertEqual(solution.preorder_traversal(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.right = TreeNode(5)
        
        solution = Solution()
        
        result = [1, 2, 3, 4, 5]
        
        self.assertEqual(solution.preorder_traversal(root), result)
        
        

if __name__ == '__main__':
    unittest.main()
        