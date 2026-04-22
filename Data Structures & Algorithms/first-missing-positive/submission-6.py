class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        num = 0

        while num != max(nums) + 1:
            if num + 1 not in hashset:
                return num + 1
            else:
                num += 1
        
        return 1
