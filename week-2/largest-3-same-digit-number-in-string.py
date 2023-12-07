class Solution:
    def largestGoodInteger(self, num: str) -> str:
            counter = 1
            mx = 0 
            flag = False
            for i in range(len(num)-1):
                if num[i] == num[i+1]:
                    counter += 1
                else:
                    counter = 1 
                if counter == 3:
                    flag = True
                    mx = max(mx, ((int(num[i]) * 100 )+ (int(num[i]) * 10) +int(num[i])))
                    counter = 1     
            if flag == True and mx == 0:
                return "000"
            elif flag == False and mx == 0:
                return ""
            return str(mx)
