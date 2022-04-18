#Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

#Time: O(N)
#Space: worst is O(N), best case is O(log(N))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def max_depth(self, root)-> int:
        curr_node = root
        if not curr_node:
            return 0
        left_nodes = self.max_depth(curr_node.left)
        right_nodes = self.max_depth(curr_node.right)
        
        return max(left_nodes, right_nodes) + 1
    

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = 3
        
        self.assertEqual(solution.max_depth(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = 3
        
        self.assertEqual(solution.max_depth(root), result)
        
if __name__ == '__main__':
    unittest.main()