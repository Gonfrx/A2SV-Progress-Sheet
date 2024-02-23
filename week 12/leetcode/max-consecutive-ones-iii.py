class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = maxLen = numZeros = 0
        while right < len(nums):
            if nums[right] == 0:
                numZeros += 1
            while numZeros > k:
                if nums[left] == 0: numZeros-= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen 