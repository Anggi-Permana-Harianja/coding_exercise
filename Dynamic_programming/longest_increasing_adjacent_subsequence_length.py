'''
Suppose you have an array of n integers, and you want to find the length of the longest increasing adjacent subsequence (LIS) of the array. 
A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. 
An increasing subsequence is a subsequence in which the elements are in increasing order.

For example, consider the array arr = [3, 4, -1, 0, 6, 2, 3]. 
The longest increasing subsequence of this array is [3, 4] or [2, 3] or [-1, 0], which has a length of 2.

arr:  3  4 -1  0  6  2  3
dp:   1  2  1  2  1  1  2

Time: O(n^2)
Space: O(n)
'''

def longest_increasing_adjacent_subsequence_length(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and i - j <= 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)