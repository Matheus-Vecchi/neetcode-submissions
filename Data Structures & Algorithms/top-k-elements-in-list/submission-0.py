class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        bucket = [[] for _ in range (0,len(nums) + 1)]

        for key, v in hashmap.items():
            bucket[v].append(key)
        
        ans = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans


            