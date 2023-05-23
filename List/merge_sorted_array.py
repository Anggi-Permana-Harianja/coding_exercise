'''
https://leetcode.com/problems/merge-sorted-array/

Time: O(m + n)
Space: O(1) since we are computing in place

hints:
    - using 3 pointers
    - loop backwards
'''

def merge(nums1: list[int], nums2: list[int], m: int, n: int) -> list[int]:
    p1 = m - 1
    p2 = n - 1
    p = len(nums1) - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        m = 3
        n = 3
        
        result = [1,2,2,3,5,6]
        
        self.assertEqual(merge(nums1, nums2, m, n), result)
        
    def test_program2(self):
        nums1 = [4,5,6,0,0,0]
        nums2 = [1, 2, 3]
        m = 3
        n = 3
        
        result = [1,2,3,4,5,6]
        
        self.assertEqual(merge(nums1, nums2, m, n), result)
        
if __name__ == '__main__':
    unittest.main()