class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product = []
        r_product = [1] * len(nums)
        ans = [1] * len(nums)
        acc_l = 1
        acc_r = 1

        for i in range(len(nums)):
            if i == 0:
                l_product.append(1)
            else:
                acc_l *= nums[i - 1]
                l_product.append(acc_l)
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                r_product[i] = 1
            else:
                acc_r *= nums[i + 1]
                r_product[i] = acc_r

        for i in range(len(ans)):
            ans[i] = l_product[i] * r_product[i]
        
        return ans
