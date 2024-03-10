class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a, b = {}, s.split(' ')

        if len(pattern) != len(b): return False
        if len(set(pattern)) != len(set(b)): return False

        for i in range(len(b)):
            if b[i] not in a:
                a[b[i]] = pattern[i]
            elif a[b[i]] != pattern[i]:
                return False
        
        return True