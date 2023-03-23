"""
adding a tuple two varable using
count a tuple elements inside come using count function
nested tuple
using * this symbol of multiplication
"""
a=("hi","bro","how"," are","you")
b=("i","am","fine"",","bro")
c=a+b
print(c)
print("============")
print("============")
a=(1,6,3,4,5)
b=(2,7,8,9)
c=a+b
print(c)
print("============")
print("============")
c=(10,20,50,10,20,10,60,70,10)
d=(200,10,300,400,500,10)
e=c+d
print(e.count(10))
print("============")
print("============")
c=(10,20,50,10,20,10,60,70,10,(200,10,300,400,500,10))
print(c[9][1])
print("============")
print("============")
c=(10,20,50,10,20,10,60,70,10)
d=(200,10,300,400,500,10)
e=(c,d)
print(e)
print(e[0])
print(e[1])
print(e[0][2])
print(e[1][3])
print("============")
print("============")
a=("natarajan , ".title())*5
b=(5,)*2
print(b)
print(a)
