class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        i = 0
        l = 1
        r = len(nums) - 1

        ans = []

        while i <= len(nums) - 3:
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l <= len(nums) - 2 and nums[l] == nums[l - 1]:
                        l += 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i <= len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
            l = i + 1
            r = len(nums) - 1

        return ans
