class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        cycle_head = 0

        while cycle_head != slow:
            cycle_head = nums[cycle_head]
            slow = nums[slow]
        
        return cycle_head