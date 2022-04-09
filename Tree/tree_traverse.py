### Q1: Tree traversals (Inorder, Preorder, Postorder)
#[GeekforGeeks](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
#input
#            +
#         /     \
#      +         *
#    /   \      /  \
#    3   5     1    4


#create tree class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def preorder_print(tree, array):
    curr_node = tree
    if not curr_node:
        return 
    array.append(curr_node.val)
    preorder_print(curr_node.left, array)
    preorder_print(curr_node.right, array)
    
    return ' '.join(array)

def inorder_print(tree, array):
    curr_node = tree
    if not curr_node:
        return 
    inorder_print(curr_node.left, array)
    array.append(curr_node.val)
    inorder_print(curr_node.right, array)
    
    return ' '.join(array)
    
def postorder_print(tree, array):
    curr_node = tree
    if not curr_node:
        return
    postorder_print(curr_node.left, array)
    postorder_print(curr_node.right, array)
    array.append(curr_node.val)
    
    return ' '.join(array)

import unittest
class TestProgram(unittest.TestCase):
    def test_case1(self):
        root = Node('+')
        root.left = Node('+')
        root.right = Node('*')
        root.left.left = Node('3')
        root.left.right = Node('5')
        root.right.left = Node('1')
        root.right.right = Node('4')
        
        inorder = '3 + 5 + 1 * 4'
        preorder = '+ + 3 5 * 1 4'
        postorder = '3 5 + 1 4 * +'
        
        self.assertEqual(inorder_print(root, []), inorder)
        self.assertEqual(preorder_print(root, []), preorder)
        self.assertEqual(postorder_print(root, []), postorder)
    
    def test_case2(self):
        root = Node('+')
        root.left = Node('+')
        root.right = Node('*')
        root.left.left = Node('*')
        root.left.left.left = Node('2')
        root.left.left.right = Node('4')
        root.left.right = Node('5')
        root.right.left = Node('1')
        root.right.right = Node('+')
        root.right.right.left = Node('6')
        root.right.right.right = Node('7')
        
        inorder = '2 * 4 + 5 + 1 * 6 + 7'
        preorder = '+ + * 2 4 5 * 1 + 6 7'
        postorder = '2 4 * 5 + 1 6 7 + * +'
        
        self.assertEqual(inorder_print(root, []), inorder)
        self.assertEqual(preorder_print(root, []), preorder)
        self.assertEqual(postorder_print(root, []), postorder)
        
if __name__ == '__main__':
    unittest.main()