class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.add(i + 1, nums[i])
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i
    def update(self, index, val):
        change = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, change)
    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total
    def sumRange(self, left, right):
        return self.sum(right + 1) - self.sum(left)
        """
        :type nums: List[int]
        """
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)