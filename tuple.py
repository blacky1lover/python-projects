"""
=>  tuple we use this () symbol
=>  tuple and list is little bit same but many changes also is there
=>  tuples ah list maari change panna mudiyathu
=>  but ana atha list ah convert panni pannalam
=>  ana ithula oru digit mattum kuduthaal athu integer ah vechikkum athanala antha single digit pakkathula oru comma , symbol use panni potta athu tuple ah
 vechikkum
=> del intha function use panni namma oru variable oda value va
=> delete panni kilam
=> adding a tuple to using a plus symbol
"""
a=(10,20,30,40)
print(type(a))
# tuple to list
print(list(a))
print(type(list(a)))
print("============")
print("============")
b=(5,"rocky",6.6,False)
print(b)
print(type(b))
print("============")
print("============")
# take a particular tuple index
print(b[1])
print("============")
print("============")
# nested tuple
h=("hello",3,True,("hi","god"))
print(h[3][1])
# inserting a value using list and change to a tuple
j=("natarajan","vijaya","anna malai","naveen kumar")
print(j)
n=list(j)
print(n)
n.append("rithesh".title())
print(n)
print(tuple(n))
print("=================")
print("=================")
job=("salary","experience")
jobs=list(job)
jobs.append("skill")
print(jobs)
job=tuple(jobs)
print(job)