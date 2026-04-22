class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        hashset = set()

        l = 0

        for r in range(len(nums)):
            if nums[r] in hashset:
                return True
            if r - l == k:
                hashset.remove(nums[l])
                l += 1
            hashset.add(nums[r])
        
        return False

