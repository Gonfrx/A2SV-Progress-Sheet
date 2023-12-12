class Solution:
    def totalMoney(self, n: int) -> int:
        sm = 0
        counter = 1
        count = 1
        for i in range(n):
            if counter - count >= 7:
                count += 1
                counter = count 
            sm += counter
            print(counter, sm)
            counter += 1
        return sm
