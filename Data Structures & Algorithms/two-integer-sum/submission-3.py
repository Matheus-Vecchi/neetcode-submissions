class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            diferenca = target - nums[i]

            if diferenca in nums:
                if nums.index(diferenca) != i:
                    if nums.index(diferenca) < i:
                        return [nums.index(diferenca), i]
                    else:
                        return [i, nums.index(diferenca)]
