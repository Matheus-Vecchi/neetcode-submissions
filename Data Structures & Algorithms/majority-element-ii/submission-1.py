class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        ans = []

        for key, value in hashmap.items():
            if value > len(nums) // 3:
                ans.append(key)
        
        return ans