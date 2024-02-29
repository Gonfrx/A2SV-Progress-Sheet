class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def inorder(root, mn, mx):
            if not root:
                return True
            if root.val >= mx or root.val <= mn:
                return False
            left = inorder(root.left, min(mn, root.val) , min(mx, root.val))
            right = inorder(root.right, max(mn, root.val), max(mx, root.val))
            return left and right

        return inorder(root, (-inf), (inf))
        