#Link: https://leetcode.com/problems/path-sum/

#Time: O(N)
#Space: O(1)

#Hint:
#--- Use DFS to calculate branch sums

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def has_path_sum(self, root: Node, target_sum: int) -> bool:
        running_sum = 0
        has_path = self.has_path_sum_helper(root, running_sum, target_sum)

        return has_path
    
    def has_path_sum_helper(self, root: Node, running_sum: int, target_sum: int) -> bool:
        curr_node = root
        if not curr_node:
            return False
        
        # calculate running_sum
        running_sum += curr_node.val

        # check exit condition 
        if not curr_node.left and not curr_node.right:
            return running_sum == target_sum
        
        # traverse the rest of tree
        left_nodes = self.has_path_sum_helper(curr_node.left, running_sum, target_sum)
        right_nodes = self.has_path_sum_helper(curr_node.right, running_sum, target_sum)

        return left_nodes or right_nodes
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = Node(5)
        root.left = Node(4)
        root.right = Node(8)
        root.left.left = Node(11)
        root.right.left = Node(13)
        root.right.right = Node(14)
        root.left.left.left = Node(7)
        root.left.left.right = Node(2)
        root.right.right.right = Node(1)
        targetSum = 22
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.has_path_sum(root, targetSum), result)
        
    def test_program2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        targetSum = 5
        
        solution = Solution()
        
        result = False
        
        self.assertEqual(solution.has_path_sum(root, targetSum), result)
        
if __name__ == '__main__':
    unittest.main()