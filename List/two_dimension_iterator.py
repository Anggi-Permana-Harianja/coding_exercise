'''
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

    next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
    has_next(): returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

Time: O(N) we traverse the list
Space: O(1)
'''

class TwoDimIterator():
    def __init__(self, arr):
        self.arr = arr
        self.row = 0
        self.col = 0 

    def next(self) -> int:
        if not self.has_next():
            raise Exception("No more elements")
        element = self.arr[self.row][self.col]
        #move next col
        self.col += 1
        #if reach end col, next row
        if self.col >= len(self.arr[self.row]):
            self.col = 0
            self.row += 1

        return element
    
    def has_next(self):
        while self.row < len(self.arr) and self.col >= len(self.arr[self.row]):
            self.row += 1
            self.col = 0

        return self.row < len(self.arr)
