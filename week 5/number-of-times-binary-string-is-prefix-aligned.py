class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        c = 0
        counter = 0
        idx = 0
        for i in range(len(flips)): 
            counter += flips[i] 
            idx += i + 1
            if counter == idx: 
                c += 1
        return c