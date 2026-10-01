class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        ans = []
        count = 0

        for key in freq.keys():
            bucket[freq[key]].append(key)
        
        for freq in range(len(bucket)-1, -1, -1):
            for num in bucket[freq]:
                ans.append(num)
                count += 1
                if count == k:
                    return ans
                    
