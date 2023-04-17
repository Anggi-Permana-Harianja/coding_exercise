'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?

Time: O(n)
Space: O(1)

In order to solve this problem, we need to do three parts:
- reverse all list
- reverse the first K elements
- reverse all elements after K

example:
List = [1, 2, 3, 4, 5, 6]
K = 2
then:
Original list:    [1, 2, 3, 4, 5, 6]
Reverse entire:   [6, 5, 4, 3, 2, 1]
Reverse first k:  [5, 6, 4, 3, 2, 1]
Reverse remaining:[5, 6, 1, 2, 3, 4] (result)
'''

def rotate_list_inplace(my_list: list, k: int) -> list:
    n = len(my_list)
    k = k % n #reduce k to be less than n

    #reverse entire list
    reverse_list_inplace(my_list, 0, n - 1)

    #reverse first k elements
    reverse_list_inplace(my_list, 0, k - 1)

    #reverse elements after k
    reverse_list_inplace(my_list, k, n - 1)

    return my_list

def reverse_list_inplace(my_list: list, start: int, end: int) -> list:
    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

    return my_list

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        list_ = [1, 2, 3, 4, 5, 6]
        k = 2

        result = [5, 6, 1, 2, 3, 4]

        return self.assertEqual(rotate_list_inplace(list_, k), result)
    
    def test_program2(self):
        list_ = [7, 8, 9, 10, 11]
        k = 12

        result = [10, 11, 7, 8, 9]

        return self.assertEqual(rotate_list_inplace(list_, k), result)

if __name__ == '__main__':
    unittest.main()    