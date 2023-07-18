"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Vid. explanation https://www.youtube.com/watch?v=gs2LMfuOR9k&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=18

Time: O(N)
Space: O(1) we only store p, q and node.val

Hint:
    - This actually simple question, we only need to compare p, q with node.val
      if p > node.val and q > node.val then traverse to node.right
      elif p < node.val and q < node.val then traverse to node.left
      else: is the LCA (where the traverse is split to both directions)
"""

from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: Optional[TreeNode], p: int, q: int) -> int:
    curr_node = root
    while curr_node:
        if p > curr_node.val and q > curr_node.val:
            curr_node = curr_node.right
        elif p < curr_node.val and q < curr_node.val:
            curr_node = curr_node.left
        else:
            return curr_node.val
        
class TestCase(unittest.TestCase):
    def test_case1(self):
        root = TreeNode(val=2)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=3)

        p = 1
        q = 3

        result = 2

        return self.assertEqual(lowest_common_ancestor(root, p, q), result)
    
    def test_case2(self):
        root = TreeNode(val=6)
        root.right = TreeNode(val=8)
        root.right.left = TreeNode(val=7)
        root.right.right = TreeNode(val=9)

        p = 7
        q = 9

        result = 8

        return self.assertEqual(lowest_common_ancestor(root, p, q), result)
    

if __name__ == "__main__":
    unittest.main()
