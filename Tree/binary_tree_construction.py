class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        curr_node = self
        if not curr_node:
            return
        
        if val <= curr_node.val:
            if not curr_node.left:
                curr_node.left = Node(val)
            else:
                curr_node.left.insert(val)
        elif val > curr_node.val:
            if not curr_node.right:
                curr_node.right = Node(val)
            else:
                curr_node.right.insert(val)
        return curr_node
    
def inorder_print(tree, array):
    curr_node = tree
    if not curr_node:
        return 

    inorder_print(curr_node.left, array)
    array.append(curr_node.val)
    inorder_print(curr_node.right, array)
        
    return ' '.join([str(item) for item in array])

import unittest
class TestProgram(unittest.TestCase):
    def test_case1(self):
        root = Node(5)
        root.insert(3)
        root.insert(2)
        root.insert(1)
        root.insert(8)
        root.insert(4)
        root.insert(7)
        root.insert(10)
        root.insert(9)
        root.insert(6)
        
        result = '1 2 3 4 5 6 7 8 9 10'
        
        self.assertEqual(inorder_print(root, []), result)

if __name__ == '__main__':
    unittest.main()
        