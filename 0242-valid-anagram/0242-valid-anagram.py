class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        a = {}
        b = {}

        for v in s:
            if v in a:
                a[v] += 1
            else:
                a[v] = 1
        for v in t:
            if v in b:
                b[v] += 1
            else:
                b[v] = 1
        
        if a == b: return True
        return False