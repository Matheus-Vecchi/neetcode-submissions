class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set()

        for i in nums:
            if i not in no_dups:
                no_dups.add(i)
            else:
                return True
        
        return False