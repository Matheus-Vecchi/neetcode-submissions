class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for pos, i in enumerate(nums):
            complement = target - i

            if complement in hashmap:
                return [hashmap[complement], pos]

            hashmap[i] = pos
