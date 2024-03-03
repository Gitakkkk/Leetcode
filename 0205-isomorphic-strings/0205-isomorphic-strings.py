class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sIdx = []
        tIdx = []

        for v in s:
            sIdx.append(s.index(v))
        for v in t:
            tIdx.append(t.index(v))
        
        if sIdx == tIdx: return True
        else: return False