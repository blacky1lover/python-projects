"""
multiple handling
 ithula oru exception tha run aguthu rendume thappa iruntha athu print aaga maatrukku
 renduthula onnu mattum tha run aaguthu
"""
print("ithu correct ah print aagum lamdy")
try:
    a = 10 / 20
    print(a)
    b = [10, 20, 30, 40]
    print(b[1])
except ZeroDivisionError as zd:
    print(" zero vaala ethaium divide panna mudiyathu lamdy")
except IndexError as ie:
    print("intha index number illa lamdy")
print("===============================")
print("ithu thappa print aagum athanala exception run aagum lamdy")
try:
    a = 10 / 20
    print(a)
    b = [10, 20, 30, 40]
    print(b[10])
except ZeroDivisionError as zd:
    print(" zero vaala ethaium divide panna mudiyathu lamdy ")

except IndexError as ie:
    print("intha index number illa lamdy")
