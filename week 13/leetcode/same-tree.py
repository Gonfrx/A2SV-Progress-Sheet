class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = False

        def preorder(curr1, curr2): 
            if not curr1 and not curr2: 
                return True
            elif not curr1:
                return False
            elif not curr2:
                return False
            
            if curr1.val != curr2.val:
                return False
            
            left =  preorder(curr1.left, curr2.left)
            right = preorder(curr1.right, curr2.right)
            return left and right
        
        return preorder(p, q)