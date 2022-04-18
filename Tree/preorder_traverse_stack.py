class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def preorder_traversal(self, root:[TreeNode]) -> list[int]:
        stack, results = [root], []
        
        while stack:
            curr_node = stack.pop(0)
            if curr_node is not None:
                results.append(curr_node.val)
                if curr_node.right is not None:
                    stack.append(curr_node.right)
                if curr_node.left is not None:
                    stack.append(curr_node.left)
                    
        return result
    
array = [1, None, 2, 3]
solution = Solution()
print(solution.preorder_traversal(array))