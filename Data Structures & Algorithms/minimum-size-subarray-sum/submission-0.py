class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_length = len(nums) + 1
        accumulator = 0

        for r in range(len(nums)):
            accumulator += nums[r]

            while accumulator >= target:
                min_length = min(min_length, r - l + 1)
                accumulator -= nums[l]
                l += 1
        
        if min_length == len(nums) + 1:
            return 0
        else:
            return min_length
