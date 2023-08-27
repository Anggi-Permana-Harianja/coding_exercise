"""
Blind 75
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Time: O(N)
Space: O(1) only save slow and fast node
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def has_cycle_hash(self, head: list[ListNode]) -> bool:
        hash_set = set()
        
        curr_node = head
        while curr_node is not None:
            if curr_node in hash_set:
                return True
            hash_set.add(curr_node)
            curr_node = curr_node.next
            
        return False
    
    def has_cycle_floyd_cycle(self, head: list[ListNode]) -> bool:
        '''
        floyd cycle algorithm idea is to create two pointer [slow, fast]
        if there is a cycle somehow the fast will catch up the slow
        '''
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        head = ListNode(3)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(0)
        head.next.next.next.next = head.next #0->1 cycle
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.has_cycle_hash(head), result)
        self.assertEqual(solution.has_cycle_floyd_cycle(head), result)
        
    def test_program2(self):
        head = ListNode(3)
        head.next = ListNode(1)
        head.next.next = ListNode(4)
        
        solution = Solution()
        
        result = False
        
        self.assertEqual(solution.has_cycle_hash(head), result)
        self.assertEqual(solution.has_cycle_floyd_cycle(head), result)
        
        
if __name__ == '__main__':
    unittest.main()