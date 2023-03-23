#print anything
print("hi")
# adding or subtraction or multiplicatio or math function
a=1
b=2
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)
#string and arrays are same in python
a="hi"
print(a)
#print the array index number and get the value or words
a="killer killer"
print(a[4:9])
# Length of the word
d="joker"
print(len(d))
# strip is a front of the waste of the space
"""
strip vanthu oru sring mattum irunthuchuna athukku munnadi or pinnadi space irunthuchunaal atha mattum count pannathu
but, space vittu innoru string irunthuchu naal appo antha space ithaium serthu eduthukkum ok vaa  
"""
k="     jhbj"
print(k.strip())
# upper is all change the capital letters
a="jhghg"
print(a.upper())
#lower is all change the small letters
a="GGJHHGVKH"
print(a.lower())
# Replace a word to mistake okay
a="killer"
print(a.replace("er","ing"))
# split a word and minus a word or letter or numbers
a="joker"
print(a.split("jo"))
# slicing is a negative of using a accesing a value of index number
a="killer"
print(a[-1:-4])
# in is using to find a word is have means is TRUE not have means FALSE
# TRUE in
a="fisher"
print("is" in a)
#FALSE in
a="hacker"
print("li"in a)
# Adding a variable also in the python
a= "hi"
b= "bye"
print(a+b)
# Boolean operators
print(4>4)
#OPERATORS IN PYTHON
# ARITHMETIC OPERATORS [+,-,*,/,%,**,//]
a=10
b=10
print(a+b)  # add a number
print(a-b) # minus a number
print(a*b) # multiplication a number
print(a/b) # divide a number
print(a%b) # modulus a number
print(a**b) # power of the number or square of the number
print(a//b) # floor division or modulus a number
# Assignment Operators[=,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=.
a=5
print(a)
# +=
a=5
a+=5
print(a)
# -=
a=5
a-=5
print(a)
# *=
a=5
a*=5
print(a)
# /=
a=5
a/=5
print(a)
# %
a=5
a%=5
print(a)
# //=
a=5
a//=5
print(a)
# **=
a=5
a**=5
print(a)
# &=
a=5
a&=5
print(a)
#|=
a=5
a|=5
print("=================",a)
# ^=
a=5
a^=5
print(a)
# >>=
a=5
a>>=5
print(a)
#<<=
a=5
a<<=5
print(a)
# CASTING IS A TO CONVERT THE VALUE
a=float(10)
b=int(20.0)
print(a,b)
#TYPE
f=10.877
m=20
print(type(f))
print(type(m))
# LIST is using a single variable annd store many elements
heroes=["superman","iron man","hulk","spiderman"]
print(heroes[3])
# SORT
n1=[5,55,99,1,4,8,9]
n1.sort(reverse=True)
print(n1)
#TUPLES using a same as the LIST but not changing anything and not add anything ,we using the brackets in tuples is ()
hi4=("kill","joke","comedy")
print(hi4)
#SET is a changing a unorder set ,we using a {} calibration brackets
hi5={'5','4','7'}
print(hi5)
# Dictionary is a store a many elements store in a single variable
hi6={
    "name": "lai",
    "age": "90",
    "aim":"CEO"

}
hi6["aim"]="hacker"
print(hi6)
print(hi6.get("aim"))
# IF,ELSE,ELIF
age = 18
if age >18:
    print("you can vote")
elif age == 18:
    print("you can apply for vote")
else :
    print("you can't vote")
#AND , OR ( or is working which one is correct is run Condition)
a,b=10,30
if a==10 and b==40:
    print("correct")
else:
    print("incorrect")
#OR ( or is working which one is correct is run Condition)
a,b=10,30
if a==10 or b==30:
    print("correct")
else:
    print("incorrect")
# Nested if
a,b=10,30
if a==10 or b==30:
    print("correct")
    if b==30:
        print("hello")
else:
    print("incorrect")
# Functions is storing or copy a full code
def addition():
    a=23
    b=35
    print(a+b)
addition() # Function calling
addition()
# we want to add a  number to choose
def addit(a, b):
    print(a+b)
addit(10, 13)
addit(30,40)
def hello(name):
    print("kill,"+ name)
hello("joker")
# return using
def hi():
    return 100
print(hi())
#adding or subtraction function on value
def king(d):
    return d+100
print(king(5))
# LOOP (FOR ,....)
name="Rithesh"
for n1 in name:
    print(n1)
# LINE BY LINE A ITEMS USING FOR
fruits={"apple","grape","banana","lemon"}
for n2 in fruits:
    print(n2)
# apply in spot loop using for
for i in "hi,welcome to our world":
    print(i)
# FINDING A  LETTERS IN LOOP USING FOR

for i in "hi,welcome to our world":
      if i == "t":
        print("t is present")
      else:
        print("t is not have ")
# BREAK is using to stop a loop
for i in "hi,welcome to our world":
      if i == "t":
        print("t is present")
        break
      else:
        print("t is not have ")
# continue is using for going to starting loop
for i in "hi,welcome to our world":
      if i == "t":
            continue
        #print("t is present")
      else:
        print("t is not have ")
#range is print a front of number
for n4 in range(10):
    print(n4)
#range is difference between a we given a number
for n5 in range(10,20,5):
    print(n5)
#While loop also same but little bit difference
i=1
while i<10:
    print(i)
    i+=1
# While loop using a else
i=1
while i<10:
    print((i))
    i+=1
else:
    print("over")
#lambda function is adding or sumbtraction method is very simple and special member function
n8=lambda num: num +20
print(n8(10))
# input() method is what we want to like to print
name =input()
print(name) # ithu oru simple input
# konjam advance input
name =input("what is your name")
print(name+" is my name")
# innum konjam advance ,namma oru number ah add or anything to do athukku atha namma casting
# (or) data type ah change pannanum ? why means input eppaiume ella thaiume
# STRINGS ah tha irukkum atha namma data type ah change pannanum
a=input( " a value")
b=input("b value")
print(a+b) # namma ipdi kuduthaal ithu add aagathu pakkathula poi join aaagum ok vaa
# ippo namma add panna porom using a user input
a=int(input( " a value"))
b=int(input("b value"))
print(a+b) # ithu maari panna entha operators vena podalam







