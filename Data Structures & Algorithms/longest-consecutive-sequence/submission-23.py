class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setmap = set(nums)

        freq = 1
        max_freq = 0

        for i in setmap:
            if i - 1 not in setmap:
                while i + freq in setmap:
                    freq += 1
                
                if freq > max_freq:
                    max_freq = freq
                freq = 1
        
        return max_freq
                
