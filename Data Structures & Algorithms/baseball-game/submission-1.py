class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        
        for pos, i in enumerate(operations):
            if i == "+":
                previous_sum = int(ans[-1]) + int(ans[-2])
                ans.append(previous_sum)
            elif i == "D":
                previous_double = int(ans[-1]) * 2
                ans.append(previous_double)
            elif i == "C":
                ans.pop()
            else:
                ans.append(int(i))
        
        return sum(ans)