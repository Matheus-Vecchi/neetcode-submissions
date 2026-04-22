class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        ans = [1] * len(nums)

        while i <= len(nums) - 1:
            acumulador = 1
            for pos, j in enumerate(nums):
                if pos != i:
                    acumulador *= j
            ans[i] = acumulador
            i += 1
        
        return ans
        



