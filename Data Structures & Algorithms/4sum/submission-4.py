class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        
        i = 0
        j = 1
        l = 2
        r = len(nums) - 1

        ans = []

        while i <= len(nums) - 4:
            while j <= len(nums) - 3:
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
                j += 1
                while j <= len(nums) - 3 and nums[j] == nums[j - 1]:
                    j += 1
                l = j + 1
                r = len(nums) - 1
            i += 1
            while i <= len(nums) - 4 and nums[i] == nums[i - 1]:
                i += 1
            j = i + 1
            l = j + 1
            r = len(nums) - 1

        return ans