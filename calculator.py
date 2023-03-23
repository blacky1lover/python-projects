def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
print(""""select a metod
1.add
2.sub
3.mul
4.div
""")
choice=int(input(" Enter your method  "))
a=int(input("Enter a Number "))
b=int(input("Enter a Number "))
if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print("give the correct choice")