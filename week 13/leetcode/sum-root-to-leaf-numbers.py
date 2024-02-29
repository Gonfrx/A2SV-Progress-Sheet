class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        arr = []
        s = ""

        def preorder(root, s):
            if not root:
                return 0
            if not root.left and not root.right: 
                s += str(root.val)
                arr.append(int(s))
            elif root:
                s += str(root.val)
            preorder(root.left, s)
            preorder(root.right, s)
        
        preorder(root, s)
        return sum(arr)