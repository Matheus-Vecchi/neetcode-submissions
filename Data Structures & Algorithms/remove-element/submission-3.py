class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0

        while j < len(nums):
            while j < len(nums) and nums[j] != val:
                nums[i] = nums[j]
                j += 1
                i += 1
            j += 1
        
        return i