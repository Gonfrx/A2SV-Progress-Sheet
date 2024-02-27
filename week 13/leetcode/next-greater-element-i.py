class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        m = len(nums1)
        v2 = [-1] * m
        s = []
        mp = {}

        for i in range(n):
            while s and s[-1] < nums2[i]:
                mp[s.pop()] = nums2[i]
            s.append(nums2[i])

        for i in range(m):
            if nums1[i] in mp:
                v2[i] = mp[nums1[i]]

        return v2
 