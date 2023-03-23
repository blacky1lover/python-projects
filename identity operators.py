"""
identity operator
 is
 is not
ithula address paarkum pothu ovoru variable kum vera vera address irukkum atha base panni tha
True illana False output varum
but
ulla irukura value or elements ah eduthukaathu
"""
# is apdina athuvum ithuvum same ah nu paakrom
# same ah irunthuchu na True nu varum
# not same ah irunthuchu na False nu varum
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(c is b)
# is not athuvum ithuvum not same ah irunthuchuna True nu varum
# is not athuvum ithuvum same ah irunthuchuna False nu varum
print("==================")
print(a is not c)
print(a is not b)
print("===================")
#ipdi panna ulla irukura value va or ulla irukura elements ah compare pannum
print(a==b)
# ulla irukura value  equal ah iruntha False
# not equal ah iruntha True ( value )
print(a!=b)
