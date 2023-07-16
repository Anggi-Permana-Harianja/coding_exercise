"""
https://leetcode.com/problems/merge-two-sorted-lists/


"""
from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_linked_list(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create dummy LL
        dummy = ListNode()
        tail_ll = dummy

        # traverse both list1 and list2
        while list1 and list2:
            if list1.val < list2.val:   
                tail_ll.next = list1
                list1 = list1.next
            else:
                tail_ll.next = list2
                list2 = list2.next
            tail_ll = tail_ll.next

        # if any of LL is finished first, just add the rest of unfinished LL
        if not list1:
            tail_ll.next = list2
        else:
            tail_ll.next = list1

        return dummy.next
    

class TestCase(unittest.TestCase):
    def compare_ll(self, result, groundtruth):
        while result and groundtruth:
            if result.val != groundtruth.val:
                self.assertFalse("Not passed")
            result = result.next
            groundtruth = groundtruth.next

        return self.assertTrue("Passed")

    def test_case1(self):
        list1 = ListNode(val=1)
        list1.next = ListNode(val=2)
        list1.next.next = ListNode(val=3)
        list2 = ListNode(val=4)
        list2.next = ListNode(val=5)
        list2.next.next = ListNode(val=6)

        result = ListNode(val=1)
        result.next = ListNode(val=2)
        result.next.next = ListNode(val=3)
        result.next.next.next = ListNode(val=4)
        result.next.next.next.next = ListNode(val=5)
        result.next.next.next.next.next = ListNode(val=6)

        solution = Solution()

        return self.compare_ll(solution.merge_two_linked_list(list1, list2), result)
    
if __name__ == "__main__":
    unittest.main()
