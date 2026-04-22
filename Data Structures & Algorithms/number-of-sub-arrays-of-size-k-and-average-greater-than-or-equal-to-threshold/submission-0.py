class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        accumulator = 0
        
        ans = 0

        l = 0

        for r in range(len(arr)):
            accumulator += arr[r]

            if r - l + 1 == k:
                if accumulator / k >= threshold:
                    ans += 1
                accumulator -= arr[l]
                l += 1
        
        return ans
