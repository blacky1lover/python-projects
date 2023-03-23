"""
copy = oru list la irukurathu innoru list ku copy pandrathu
clear = oru list kulla irukuratha clear pandrathu
count = we want to find a number or any words or any string or any other to find how many times come in list
index = we will find the index numbers using by index function
len = we will find the length of the value, the len function count only how many values or strings in the list not count a index number
max = find a maximum number or string using a max function
min = find a minimum number or string using a min function
pop = remove a particular index number
remove = remove a number or elements using a value
append = adding a elements in same list
extend = joining a list in same list
insert = this using for a adding a elements using insert not replace to help of index number
list = this convert a normal elements to list
range = to print a sequence of number
sort = this is using a elements to order a ascending order
sort(reverse=True) = this is use to order a descending order
sort(key=len) = this use to order a elements base on length
"""
a=[1,2,3,4]
b=a.copy()
print(b,"b is copy by using copy function")
print("================")
a.clear()
print(a,"a is clear by using clear function")
print("===================")
c=[67,76,0,67,5,3,9,0,67,43,0,5,67]
print(c.count(67),"this shows how many 67 in the list".title())
print(c.count(5),"this shows how many 5 in the list".title())
print(c.count(0),"this shows how many 0 i the list".title())
print("===========")
print("============")
n=[1,2,3,4,5,6]
print(n.index(4),"this is a index number of 4")
print("===============")
v=[1,2,34,5,6]
print(len(v))
print("===========")
v=[1,2,34,5,6]
print(max(v))
print("=============")
v=[1,2,34,5,6]
print(min(v))
print("=============")
v=[1,2,34,5,6]
v.pop(1)
print(v,"remove 1 index number")
print("===========")
b=[10,20,30,40,50]
b.remove(20)
print(b," remove 20 in b using remove function")
print("===========")
print("===========")

s=["vijaya"]
print(s)
s.append("natarajan")
print(s)
print("===========")
print("===========")
f=["annamalai","naveen kumar".title()]
print(f)
g=["rithesh".title()]
f.extend(g)
print(f)
print("===========")
print("===========")
m=["natarajan","vijaya","anna malai","naveen kumar"]
m.insert(4,"rithesh")
print(m)
print("===========")
print("===========")
d="hello nanba"
print(list(d))
print(list(range(8)))
print("===========")
print("===========")
a=[10,8,4,2,1,7,9,5,3,6]
a.sort()
print(a)
print("===========")
print("===========")
b=[10,8,4,2,1,7,9,5,3,6]
b.sort(reverse=True)
print(b)
print("===========")
print("===========")
c=["annas","thambi","amma","appa"]
c.sort(key=len)
print(c)
c.sort(reverse=True,key=len)
print(c)