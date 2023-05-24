"""
Given a number, generate possibilities of bracket

Example: 
- n = 1 -> ()
- n = 2 -> (()), ()()
- n = 3 -> ((())), (()()), (())(), ()(()), ()()()
"""

def generate_parentheses(n: int) -> list[str]:
    result = []
    left = right = n
    backtrack(left, right, "", result)

    return result

def backtrack(left: int, right: int, current: str, result: list[str]) -> list[str]:
    # base exit / exit case
    if left == 0 and right == 0:
        result.append(current)

        return 
    
    # try add left parantheses
    if left > 0:
        backtrack(left - 1, right, current + "(", result)
    
    # try add right parentheses
    if right > left:
        backtrack(left, right - 1, current + ")", result)


import unittest

class TestCases(unittest.TestCase):
    def test_case1(self):
        n = 2

        result = ["(())", "()()"]

        self.assertEqual(generate_parentheses(n), result)

    def test_case2(self):
        n = 3

        result = ['((()))', '(()())', '(())()', '()(())', '()()()']

        self.assertEqual(generate_parentheses(n), result)

if __name__ == "__main__":
    unittest.main()
