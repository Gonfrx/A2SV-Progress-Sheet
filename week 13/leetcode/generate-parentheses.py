class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = [] 
        ret = []
        def backtrack(open, close):
            if open == 0 and close == 0: 
                ret.append("".join(ans))
                return 
            
            if open > 0: 
               ans.append('(')
               backtrack(open-1, close)
               ans.pop()
            if close > open:
                ans.append(')')
                backtrack(open, close-1)
                ans.pop()

        backtrack(n, n) 
        return ret