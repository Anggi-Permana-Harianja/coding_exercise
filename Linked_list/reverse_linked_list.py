#Link: https://www.algoexpert.io/questions/Reverse%20Linked%20List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        
    def get(self, idx: int) -> int:
        #sanity check
        if idx < 0 or idx >= self.size:
            return -1
        
        curr_node = self.head
        for _ in range(idx + 1):
            curr_node = curr_node.next
            
        return curr_node.val
    
    def add_at_index(self, idx: int, val: int) -> None:
        if idx > self.size:
            return
       
        if idx < 0:
            idx = 0
            
        curr_node = self.head
        new_node = ListNode(val)
        
        for _ in range(idx):
            curr_node = curr_node.next
            
        new_node.next = curr_node.next
        curr_node.next = new_node
        
        #update size
        self.size += 1
           
    def delete_at_index(self, idx: int) -> None:
        if idx < 0 or idx >= self.size:
            return
        
        curr_node = self.head
        for _ in range(idx):
            curr_node = curr_node.next
            
        curr_node.next = curr_node.next.next
        
        #update size
        self.size -= 1
        
    def add_at_head(self, val: int) -> None:
        return self.add_at_index(0, val)
    
    def add_at_tail(self, val: int) -> None:
        return self.add_at_index(self.size, val)
    
    def delete_at_head(self) -> None:
        return self.delete_at_index(0)
    
    def delete_at_tail(self) -> None:
        return self.delete_at_index(self.size-1)
    
def reverse(linked_list: LinkedList) -> list:
    reversed_in_list = []
    curr_node = linked_list.head
    prev_node = None
    
    '''
    To reverse a linkedlist here is the sequence to work 
    - next_node, curr_node.next, prev_node, curr_node
    '''
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        reversed_in_list.append(prev_node.val)
       
    return reversed_in_list

def nodes_in_array(linked_list: LinkedList) -> list:
    return_list = []
    curr_node = linked_list.head
    
    while curr_node is not None:
        return_list.append(curr_node.val)
        curr_node = curr_node.next
        
    return return_list
            
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        my_linkedlist = LinkedList()
        my_linkedlist.add_at_head(1)
        my_linkedlist.add_at_tail(3)
        my_linkedlist.add_at_index(1, 2)
        my_linkedlist.add_at_head(4)
        my_linkedlist.delete_at_index(1)
        my_linkedlist.delete_at_head()
        my_linkedlist.delete_at_tail()
        my_linkedlist.add_at_tail(7)
        reversed_in_list = reverse(my_linkedlist)
        
        result = [7, 2]
        
        self.assertEqual(nodes_in_array(my_linkedlist), result)
         
        
if __name__ == '__main__':
    unittest.main()