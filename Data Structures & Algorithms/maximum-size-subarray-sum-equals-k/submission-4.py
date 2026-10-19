class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = {0: -1}
        ans = 0
        acc = 0

        for i in range(len(nums)):
            acc += nums[i]
            if acc - k in prefix:
                ans = max(ans, i - (prefix[acc - k] +1)+1)
            
            if acc in prefix:
                prefix[acc] = min(i, prefix[acc])
            else:
                prefix[acc] = i
        
        return ans
            

            
