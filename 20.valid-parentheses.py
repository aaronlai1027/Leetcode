class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif not stack:
                return False
            else:
                if dict[char] != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False
