"""
Check whether given str of bracket is well balance

Time: O(N)
Space: O(N)
"""

def well_balance(brackets: str) -> bool:
    # set the pairs
    dict_ = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    brackets = list(brackets) # convert str into list

    for bracket in brackets:
        # check if it is opening or closing bracket
        if bracket not in dict_.keys():
            stack.append(bracket)
        # check if stack is empty or not
        # check if bracket is pair of the closing bracket
        elif not stack or dict_[bracket] != stack.pop():
            return False

    # check if stack is not empty means not balance
    if stack:
        return False

    return True

import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        brackets = "()()"

        self.assertEqual(well_balance(brackets), True)

    def test_case2(self):
        brackets = "[([])"

        self.assertEqual(well_balance(brackets), False)

    def test_case(self):
        brackets = "(((("

        self.assertEqual(well_balance(brackets), False)

if __name__ == "__main__":
    unittest.main()
