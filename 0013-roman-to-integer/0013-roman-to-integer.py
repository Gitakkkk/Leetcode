class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        
        romanVal = {'I': 1, 'IV': 4, 'IX': 9, 'V': 5, 'X': 10, 'XL': 40, 'XC': 90, 'L': 50, 'C': 100, 'CD': 400, 'CM': 900, 'D': 500, 'M': 1000}
        pointer = 0
        while pointer < len(s):
            if (pointer+1) != len(s) and s[pointer]+s[pointer+1] in romanVal:
                ans += romanVal[s[pointer]+s[pointer+1]]
                pointer += 2
            else:
                ans += romanVal[s[pointer]]
                pointer+=1

        return ans