class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        char = ""
        num = 0
        
        for c in s:
            if c == "[":
                stack.append(char)
                stack.append(num)
                char = ""
                num = 0
            elif c == "]":
                t = stack.pop()
                char = stack.pop() + t*char
                
            elif c.isdigit():
               num = num*10 + int(c) 
            else:
                char += c
        return char
