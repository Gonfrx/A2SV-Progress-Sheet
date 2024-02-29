from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort costs based on the difference between costs of two cities
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs)
        min_cost = 0
        
        # Send the first n/2 people to city A and the rest to city B
        for i in range(n // 2):
            min_cost += costs[i][0]  # Add cost for city A
        
        for i in range(n // 2, n):
            min_cost += costs[i][1]  # Add cost for city B
        
        return min_cost
