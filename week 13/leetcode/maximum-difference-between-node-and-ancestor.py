class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ret = mx = mn = 0
        mn = mx = root.val

        def preorder(root, mx, mn): 
            nonlocal ret    
            if not root:
                return 
        
            ret = max(ret, abs(mx - root.val), abs(mn - root.val)) 
            preorder(root.left, max(root.val, mx), min(root.val, mn))
            preorder(root.right, max(root.val, mx), min(root.val, mn))
        
        preorder(root, root.val, root.val)
        return ret