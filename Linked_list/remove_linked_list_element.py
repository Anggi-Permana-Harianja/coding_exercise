"""
https://leetcode.com/problems/remove-linked-list-elements/

Vid. explanation: https://www.youtube.com/watch?v=JI71sxtHTng&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=21

Time: O(N) we traverse all elements at most once
Space: O(N)

Hint:
    - We actually need two pointers (prev, curr) to handle if element we wanted to 
      remove is the head of LL
    - We still can use only one pointer, but we need to take head of LL as corner case
"""

from typing import Optional, List
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linked_list(head: Optional[ListNode]) -> List[int]:
    elements = []
    curr = head
    while curr:
        elements.append(curr.val)
        curr = curr.next

    return elements

def remove_linked_list_element(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # create a dummy node to be returned
    dummy = ListNode(next=head)
    # initialize two pointers
    prev, curr = dummy, head

    while curr:
        next = curr.next
        if curr.val == val:
            prev.next = next
        else:
            prev = curr
        curr = next

    return dummy.next


class TestCases(unittest.TestCase):
    def test_case1(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)
        head.next.next.next = ListNode(val=4)

        val=3

        return self.assertEqual(get_linked_list(remove_linked_list_element(head, val)), [1, 2, 4])

    def test_case2(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)

        val=1

        return self.assertEqual(get_linked_list(remove_linked_list_element(head, val)), [2, 3])
    
if __name__ == "__main__":
    unittest.main()
