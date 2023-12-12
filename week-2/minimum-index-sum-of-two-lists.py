class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        mn = float("inf") 
        val = ""
        dec = {}
        ans = []
        for i in range(len(list1)):
            dec[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dec:
                if abs(dec[list2[i]] + i) < mn: 
                        ans.clear()
                        mn = abs(dec[list2[i]] + i) 
                        ans.append(list2[i])
                elif abs(dec[list2[i]] + i) == mn:
                        ans.append(list2[i])
        return ans