'''
https://leetcode.com/problems/intersection-of-two-linked-lists/

Time: O(M + N) because we use two pointers
Space: O(1) we only check current nodes for each pointers

Hint
    - There are two pointers, longer one and short one
    - for short one:
        - the traverse: short LL -> common LL -> long LL
    - for long one:
        - the traverse: long LL -> common LL -> short LL
    - this approach works like magic, you can test it on paper
'''

from typing import *

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        #initiate two pointers
        pointer_a = head_a
        pointer_b = head_b
        
        while pointer_a != pointer_b:
            pointer_a = head_b if not pointer_a else pointer_a.next
            pointer_b = head_a if not pointer_b else pointer_b.next
            
        return pointer_a
    
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        head_a = ListNode(1)
        head_a.next = ListNode(2)
        head_a.next.next = ListNode(3)
        
        head_b = ListNode(10)
        head_b.next = head_a.next
        head_b.next.next = head_a.next.next
        
        solution = Solution()
        
        result = head_a.next
        
        #print(solution.get_intersection_node(head_a, head_b), result)
        
        self.assertEqual(solution.get_intersection_node(head_a, head_b), result)

    def test_program2(self):
        head_a = ListNode(1)
        head_a.next = ListNode(2)
        head_a.next.next = ListNode(3)
        head_a.next.next.next = ListNode(4)
        
        head_b = ListNode(10)
        head_b.next = ListNode(9)
        head_b.next.next = head_a.next
        head_b.next.next.next = head_a.next.next
        head_b.next.next.next.next = head_a.next.next.next
        
        solution = Solution()
        
        result = head_a.next
        
        #print(solution.get_intersection_node(head_a, head_b), result)
        
        self.assertEqual(solution.get_intersection_node(head_a, head_b), result)
        
    def test_program3(self):
        head_a = ListNode(1)
        head_a.next = ListNode(2)
        
        head_b = ListNode(10)
        head_b.next = ListNode(9)
        
        solution = Solution()
        
        result = None
        
        #print(solution.get_intersection_node(head_a, head_b), result)
        
        self.assertEqual(solution.get_intersection_node(head_a, head_b), result)
        
if __name__ == '__main__':
    unittest.main()
        