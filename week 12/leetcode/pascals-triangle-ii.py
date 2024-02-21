class Solution:
    def getRow(self, row: int) -> List[int]:
        c = 0
        a = [1]
        def ans(counter,arr):
            if counter == row: return arr
            curr = [1]
            for i in range(len(arr)-1):
                curr.append(arr[i]+arr[i+1])
            curr.append(1)
            arr = curr
            counter += 1
            return ans(counter, arr)
        return ans(c,a)

        