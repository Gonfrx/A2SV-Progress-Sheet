class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        sm = 0 
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sm += nums[i]
        for i in range(len(queries)):
            val = nums[queries[i][1]]
            if val % 2 == 0:
                if (val + queries[i][0]) % 2 != 0:
                    sm -= val
                else:
                    sm += queries[i][0]
            else:
                if (val + queries[i][0]) % 2 == 0:
                    sm += val + queries[i][0]
            arr.append(sm)
            nums[queries[i][1]] += queries[i][0]
        return arr
        








        