class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arrless = []
        arrequal = []
        arrgreater = []
        for val in nums:
            if val < pivot:
                arrless.append(val)
            elif val == pivot:
                arrequal.append(val)
            else:
                arrgreater.append(val) 
        return arrless + arrequal + arrgreater 