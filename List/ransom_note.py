'''
https://leetcode.com/problems/ransom-note/

Time: O(N)
Space: O(1) since alphabet is always 26
'''

from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    if len(ransom_note) > len(magazine):
        return False
    
    magazine_cnt = Counter(magazine)
    
    for char in ransom_note:
        if magazine_cnt[char] <= 0:
            return False
        magazine_cnt[char] -= 1
        
    return True

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        ransom_note = "aa"
        magazine = "ab"
        
        result = False
        
        self.assertEqual(can_construct(ransom_note, magazine), result)
        
    def test_program2(self):
        ransom_note = 'aa'
        magazine = 'aab'
        
        result = True
        
        self.assertEqual(can_construct(ransom_note, magazine), result)
        
if __name__ == '__main__':
    unittest.main()