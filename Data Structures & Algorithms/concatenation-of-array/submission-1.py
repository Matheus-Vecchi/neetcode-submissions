class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        ans = [0] * n

        for i in range(n):
            pos = i % len(nums)
            ans[i] = nums[pos]
        
        return ans