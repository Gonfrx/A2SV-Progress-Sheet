class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        use = sorted(fronts)
        mn = float(inf)
        s = set(fronts)
        for i in range(len(backs)):
            if backs[i] < mn:
                if backs[i] not in s: 
                    mn = backs[i]
        for i in range(len(use)):
            found = False
            skip = False
            x = 0
            for j in range(len(fronts)):
                if fronts[j] == use[i]:
                    if backs[j] != fronts[j]:
                            found = True
                            x = fronts[j]
                    else: 
                        skip = True
                        break 
            if found == True and skip == False:
                if x < mn: 
                    return x
        if mn != float(inf):
            return mn
        return 0

            
        