class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        cur = 0
        
        for row in range(len(grid)-2):
            for col in range(1,len(grid[0])-1):
                upper_row = grid[row][col-1] + grid[row][col] + grid[row][col+1] 
                middle_col = grid[row+1][col] 
                left_row = grid[row+2][col-1] + grid[row+2][col] + grid[row+2][col+1] 
                curr_sum = upper_row + middle_col + left_row
                ans = max(ans,curr_sum)
                                                     
        return ans 
            