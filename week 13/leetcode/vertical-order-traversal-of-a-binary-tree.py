class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        mp = defaultdict(int)

        def preorder(root, col, row):
            if not root:
                return 
            if col not in mp: 
                mp[col] = [[row, root.val]]
            else:
                mp[col].append([row, root.val])
            preorder(root.left, col-1, row+1)
            preorder(root.right, col+1, row+1)
        
        preorder(root, 0, 0)
        
        sorted_mp = dict(sorted(mp.items()))
        ans = []
        for key, col in sorted_mp.items():
            col.sort(key=lambda x: (x[0], x[1]))
            temp = []
            for val1, val2 in col: 
                temp.append(val2)
            ans.append(temp)


        return ans
        