class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            mx = max(candies)
            arr = []
            for val in candies:
                if val + extraCandies < mx:
                    arr.append(False)
                else:
                    arr.append(True)
            return arr