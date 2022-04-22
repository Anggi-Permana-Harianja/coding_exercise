#Link: https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List

#Time: O(N)
#Space: O(1)

#Hint: This question has sorted ListNode

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        
    def get(self, index: int) -> int:
        #sanity check
        if index < 0 or index >= self.size:
            return -1 #not found
        
        curr_node = self.head
        for _ in range(index + 1):
            curr_node = curr_node.next
        
        return curr_node.val
    
    def add_at_index(self, index: int, val: int) -> None:
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
        
    def delete_at_index(self, index: int) -> None:
        #sanity check
        if index < 0 or index >= self.size:
            return 
        
        curr_node = self.head
        for _ in range(index):
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
        
        return self.delete_at_index(self.size)
    
    def print_linkedlist(self) -> str:
        str_ = ''
        curr_node = self.head
        for index in range(self.size):
            str_ += f'{self.get(index)}->'
            curr_node = curr_node.next
        
        return ''.join(str_[:-2])
    
    def remove_duplicates(self) -> None:
        
        index = 0
        while index < self.size:
            if self.get(index) == self.get(index + 1):
                self.delete_at_index(index)
                index -= 1 #this part is the trick, since .delete_at_index method update the self.size, we need to shift 1 index back
            index += 1
                
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self) -> None:
        MyLinkedList = LinkedList()
        MyLinkedList.add_at_head(1)
        MyLinkedList.add_at_tail(2)
        MyLinkedList.add_at_tail(3)
        MyLinkedList.add_at_tail(3)
        MyLinkedList.add_at_tail(3)
        MyLinkedList.add_at_tail(3)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.remove_duplicates()
        
        result = '1->2->3->4'
        
        self.assertEqual(MyLinkedList.print_linkedlist(), result)
        
    def test_program2(self) -> None:
        MyLinkedList = LinkedList()
        MyLinkedList.add_at_tail(1)
        MyLinkedList.add_at_tail(1)
        MyLinkedList.add_at_tail(3)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.add_at_tail(4)
        MyLinkedList.add_at_tail(5)
        MyLinkedList.add_at_tail(5)
        MyLinkedList.add_at_tail(5)
        MyLinkedList.add_at_tail(5)
        MyLinkedList.add_at_tail(6)
        MyLinkedList.remove_duplicates()
        
        result = '1->3->4->5->6'
        
        self.assertEqual(MyLinkedList.print_linkedlist(), result)
        
        
if __name__ == '__main__':
    unittest.main()
        