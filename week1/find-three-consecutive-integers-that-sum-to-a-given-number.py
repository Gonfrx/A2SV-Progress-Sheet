class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            y = int(num / 3 - 1)
            return [y, y+1, y+2]
        return []