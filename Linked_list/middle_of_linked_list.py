"""
Blind 75
https://leetcode.com/problems/middle-of-the-linked-list/description/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Time: O(N)
Space: O(1) because we only store value for fast and slow

Hint:
    - Use slow and fast approach
"""

from typing import Any
import unittest

class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = None

def middle_of_linked_list(head: ListNode) -> int:
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.val

class TestCase(unittest.TestCase):
    def test_case1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        return self.assertEqual(middle_of_linked_list(head), 3)
    
    def test_case2(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)

        return self.assertEqual(middle_of_linked_list(head), 4)
    
if __name__ == "__main__":
    unittest.main()
