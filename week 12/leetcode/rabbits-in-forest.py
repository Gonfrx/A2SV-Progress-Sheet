class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mx = max(answers)
        nums = [0] * (mx + 1)
        count = 0
        for i in range(len(answers)):
            nums[answers[i]] += 1

        for i in range(len(nums)):
    
            if nums[i] > i + 1:
                count += nums[i] + (i+1 - (nums[i] % (i+1))) 
                if nums[i] % (i+1) == 0:
                    count -= i+1
            else:
                if nums[i] > 0:
                    count += i + 1 
        return count
        #

