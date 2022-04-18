#Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

#Time: O(N)
#Space: O(N)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def min_depth(self, root)-> int:
        curr_node = root
        
        if not curr_node:
            return 0
        
        #collect children
        children = [curr_node.left, curr_node.right]
        
        #if we reach leaf node
        if not any(children):
            return 1
        
        #traverse the childern and update min_depth
        min_depth = float('inf')
        for child in children:
            if child is not None:
                min_depth = min(min_depth, self.min_depth(child))
                
        return min_depth + 1
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        root = Node(3)
        root.left = Node(9)
        root.right = Node(20)
        root.right.left = Node(15)
        root.right.right = Node(7)
        
        solution = Solution()
        
        result = 2
        
        self.assertEqual(solution.min_depth(root), result)
        
    def test_program2(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        
        solution = Solution()
        
        result = 3
        
        self.assertEqual(solution.min_depth(root), result)
        
if __name__ == '__main__':
    unittest.main()