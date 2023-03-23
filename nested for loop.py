for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print(" ")
print("===============================")
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print(" ")
print("===============================")
"""
acii value in char to numbers
A-Z  = 65-90
 a-z = 97-122"""
# printing a capital letters of alphabets
"""
A
B
C
.
.
.
.
. 
intha order la print aagum """
for i in range(65,91):
    print(chr(i))
print("===================================")
#printing a small letters of alphabets
for j in range(97,123):
    print(chr(j))
print("==================================")
# printing a line abcde....
for j in range(97,123):
    print(chr(j),end="")
print("")
print("====================================")
for i in range(65,91):
    print(chr(i),end="")
