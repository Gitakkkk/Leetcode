class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        minStr = min(strs, key=len)
        for i, v in enumerate(minStr):
            for other in strs:
                if other[i] != v:
                    return minStr[:i]
        
        return minStr
