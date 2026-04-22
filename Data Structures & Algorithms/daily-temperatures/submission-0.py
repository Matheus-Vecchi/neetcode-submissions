class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j - i)
                    break
            if len(ans) - 1 != i:
                ans.append(0)
        
        return ans