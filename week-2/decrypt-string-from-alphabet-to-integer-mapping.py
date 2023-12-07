class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {}
        char = 'a'

        for i in range(1, 10):
            dic[str(i)] = char
            char = chr(ord(char) + 1)

        for i in range(10, 27):
            dic[str(i)] = char
            char = chr(ord(char) + 1)
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                temp = s[i - 2: i]
                i -= 3
            else:
                temp = s[i]
                i -= 1
            ans = dic[temp] + ans
        return ans
