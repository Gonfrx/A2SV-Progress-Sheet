class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        curr1 = root1
        curr2 = root2
        
        def merge(curr1,curr2):
            if not curr1 and not curr2:
                return None
            val1, val2 = 0, 0
            if curr1: val1 = curr1.val
            if curr2: val2 = curr2.val

            node = TreeNode(val1 + val2)
            if not curr1:
                node.left = merge(None, curr2.left)
                node.right = merge(None, curr2.right)
            elif not curr2: 
                node.left = merge(curr1.left, None)
                node.right = merge(curr1.right, None)
            else:
                node.left = merge(curr1.left, curr2.left)
                node.right = merge(curr1.right, curr2.right)
            return node
            

        return merge(root1, root2)