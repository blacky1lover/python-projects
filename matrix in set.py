"""
union
intersection
intersection_update
symmetric_difference
symmetric_dufference_update
"""
a={"hii","bro","hello"}
b={1,2,4,5}
c=a.union(b)
print(c)

print("================")
print("================")
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.intersection(b)
print(c)
# ipdium pannalam
a.intersection_update(b)
print(a)

print("================")
print("================")
a={1,2,3,4,5}
b={4,5,6,7,8}
c= a.symmetric_difference(b)
print(c)
# ipdium pannalam
a.symmetric_difference_update(b)
print(a)
print("================")
print("================")
a={1,2,3,4,5}
b={4,5,6,7,8}
d={9,10,11,12}
c=a.isdisjoint(b)
e=a.isdisjoint(d)
print(c)
print(e)
print("================")
print("================")
a={11,13,14}
b={5,6,7,8,9}
d={11,12,13,14}
c=a.issubset(b)
e=a.issubset(d)
print(c)
print(e)
print("================")
print("================")
a={5,6,7}
b={5,6,7}
c=a.issuperset(b)
print(c)
print("================")
print("================")
a={5,6,7}
b={5,6,7,8}
c=a.issuperset(b)
print(c)






