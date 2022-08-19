'''
https://leetcode.com/problems/binary-tree-preorder-traversal/

Time: O(N) because we traverse all nodes once
Space: O(N) we keep track all nodes

Hint:
    - DFS
    - pay attention of pop(), it made the list pop in right first
    - This particular solution is iterative but you can have recursive too
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
            curr_node = stack.pop()
            if curr_node:
                result.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
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
        
    def test_program3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [1, 2, 4, 5, 3, 6, 7]
        
        self.assertEqual(solution.preorder_traversal(root), result)
        
        
if __name__ == '__main__':
    unittest.main()
        