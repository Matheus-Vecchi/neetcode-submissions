class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for i in nums:
            hashset.add(i)
        
        seq = 0
        max_seq = 0

        for j in nums:
            seq = 1
            if j + 1 in hashset:
                while j + seq in hashset:
                    seq += 1
            if seq > max_seq:
                max_seq = seq

        return max_seq