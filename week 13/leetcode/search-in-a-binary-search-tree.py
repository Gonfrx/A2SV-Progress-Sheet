class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if val>root.val:
            return self.searchBST(root.right,val)
        elif val<root.val:
            return self.searchBST(root.left,val)
        return root       
        