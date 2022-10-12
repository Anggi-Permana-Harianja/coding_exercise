'''
https://leetcode.com/problems/linked-list-cycle-ii/

Time: O(N) since we travel all nodes
Space: O(1)

Hint:
    - Use Floyd's hare and tortoise algorithm,
      where there is one pointer will be faster (.next.next) and another with normal pace (.next)
'''

from typing import *

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    '''
    implement hare and tortoise race in get_intersect function
    '''
    def get_intersect(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head
        
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
            if hare == tortoise:
                return tortoise
            
        return None
    
    def detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        #get the intersect node from hare and tortoise race
        intersect = self.get_intersect(head)
        if not intersect:
            return None
        
        #walktrough between intersect and head, if the pointers meet, it is a cycle
        pointer_1 = intersect
        pointer_2 = head
        while pointer_1 != pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
            
        return pointer_1
    
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = head
        
        solution = Solution()
        
        result = head
        
        #print(result, solution.detect_cycle(head))
        
        self.assertEqual(solution.detect_cycle(head), result)
        
    def test_program2(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next.next
        
        solution = Solution()
        
        result = head.next.next
        
        #print(result, solution.detect_cycle(head))
        
        self.assertEqual(solution.detect_cycle(head), result)
        
    def test_program3(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        
        solution = Solution()
        
        result = None
        
        #print(result, solution.detect_cycle(head))
        
        self.assertEqual(solution.detect_cycle(head), result)
        
if __name__ == '__main__':
    unittest.main()