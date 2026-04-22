class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "+":
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif i == "D":
                res = stack[-1] * 2
                stack.append(res)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        return sum(stack)