'''
Fibonacci using DP

Time: O(n)
Space: O(n)
'''

def fibonacci(n: int) -> list:
    if n <= 1:
        return n
    else:
        fib_values = [0, 1]
        for i in range(2, n + 1):
            fib_values.append(fib_values[i - 1] + fib_values[i - 2])

    return fib_values

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        n = 5

        result = [0, 1, 1, 2, 3, 5]

        return self.assertEqual(fibonacci(n), result)
    
    def test_program2(self):
        n = 10

        result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        return self.assertEqual(fibonacci(n), result)
    
if __name__ == '__main__':
    unittest.main()
