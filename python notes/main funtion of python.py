def maintest():
    print("this function is different and the whole program is running in the main fucntion \3\+\5")
    print(__name__)
class x:
    def notmain():
        maintest()
x.notmain()