class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        
        count = 0
        max_count = 0

        for i in nums:
            if i - 1 not in hashset:
                count = 1
                while i + count in hashset:
                    count += 1
                
            if count > max_count:
                max_count = count
        
        return max_count