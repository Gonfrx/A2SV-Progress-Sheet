class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = []
        self.arr.append(0)
        self.arr.append(nums[0])
        for i in range(1, len(nums)):
            self.arr.append(self.arr[-1] + nums[i])
         

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)