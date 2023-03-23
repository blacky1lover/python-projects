def hell():
    print("welcome to my darkside")
hell()
print("==================")
""" No return type without argument function in python
 argument apdina eg:
     def add() ithu kulla ethuvum kudukama potta athu no argument
"""
# No return type without argument function in python
def add():
    a=int(input("enter a number : ".title()))
    b = int(input("enter a number : ".title()))
    c=a+b
    print(c)
add()
# with argument
def sub(a,b):
    c=a-b
    print(c)
sub(int(input("enter the number")),int(input("enter the number")))