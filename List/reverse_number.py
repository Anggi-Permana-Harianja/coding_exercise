#Link: https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/

def reverse_number(num: int) -> int:
    rem = 0
    
    while num:
        mod_ = num % 10
        rem = rem * 10 + mod_
        num = num // 10
        
    return rem

import unittest 
class TestProgram(unittest.TestCase):
    def test_program1(self):
        num = 1234
        
        result = 4321
        
        self.assertEqual(reverse_number(num), result)
        
    def test_program2(self):
        num = 123456789
        
        result = 987654321
        
        self.assertEqual(reverse_number(num), result)
        

if __name__ == '__main__':
    unittest.main()