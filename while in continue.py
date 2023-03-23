"""
continue statement
ithu enna na onnu namma ku venum ana athu thaandi tha poganum athanala athu vara varikkum ithu pannite irukkum
vanthuchuna athukun aprm irukura program ah run pannum

"""
i = 1
while i <= 20:
    if i % 2 == 0:
        i = i + 1
        continue

    print(i)
    i += 2

