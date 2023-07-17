"""
https://leetcode.com/problems/palindrome-linked-list/

vid. explanation: https://www.youtube.com/watch?v=yOzXms1J6Nk&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=13

Array solution:
Time: O(N)
Space: O(N)

Fast slow solution:
Time: O(N)
Space: O(1) # 1 on 1 comparison
"""

from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

def reverse_ll(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    while head:
        tmp = head.next
        head.next = prev_node
        prev_node = head
        head = tmp
        
    return prev_node

def palindrome_ll_array_solution(head: Optional[ListNode]) -> bool:
    nodes = []

    # traverse and store val
    while head:
        nodes.append(head.val)
        head = head.next

    # compare and return 
    return nodes == nodes[::-1]

def palindrome_fast_slow_solution(head: Optional[ListNode]) -> bool:
    # initialize fast and slow
    fast = head
    slow = head

    # traverse
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the first half and check palindrome
    left_hand, right_hand = head, reverse_ll(slow)
    while right_hand:
        if left_hand.val != right_hand.val:
            return False
        left_hand = left_hand.next
        right_hand = right_hand.next

    return True

class TestCases(unittest.TestCase):
    def test_case1(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=2)
        head.next.next.next = ListNode(val=1)

        return self.assertEqual(palindrome_ll_array_solution(head), True)
    
    def test_case2(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=2)
        head.next.next.next = ListNode(val=1)

        return self.assertEqual(palindrome_fast_slow_solution(head), True)
    
    def test_case3(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)
        head.next.next.next = ListNode(val=4)

        return self.assertEqual(palindrome_ll_array_solution(head), False)
    
    def test_case4(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)
        head.next.next.next = ListNode(val=4)
        head.next.next.next.next = ListNode(val=5)

        return self.assertEqual(palindrome_fast_slow_solution(head), False)


if __name__ == "__main__":
    unittest.main()
