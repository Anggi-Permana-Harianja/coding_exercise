"""
Blind 75
https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]


    [1, 2] doesn't overlap with newInterval since 2 < 4, so it's added as is.
    [3, 5] overlaps with newInterval since 3 <= 8, so we merge them to [3, 8].
    [6, 7] overlaps with newInterval since 6 <= 8, so we merge them to [3, 8].
    [8, 10] overlaps with newInterval since 8 <= 8, so we merge them to [3, 10].
    [12, 16] doesn't overlap with newInterval since 12 > 8, so it's added as is.

The final result is [[1, 2], [3, 10], [12, 16]].

Time: O(N)
Space: O(N)

Hint:
    - There are two conditions
        - add as it is, no need to merge
        - merge
"""

from typing import List
import unittest

def insert_inteval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # Reserve empty list
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that no need to merge
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Add intervals that need to merge
    while i < n and intervals[i][0] <= new_interval[1]:
        # Update new_interval
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    # Add newly updated new_interval
    result.append(new_interval)

    # Add remaining interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

class TestCase(unittest.TestCase):
    def test_case1(self):
        intervals = [[1,3],[6,9]]
        new_interval = [2,5]

        result = [[1, 5], [6, 9]]

        return self.assertEqual(insert_inteval(intervals, new_interval), result)

    def test_case2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        new_interval = [4, 8]

        result = [[1,2],[3,10],[12,16]]

        return self.assertEqual(insert_inteval(intervals, new_interval), result)
    
if __name__ == "__main__":
    unittest.main()
