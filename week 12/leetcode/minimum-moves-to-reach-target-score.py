class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        pos = []
        curr = 1
        count = 0
        tar = target 
        
        while(tar > 2  and maxDoubles > 0):
            tar = tar // 2
            pos.append(tar) 
            maxDoubles -= 1
        l = len(pos)-1

        if len(pos) == 0:
            return target - 1
        
        while(curr < target):
            if l > -1:
                if curr < pos[l]:
                    count += pos[l] - curr
                    curr = pos[l]
                    count += 1
                    curr *= 2
                else: 
                    count += 1
                    curr *= 2
                l -= 1
            else:
                count += target - curr
                break 
        
        return count