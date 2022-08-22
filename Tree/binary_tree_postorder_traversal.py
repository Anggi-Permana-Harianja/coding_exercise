'''
https://leetcode.com/problems/binary-tree-postorder-traversal/

Time: O(N)
Space: O(N)

Hint:
    - This approach is using iterative
    - same as pre-order but starts from left and return in reverse
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, result = [root], []
        
        curr_node = root
        while stack:
            curr_node = stack.pop()
            if curr_node:
                result.append(curr_node.val)
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
                
        return result[::-1]
    
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
        
        result = [4, 5, 2, 6, 7, 3, 1]
        
        self.assertEqual(solution.postorder_traversal(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        
        solution = Solution()
        
        result = [2, 4, 5, 3, 1]
        
        self.assertEqual(solution.postorder_traversal(root), result)
        
    def test_program3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        solution = Solution()
        
        result = [4, 5, 2, 3, 1]
        
        self.assertEqual(solution.postorder_traversal(root), result)
        

if __name__ == '__main__':
    unittest.main()