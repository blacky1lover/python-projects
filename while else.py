i=1
while i in range(1,10):
    print(i)
    i+=1
else:
    print("loop completed".title())

print("")
i=1
while i in range(1,10):
    if i==8:
        break
    print(i)
    i+=1
else:
    print("loop completed".title())
print("")
i=1
while i in range(1,10):
    if i==8:
        continue
    print(i)
    i+=1
else:
    print("loop completed".title())