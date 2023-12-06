class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        ini = capacity
        for i in range(len(plants)):
            if(capacity - plants[i] < 0):
                steps += (2 * (i+1)) - 1 
                capacity = ini - plants[i]
            else:
                steps += 1
                capacity -= plants[i]
        return steps 
            