class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        acc = 0

        for i in nums:
            acc += i
            self.prefix.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            range_sum = self.prefix[right] - self.prefix[left - 1]
        else:
            range_sum = self.prefix[right]

        return range_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)