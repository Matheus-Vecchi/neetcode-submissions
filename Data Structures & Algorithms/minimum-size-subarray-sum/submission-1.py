class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        accumulator = 0
        ans = len(nums) + 1

        for r in range(len(nums)):
            accumulator += nums[r]

            while accumulator >= target:
                ans = min(r - l + 1, ans)
                accumulator -= nums[l]
                l += 1

        if ans == len(nums) + 1:
            return 0
        else:
            return ans