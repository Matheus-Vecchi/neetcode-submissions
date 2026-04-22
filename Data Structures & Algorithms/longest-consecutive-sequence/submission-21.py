class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        hashset = set(nums)

        seq = 1
        max_seq = 1

        for i in nums:
            if i - 1 not in hashset:
                while i + seq in hashset:
                    seq += 1
                    if seq > max_seq:
                        max_seq = seq
                seq = 1
        return max_seq


