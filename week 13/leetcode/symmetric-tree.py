class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #project 0 - question 3
        q = deque()
        q.append(root)
        counter = 1
        curr = 0
        while q:
            for i in range(counter):
                if q[0]: 
                    if q[0].left: 
                        curr += 1
                        q.append(q[0].left)
                    else:
                        curr += 1
                        q.append(None)
                    if q[0].right:
                        curr += 1
                        q.append(q[0].right)
                    else:
                        curr += 1
                        q.append(None)
                counter -= 1
                q.popleft()
            
            l , r = 0, len(q)-1

            while l < r: 
                
                if not q[l] and q[r] or not q[r] and q[l]: 
                    return False
                elif q[l] and q[r] and q[l].val != q[r].val:
                    return False
                l += 1
                r -= 1
            
            counter = curr
            curr = 0


        return True
        