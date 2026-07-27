class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        acc = 0
        ans = 0

        for i in nums:
            acc += i
            diff = acc - k

            if diff in prefix:
                ans += prefix[diff]
            
            if acc in prefix:
                prefix[acc] += 1
            else:
                prefix[acc] = 1
        
        return ans


            