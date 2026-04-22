class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = [1] * len(nums)

        produto = 1

        for pos, i in enumerate(nums):
            if pos == 0:
                left[0] = 1
            else:
                produto = produto * nums[pos - 1]
                left[pos] = produto
        
        produto_r = 1
        
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right[j] = 1
            else:
                produto_r = produto_r * nums[j + 1]
                right[j] = produto_r
        
        for p in range(0, len(ans)):
            ans[p] = left[p] * right[p]
        
        return ans

