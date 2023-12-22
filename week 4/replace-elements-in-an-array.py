class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for val in operations:
            if val[0] in dic:
                ind = dic[val[0]]
                del dic[val[0]]
                dic[val[1]] = ind
        arr = []
        for i in range(len(nums)):
            arr.append(0)
        for i in dic:
            arr[dic[i]] = i 
        print(dic)
        return arr
       

        