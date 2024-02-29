class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root: return []
        q.append(root)
        if not root.left and not root.right:
            return [[root.val]]
        counter = 1
        curr = 0
        flag = False
        nums = []
        while q:
            temp = []
            for i in range(counter): 
                if q[0].left:
                    q.append(q[0].left)
                    curr += 1
                if q[0].right:
                    q.append(q[0].right)
                    curr += 1    
                temp.append(q[0].val)
                q.popleft()
            counter = curr
            curr = 0
            if flag == False:
                flag = True
            else:
                temp.reverse()    
                flag = False
            nums.append(temp)
            
            
        return nums
        