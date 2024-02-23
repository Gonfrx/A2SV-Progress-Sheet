class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        maxi = 0
        mini = 0
        j = 0
        first = s[j]
        n = len(s)
        for i in range(n):
            if mini < k:
                if s[i] in ['a', 'e', 'i', 'o', 'u']:
                    mini += 1
                    count += 1
                else:
                    mini += 1
            elif mini == k:
                maxi = max(count, maxi)
                first = s[j]
                if first in ['a', 'e', 'i', 'o', 'u']:
                    count -= 1
                if s[i] in ['a', 'e', 'i', 'o', 'u']:
                    count += 1
                j += 1
        maxi = max(count, maxi)
        return maxi
