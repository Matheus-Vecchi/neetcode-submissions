class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if target < nums[mid]:
                high = mid - 1
                ans = mid
            elif target > nums[mid]:
                low = mid + 1
                ans = mid + 1
            else:
                return mid

        return low
