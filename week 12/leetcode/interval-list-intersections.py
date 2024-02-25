class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #the maximum start and the minimum end fi they are overlapping 
        #and to find if this overlapping exists what we can do is check 
        # 1. if the start of firstlist is less than the end of second list
        # 2. if the start of secondlist is less than the end of the first list 
        # now we are sure that the ranges will be intersecting 

        ans = []
        l = 0
        r = 0
        while l < len(firstList) and r < len(secondList): 
            first_start, first_end = firstList[l]
            second_start, second_end = secondList[r]

            if first_start <= second_end and second_start <= first_end:
                ans.append([max(first_start, second_start), min(first_end, second_end)])
            
            if first_end <= second_end: 
                l += 1
            else: r += 1

        return ans