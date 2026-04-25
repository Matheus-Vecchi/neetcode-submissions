from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0

        dq = deque([])

        ans = []

        for r in range(len(nums)):
            while dq and nums[r] > dq[-1]:
                dq.pop()
            
            dq.append(nums[r])

            if r - l + 1 == k:
                ans.append(dq[0])

                if nums[l] == dq[0]:
                    dq.popleft()
                
                l += 1
        
        return ans