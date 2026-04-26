class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        ans = ""

        i = 0
        j = 0

        while i < len(path):
            if path[i] != "/":
                j = i
                while i < len(path) and path[i] != "/":
                    i += 1

                if path[j:i] == "..":
                    if stack:
                        stack.pop()
                elif path[j:i] == ".":
                    continue
                else:
                    stack.append(path[j:i])
            else:
                i += 1

        ans = ""

        for i in stack:
            ans += "/"
            ans += i

        if stack:
            return ans
        else:
            return "/"
