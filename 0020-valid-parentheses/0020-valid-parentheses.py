class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}

        for v in s:
            if v in dic.values():
                stack.append(v)
            elif v in dic.keys():
                if stack == [] or dic[v] != stack.pop():
                    return False
            else:
                return False
        
        return len(stack) == 0