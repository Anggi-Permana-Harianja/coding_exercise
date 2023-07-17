"""
https://leetcode.com/problems/merge-two-binary-trees/

Time: O(tree1 + tree2)
Space: O(height of merged tree)

Hint:
    - just add val from both leaves and assign to new tree
"""

from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Optional[TreeNode], nodes_val: List[int]) -> List[int]:
    # base case
    if not root:
        return 
    nodes_val.append(root.val)
    dfs(root.left, nodes_val)
    dfs(root.right, nodes_val)

    return nodes_val

def merge_binary_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    # base case
    if not root1 and not root2:
        return None
    
    # sum values from both roots
    val1 = root1.val if root1 else 0 
    val2 = root2.val if root2 else 0
    root = TreeNode(val=val1 + val2)

    # traverse
    root.left = merge_binary_trees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = merge_binary_trees(root1.right if root1 else None, root2.right if root2 else None)

    return root

class TestCases(unittest.TestCase):
    def test_case1(self):
        root1 = TreeNode(val=1)
        root1.left = TreeNode(val=1)
        root1.right = TreeNode(val=1)

        root2 = TreeNode(val=2)
        root2.left = TreeNode(val=2)
        root2.right = TreeNode(val=2)

        return self.assertEqual(dfs(merge_binary_trees(root1, root2), []), [3, 3, 3])
    
    def test_case2(self):
        root1 = TreeNode(val=1)
        root1.left = TreeNode(val=1)

        root2 = TreeNode(val=1)
        root2.right = TreeNode(val=1)

        return self.assertEqual(dfs(merge_binary_trees(root1, root2), []), [2, 1, 1])
    
if __name__ == "__main__":
    unittest.main()
