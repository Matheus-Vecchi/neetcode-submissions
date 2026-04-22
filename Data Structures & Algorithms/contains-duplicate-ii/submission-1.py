class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for pos, num in enumerate(nums):
            if num in hashmap and pos - hashmap[num] <= k:
                return True
            hashmap[num] = pos
        
        return False