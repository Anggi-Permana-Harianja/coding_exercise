#Link: https://leetcode.com/problems/balanced-binary-tree/

#Time O(N log N)
#Space O(N)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def is_balance(self, root)->bool:
        curr_node = root
        return self.check_balance(curr_node) != -1
    
    def check_balance(self, root):
        curr_node = root
        
        #if not a tree means balanced
        if not curr_node:
            return True
        
        left_nodes = self.check_balance(curr_node.left)
        right_nodes = self.check_balance(curr_node.right)
        
        #if any sign of skewed tree, return -1, and carry this value through
        if abs(left_nodes - right_nodes) >= 2 or left_nodes == -1 or right_nodes == -1:
            return -1
        
        #get depth
        return max(left_nodes, right_nodes) + 1
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        root.right.left = Node(15)
        root.right.right = Node(7)
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.is_balance(root), result)
        
    def test_program2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(3)
        root.left.left.left = Node(4)
        root.left.left.right = Node(4)
        
        solution = Solution()
        
        result = False
        
        self.assertEqual(solution.is_balance(root), result)
        
    def test_program3(self):
        root = Node(None)
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.is_balance(root), result)
        
if __name__ == '__main__':
    unittest.main()