import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        temp = 0

        for v in s:
            if v == ' ':
                temp = 0
            else:
                temp += 1
                ans = temp
        
        return ans