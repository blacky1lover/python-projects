g = -2
for z2 in range(6, 13, 5):
    g += z2
    print(g)
print("======================")
g = 2
for i in range(0, 10):
    g += i
    print(g)
print("=====================")
"""
e = 'lion'
e[:2] = "horse"
print(len(e))
"""
print("=====================")
x = "126217"
print(x + x[4])
print('3073129'[2])
n = 6
r = 1.5
print(n // r)


def fnc():
    return 'whale', "-1", "deer", "bird"


print(len((fnc(),)))
c1 = {a * 2 for a in range(8)}
c2 = {a * 3 for a in range(8)}
c3 = {a * 4 for a in range(8)}
c4=c1|c2|c3
print(c4)
print(2>5)
print(2<5)
