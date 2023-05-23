"""
https://leetcode.com/problems/reverse-linked-list-ii/description/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_between(self, head: ListNode, left: int, right: int) -> ListNode:
        # no changes since left == right
        if not head or left == right:
            return head
        
        '''
        Dummy part is to counter that if we have left == 0 and right == end of LL
        thus we have to reverse entire LL
        '''
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy

        # move the prev_node into left idx
        for i in range(left - 1):
            prev_node = prev_node.next

        # reverse the nodes between left idx and right idx
        curr_node = prev_node.next
        for _ in range(right - left):
            tmp_node = curr_node.next
            curr_node.next = tmp_node.next
            tmp_node.next = prev_node.next
            prev_node.next = tmp_node

        return dummy.next
    
import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        solution = Solution()
        result = []
        reversed_in_between = solution.reverse_between(head, 2, 4)
        while reversed_in_between:
            result.append(reversed_in_between.val)
            reversed_in_between = reversed_in_between.next

        self.assertEqual(result, [1, 4, 3, 2, 5])

if __name__ == "__main__":
    unittest.main()
