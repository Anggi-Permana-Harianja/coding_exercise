#Link: https://www.algoexpert.io/questions/Product%20Sum

def product_sum(array, depth=1):
    curr_sum = 0
    for i in range(len(array)):
        if isinstance(array[i], list):
            curr_sum += product_sum(array[i], depth=depth+1)
        else:
            curr_sum += array[i]
            
    return curr_sum * depth


import unittest
class TestProgram(unittest.TestCase):
    def test_program(self):
        array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        
        result = 12 #calculated as 5 + 2 + [2 * (7 + 1)] + 3 + [2 * (6 + [3 * (-13 + 8) + 4])]
        
        self.assertEqual(product_sum(array, 1), result)
        
if __name__ == '__main__':
    unittest.main()