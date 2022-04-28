#Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

#Time: O(N)
#Space: O(N)

#Hint: using depth-level technique from https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def average_of_level(self, root) -> list[float]:
        result = []
        level = 0
        curr_node = root
        
        dfs_traverse = self.helper([], curr_node, level)
        
        for num in dfs_traverse:
            result.append(sum(num) / len(num))
            
        return result
    
    def helper(self, dfs_traverse, curr_node, level) -> list[list[int]]:
        if curr_node is None:
            return
        
        if level == len(dfs_traverse):
            dfs_traverse.append([])
            
        if curr_node is not None:
            dfs_traverse[level].append(curr_node.val)
            
        if curr_node.left is not None:
            self.helper(dfs_traverse, curr_node.left, level+1)
        if curr_node.right is not None:
            self.helper(dfs_traverse, curr_node.right, level+1)
            
        return dfs_traverse
    
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [3.0, 14.5, 11.0]
        
        self.assertEqual(solution.average_of_level(root), result)
        
    def test_program2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        
        result = [1, 2.5, 5.5]
        
        self.assertEqual(solution.average_of_level(root), result)
        
if __name__ == '__main__':
    unittest.main()