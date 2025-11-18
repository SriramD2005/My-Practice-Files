#FORMATTING
str='temperature:{0:10.2f}'.format(30.2345)#10 specifies space for the value
print(str)                                 #.2f float with to numbers after point
str2='score in hexadecimal:{0:x} score in decimal:{1:d}'.format(int('a5',16),165)
print(str2)
#or you can use variables instead of integers to indicate the respective position
str2='score in hexadecimal:{a:x} score in decimal:{b:d}'.format(a=int('a5',16),b=165)
print(str2)
x=34
print('num:{x:d}'.format(x=x))
y=[1,2,3,4]
def iseve(x):
    return x%2==0
print(iseve(2))
z=list(filter(iseve,y))
print('z',z)
print(f"{2.345342:.2f}")