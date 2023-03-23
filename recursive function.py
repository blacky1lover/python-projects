"""
5*4
5*4*3
5*4*3*2
5*4*3*2*1
"""
def factorial(x):
    if x==1:
        return 0
    else:
        return x*factorial(x-1)
print("factorial",factorial(5))