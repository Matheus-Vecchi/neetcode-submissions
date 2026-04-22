class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = [1] * len(nums)

        product_l = 1
        for i in range(0, len(nums)):
            if i == 0:
                left[0] = 1
            else:
                product_l *= nums[i - 1]
                left[i] = product_l
        
        product_r = 1
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right[-1] = 1
            else:
                product_r *= nums[j + 1]
                right[j] = product_r
        
        for t in range(0, len(nums)):
            ans[t] = right[t] * left[t]

        return ans
