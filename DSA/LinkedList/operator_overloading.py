class height:
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch
    def __lt__(self,other):
        return self.feet<other.feet
x=height(10,4)
y=height(9,3)
print(y==x)