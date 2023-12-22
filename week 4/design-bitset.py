class Bitset:
   
    def __init__(self, size: int): 
        self.arr = []
        self.flipp = []
        self.counter = 0
        for i in range(size):
            self.arr.append(0)
            self.flipp.append(1)
    def fix(self, idx: int) -> None:
        if self.arr[idx] != 1: 
            self.arr[idx] = 1
            self.flipp[idx] = 0
            self.counter += 1
            print(self.counter)
    def unfix(self, idx: int) -> None:
        if self.arr[idx] != 0:
            self.arr[idx] = 0
            self.flipp[idx] = 1
            self.counter -= 1
            print(self.counter)
    def flip(self) -> None:
        temp = []
        temp = self.arr
        self.arr = self.flipp
        self.flipp = temp
        self.counter = len(self.arr) - self.counter
    def all(self) -> bool:
        if self.counter == len(self.arr): 
            return True
        return False
    def one(self) -> bool:
        if  self.counter > 0:
            return True
        return False
    def count(self) -> int:
        return self.counter    
    def toString(self) -> str:
        s = ""
        for val in self.arr: 
            s += str(val) 
        return s


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flipp()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.counter()
# param_7 = obj.toString()