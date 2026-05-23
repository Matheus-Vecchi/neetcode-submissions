class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for i in nums:
            if i not in hashset:
                hashset.add(i)                
            else:
                return i
        
