#Link: https://leetcode.com/problems/design-linked-list/


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def get(self, index:int)->int:
        #sanity check
        if index < 0 or index >= self.size:
            return -1 #not found
        
        curr_node = self.head
        for _ in range(index + 1):
            curr_node = curr_node.next
            
        return curr_node.val
    
    def add_at_index(self, index:int, val:int)->None:
        #sanity check
        if index > self.size:
            return 
        
        if index < 0:
            index = 0
            
        curr_node = self.head
        new_node = ListNode(val)
        
        for _ in range(index):
            curr_node = curr_node.next
            
        new_node.next = curr_node.next
        curr_node.next = new_node
        
        #update size
        self.size += 1
        
    def delete_at_index(self, index:int)->None:
        #sanity check
        if index < 0 or index >= self.size:
            return 
        
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        
        curr_node.next = curr_node.next.next
        
        #update size
        self.size -= 1
        
    def add_at_head(self, val:int)->None:
        
        return self.add_at_index(0, val)
    
    def add_at_tail(self, val:int)->None:
        
        return self.add_at_index(0, self.size)
    
    def delete_at_head(self)->None:
        
        return self.delete_at_index(0)
    
    def delete_at_tail(self)->None:
        
        return self.delete_at_index(self.size)
    
    def print_linkedlist(self)->list:
        str_ = ''
        curr_node = self.head
        for index in range(self.size):
            str_ += f'{self.get(index)}->'
            curr_node = curr_node.next
            
        return ''.join(str_[:-2])
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        my_linked_list = LinkedList()
        my_linked_list.add_at_head(1)
        my_linked_list.add_at_tail(3)
        my_linked_list.add_at_index(1, 2)
        my_linked_list.delete_at_head()
        my_linked_list.add_at_tail(4)
        my_linked_list.delete_at_tail()
        my_linked_list.delete_at_index(1)
        my_linked_list.add_at_head(5)
        my_linked_list.add_at_tail(6)
        
        result = '3->5->2->1'
        
        self.assertEqual(my_linked_list.print_linkedlist(), result)
        
if __name__ == '__main__':
    unittest.main()