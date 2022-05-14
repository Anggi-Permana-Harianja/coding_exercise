#Link: https://leetcode.com/problems/design-linked-list/

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
    
    def print_linkedlist(self) -> str:
        str_ = ''
        curr_node = self.head
        
        for idx in range(self.size):
            str_ += f'{self.get(idx)}->'
            curr_node = curr_node.next
            
        return ''.join(str_[:-2])
    
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
        
        result = '2->7'
        
        self.assertEqual(my_linkedlist.print_linkedlist(), result)
        
    def test_program1(self):
        my_linkedlist = LinkedList()
        my_linkedlist.add_at_head(1)
        my_linkedlist.add_at_tail(2)
        my_linkedlist.add_at_index(1, 3)
        my_linkedlist.delete_at_index(1)
        my_linkedlist.delete_at_head()
        my_linkedlist.delete_at_tail()
        
        result = ''
        
        self.assertEqual(my_linkedlist.print_linkedlist(), result)
        
        
if __name__ == '__main__':
    unittest.main()
        