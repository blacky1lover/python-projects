# Variable page no : 3 start -end in 5
# Example program
a=5
b=5
c=a+b
print("answer is  ",c)
print(id(a))
print(id(b))
print(id(c))
print(type(a))
print(type(a))
print(type(b))
print(type(c))
#  showing a python keywords in python
# 'False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class' = KEYWORD
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda' = KEYWORD
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] = KEYWORD
# page no 6,7,8,9

import keyword
print(keyword.kwlist)

# input() statement page no : 10,11
# ipdi namma kuduthaal answer add aagathu only join panni kudukkum
a=input("enter a value : ")
b=input("enter a value : ")
print(a+b)
# namakku add or vera ethavathu pannanum na enna data type kudukuromo atha frot la podanum
# eg :  int kudukanum
a=int(input("enter a value ; "))
b=int(input("enter a value ; "))
c=a+b
print(a+b) # or
print("answer is the ",c)
# eg :  float kudukanum
a=float(input("enter a value ; "))
b=float(input("enter a value ; "))
c=a+b
print(a+b) # or
print("answer is the ",c)
# single line program PAGE NO : 12,13
# eg : line by line
n1,n2,n3=input("Enter a names : ").split(',')
print("Name1",n1)
print("Name2",n2)
print("Name3",n3)
#Multi-line and join function and list
# page no : 14,15,16,17,18,19,20,21
para=["25","30","40"]
print(",".join(para))# "," double quote kulla ethu pottalum antha symbol centre la pottu varum
# next program
para=[]
print("Enter a para :")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)

output = "\n".join(para)
print(output)
# 1.13.20 seconds in this folder finished next
# topic name is ==tutor2 python