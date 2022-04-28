#Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

#Time: O(N)
#Space: O(N)

#Hint: use DFS traversal

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def level_order(self, root) -> list[list[int]]:
        result = []
        level = 0
        curr_node = root
        
        return self.helper(result, curr_node, level)
    
    def helper(self, result: list, curr_node: TreeNode, level: int) -> list[list[int]]:
        if not curr_node:
            return 
        
        if level == len(result):
            result.append([])
            
        if curr_node is not None:
            result[level].append(curr_node.val)
            
        if curr_node.left is not None:
            self.helper(result, curr_node.left, level=level+1)
        if curr_node.right is not None:
            self.helper(result, curr_node.right, level=level+1)
            
        return result
            
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [[3], [9, 20], [15, 7]]
        
        self.assertEqual(solution.level_order(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [[1], [2, 3], [4, 5, 6, 7]] #[4, 5, 6, 7] are in depth=3
        
        self.assertEqual(solution.level_order(root), result)
        
        
        
if __name__ == '__main__':
    unittest.main()
