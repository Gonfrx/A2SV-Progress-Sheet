class Solution:
    def average(self, salary: List[int]) -> float:
       mn = min(salary)
       mx = max(salary)
       sm = sum(salary)
       return (sm - mx - mn) /( len(salary)-2)