class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
     
        max_sum = 0
        #mp = defaultdict(int)
        #+inf , -inf
        # bool , mx, mn , sm 
        def valid(root): 
            nonlocal max_sum
            
            if not root: return True, 0, -inf, inf

            left, left_sm, left_mx, left_mn = valid(root.left) 
            right, right_sm, right_mx, right_mn = valid(root.right)

            if  left and right and left_mx < root.val < right_mn: 
                curr = left_sm + right_sm + root.val 
                max_sum = max(max_sum, curr)
                return True, curr, max(right_mx, root.val), min(left_mn, root.val)
            return False, 0, -inf, inf
                      

        valid(root)
        return max_sum
                