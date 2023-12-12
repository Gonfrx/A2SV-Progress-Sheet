class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
            arr = []
            arr1 = []
            for val in nums:
                if val < 0:
                    arr.append(val)
                else:
                    arr1.append(val)
            ans = []
            i = 0
            j = 0
            while i < len(arr1):
                ans.append(arr1[i])
                ans.append(arr[j])
                i+=1
                j+=1 
            return ans
        