class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #project 0 - question 1 
        mp = defaultdict(int) 


        def preorder(root):
            if not root:
                return 
            mp[root.val] += 1
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)

        mx = 0
        for key, val in mp.items():
            if val > mx: mx = val
        
        ans = []
        for key, val in mp.items():
            if val == mx: ans.append(key)
         
        return ans 


