"""
Blind 75
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Time: O(row * col)
Space: O(row * col)

Hint:
    - Use DFS
"""

from typing import List
import unittest

def dfs(image: List[List[int]], row: int, col: int, new_color: int, start_color: int) -> List[List[int]]:
    # Set boundary for DFS
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start_color:
        return 
    
    # Update row col to new color
    image[row][col] = new_color

    # DFS to up down left right
    dfs(image, row - 1, col, new_color, start_color)
    dfs(image, row + 1, col, new_color, start_color)
    dfs(image, row, col - 1, new_color, start_color)
    dfs(image, row, col + 1, new_color, start_color)

def flood_fill(image: List[List[int]], start_row:int, start_col: int, new_color: int) -> List[List[int]]:
    # Skip if the row col already new color
    if image[start_row][start_col] == new_color:
        return image
    
    # DFS
    dfs(image, start_row, start_col, new_color, image[start_row][start_col])

    return image

class TestCase(unittest.TestCase):
    def test_case1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        start_row = 1
        start_col = 1
        color = 2

        result = [[2,2,2],[2,2,0],[2,0,1]]

        return self.assertEqual(flood_fill(image, start_row, start_col, color), result)

    def test_case2(self):
        image = [[0,0,0],[0,0,0]]
        start_row = 0
        start_col = 0
        color = 0

        result = [[0, 0, 0], [0, 0, 0]]

        return self.assertEqual(flood_fill(image, start_row, start_col, color), result)


if __name__ == "__main__":
    unittest.main()
