#Link: https://www.algoexpert.io/questions/Branch%20Sums

#Time: O(N)
#Space: O(N)

#Hint: Use DFS to traverse all branch

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def branch_sums(self, root)->list[int]:
        branch_sums = []
        running_sum = 0
        self.branch_sums_helper(root, branch_sums, running_sum)
        
        return branch_sums
    
    def branch_sums_helper(self, root, branch_sums, running_sum)->list[int]:
        curr_node = root
        
        if not curr_node:
            return 0
        
        running_sum += curr_node.val
        
        if not curr_node.left and not curr_node.right:
            branch_sums.append(running_sum)
            running_sum = 0
            
        left_nodes = self.branch_sums_helper(curr_node.left, branch_sums, running_sum)
        right_nodes = self.branch_sums_helper(curr_node.right, branch_sums, running_sum)
        
        return left_nodes or right_nodes

import unittest
class TestProgram(unittest.TestCase):
    def test_program(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        root.left.right.left = Node(10)
        
        solution = Solution()
        
        result = [15, 16, 18, 10, 11]
        
        self.assertEqual(solution.branch_sums(root), result)
        
if __name__ == '__main__':
    unittest.main()