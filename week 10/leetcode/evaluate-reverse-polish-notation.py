class Solution:
    def evalRPN(self, nums: List[str]) -> int:
        stk = deque() 
        curr = temp = 0
        for i in range(len(nums)):    
            if nums[i] == "+":
               x = (stk.pop())
               y = (stk.pop())
               stk.append(y+x) 
            elif nums[i] == "-":
                x = (stk.pop())
                y = (stk.pop())
                stk.append(y-x)
            elif nums[i] == "*":
                x = (stk.pop())
                y = (stk.pop())
                stk.append(y*x)
            elif nums[i] == "/":
                x = (stk.pop())
                y = (stk.pop())
                if y / x < 0:
                    stk.append(ceil(y/x))
                else:
                    stk.append(y//x)
            else:
                stk.append(int(nums[i]))
        
        
        return stk[-1]
            
