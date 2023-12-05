class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        counter = 0
        if destination < start:
            temp = start
            start = destination 
            destination = temp
        for i in range(len(distance)):
            if i == destination:
                break
            if i >= start:
                counter += distance[i]
        x = sum(distance) - counter
        return min(x, counter)

            

        