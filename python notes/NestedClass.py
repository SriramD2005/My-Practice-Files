class outer:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    x = 5
    class inner:
        def __init__(innerself, p, q):
            innerself.p = p
            innerself.q = q
        def printOut(innerself):
            print('x',outer.x)
            o = outer(innerself.p, innerself.q)
            print('a', o.a)
x = outer.inner(2,3)
x.printOut()
