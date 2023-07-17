"""
https://leetcode.com/problems/diameter-of-binary-tree/

Vid. explanation: https://www.youtube.com/watch?v=bkxqA8Rfv04&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=11

Time: O(N) we traverse using DFS
Space: O(1) only store max diameter

Hint:
    - Bottom up using DFS
    - Keep track height and diameter each time we go up
"""

from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_binary_tree(root: Optional[TreeNode]) -> int:
    result = [0]

    # DFS function
    def dfs(root):
        if not root:
            return -1
        # traverse
        left_node = dfs(root.left)
        right_node = dfs(root.right)
        # count diameter
        # note: we use constant of 2, please watch the vid explation to find out why
        result[0] = max(result[0], 2 + left_node + right_node)

        # return and keep track height
        return 1 + max(left_node, right_node)
    
    dfs(root)

    return result[0]

class TestCases(unittest.TestCase):
    def test_case1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=3)
        root.left.left = TreeNode(val=4)
        root.left.right = TreeNode(val=5)

        return self.assertEqual(diameter_binary_tree(root), 3)
    
    def test_case2(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=3)
        root.right.right = TreeNode(val=4)

        return self.assertEqual(diameter_binary_tree(root), 3)
    
if __name__ == "__main__":
    unittest.main()
