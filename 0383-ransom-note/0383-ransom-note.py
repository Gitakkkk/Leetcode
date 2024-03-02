class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = dict()

        for v in magazine:
            if v not in magazineMap:
                magazineMap[v] = 1
            else:
                magazineMap[v] += 1
        
        for v in ransomNote:
            if v in magazineMap:
                if magazineMap[v] is 0: return False
                magazineMap[v] -= 1
            else: return False

        return True
            