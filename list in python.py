a = [1, 2, 3, 4, 5]
#    0  1  2  3  4
#   -5 -4 -3 -2 -1
b = [1, 2, 3, 4, 5]
#    0  1  2  3  4
#   -5 -4 -3 -2 -1
print(a)
print(type(a))
# changing a value using list or array
a[0] = 100
a[3] = 30
print("a", a)
# printing a particular number
print("b", b[3], b[4])
# printing a number reverse we use minus symbol
print("b", b[-1], b[-2])
# printing a sequence of number
print("b", b[0:2])
print("b", b[-4:-1])
print("b", b[:3])
print("b", b[:-3])
print("b", b[2:])
# finding a list type using a type function
print("============")
print("============")
l = ["hi", 2.3, True, 1]
print(type(l))
print(type(l[0]))
print(type(l[1]))
print(type(l[2]))
print(type(l[3]))
# nested list
print("================")
n = [1, "ram", 6.6, False, [1, 2, 3, 4]]
print(n[4][3])
