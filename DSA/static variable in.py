class dog:
    global x
    x=5
    def __init__(self,y):
        self.y=y
var=dog(10)
dog.x=20
var2=dog(30)
print(dog.x)