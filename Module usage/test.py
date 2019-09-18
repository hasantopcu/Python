import mymodule as md


class calculateCube(md.calculateSquare):
    def __init__(self,n1,n2,n3):
        super().__init__(n1,n2)
        self.n3=n3

    def calculateCb(self):
        return super().calculateSqr()*self.n3

    
x = md.calculateSquare(5,5)
a = x.calculateSqr()
print(a)

y = calculateCube(5,5,5)
b = y.calculateCb()
print(b)
