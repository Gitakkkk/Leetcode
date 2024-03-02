class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        pointerS = 0
        lenS = 0

        for i in range(len(t)):
            if t[i] == s[pointerS]:
                pointerS += 1
                lenS += 1
            if lenS == len(s):
                return True
        
        return False