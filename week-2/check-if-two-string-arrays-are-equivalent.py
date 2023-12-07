class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        for val in word1:
            temp = str1 + val
            str1 = temp
        for val in word2:
            temp = str2 + val
            str2 = temp
        if str1 != str2:
            return False
        return True