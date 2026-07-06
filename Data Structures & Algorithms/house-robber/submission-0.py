class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0

        for i in range(len(nums)):
            curr = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = curr
        
        return max(prev, prev2)

            