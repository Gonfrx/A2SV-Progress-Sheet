class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        
        i = j = 0
        mid = -1
        if len(mat) % 2 != 0:
            mid = (len(mat) -1 )// 2
        m = 0
        curr = mx = 0
        while i < len(mat):
            curr += mat[i][j]
            i += 1
            j += 1
        i = 0
        j = len(mat[0]) - 1
        while i < len(mat):
           
            if i == mid: 
                i += 1
                j -= 1
                continue
            curr += mat[i][j]
            i += 1
            j -= 1
        
        return curr
        