class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        mx = [0]

        def inorder(root, mx, low, high):
            if not root:
                return mx
            if root.val >= low and root.val <= high:
                mx[-1] += root.val 
            inorder(root.left, mx, low, high)
            inorder(root.right, mx, low, high)
        
        inorder(root, mx, low, high)
        return mx[-1]
        
            
        