class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            while nums[l] == nums[l + 1]:
                nums.pop(l)
            l += 1
            r = len(nums) - 1

            while nums[r] == nums[r - 1]:
                nums.pop()
                r -= 1
        
        return len(nums)
