class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif len(stack) == 0:
                return False
            
            if char == ")":
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif char == "}":
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            
        if len(stack) > 0:
            return False
        else:
            return True
                