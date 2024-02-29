class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums  = []
        
        def inorder(root): 
            if not root: return None
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return nums[k-1]