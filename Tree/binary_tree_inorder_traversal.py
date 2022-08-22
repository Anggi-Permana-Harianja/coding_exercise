'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

Time: O(N)
Space: O(N)

Hint:
    - This approach is iterative one
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        
        stack, result = [], []
        
        curr_node = root
        while True:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
                
            if not stack:
                return result
            
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
            
        return result
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [4, 2, 5, 1, 6, 3, 7]
        
        
        self.assertEqual(solution.inorder_traversal(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [1, 6, 3, 7]
        
        self.assertEqual(solution.inorder_traversal(root), result)
        
        
    def test_program3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [2, 1, 6, 3, 7]
        
        self.assertEqual(solution.inorder_traversal(root), result)
        
        
if __name__ == '__main__':
    unittest.main()