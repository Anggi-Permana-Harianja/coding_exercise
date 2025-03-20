"""
### Merge Two Sorted Lists (Array Version)
#### Problem Description:
You are given two sorted lists `arr1` and `arr2`. Merge them into a single sorted list and return the result.

#### Example 1:
Input: arr1 = [1,2,4], arr2 = [1,3,4]
Output: [1,1,2,3,4,4]

#### Example 2:
Input: arr1 = [], arr2 = []
Output: []

#### Example 3:
Input: arr1 = [], arr2 = [0]
Output: [0]

#### Constraints:
- Both `arr1` and `arr2` are sorted in non-decreasing order.
- The function should return a new sorted merged list.

Time, space = O(m+n) because we traverse all elements, O(m+n) because we store m+n elements
"""

def merge_two_sorted_lists(arr1, arr2):
    i, j = 0, 0 # double pointer
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    #append the remaining elements for both
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

import unittest
class TestMergeTwoSortedLists(unittest.TestCase):
    def test_case1(self):
        arr1 = [1, 2, 4]
        arr2 = [1, 3, 4]
        result = [1, 1, 2, 3, 4, 4]
        self.assertEqual(merge_two_sorted_lists(arr1, arr2), result)
    
    def test_case2(self):
        arr1 = []
        arr2 = []
        result = []
        self.assertEqual(merge_two_sorted_lists(arr1, arr2), result)
    
    def test_case3(self):
        arr1 = []
        arr2 = [0]
        result = [0]
        self.assertEqual(merge_two_sorted_lists(arr1, arr2), result)
    
    def test_case4(self):
        arr1 = [1, 5, 7]
        arr2 = [2, 6, 8]
        result = [1, 2, 5, 6, 7, 8]
        self.assertEqual(merge_two_sorted_lists(arr1, arr2), result)

if __name__ == '__main__':
    unittest.main()