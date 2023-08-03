"""
Blind 75
https://leetcode.com/problems/invert-binary-tree/description/

Time: O(N) we traverse each node once
Space: O(height of the tree)

Hint:
    - just swap left and right leaves
"""

import unittest
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_vals_using_dfs(root: Optional[TreeNode], nodes: List[int]) -> List[int]:
    if not root:
        return 
    
    nodes.append(root.val)
    get_tree_vals_using_dfs(root.left, nodes)
    get_tree_vals_using_dfs(root.right, nodes)

    return nodes


def invert_binary_tree(root: Optional[TreeNode]) -> TreeNode:
    # define exit condition
    if not root:
        return 
    
    # swap
    root.left, root.right = root.right, root.left
    invert_binary_tree(root.right)
    invert_binary_tree(root.left)

    return root

class TestCases(unittest.TestCase):
    def test_case1(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=3)

        return self.assertEqual(get_tree_vals_using_dfs(invert_binary_tree(root), []), [1, 3, 2])
    
    def test_case2(self):
        root = TreeNode(val=1)
        root.left = TreeNode(val=2)
        root.right = TreeNode(val=3)
        root.left.left = TreeNode(val=4)
        root.right.right = TreeNode(val=5)

        return self.assertEqual(get_tree_vals_using_dfs(invert_binary_tree(root), []), [1, 3, 5, 2, 4])
    
if __name__ == "__main__":
    unittest.main()
