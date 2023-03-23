for i in range(0,10):
    if i==7:
        break
    print(i)
    i+=1
else:
    print("loop completed".title())
print(" ")
for i in range(0,10):
    if i==7:
        continue
    print(i)
else:
    print("loop completed".title())
