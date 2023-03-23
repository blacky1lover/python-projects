"""
ulla exception thappa irutnhalum finally run aagum
correct ah irunthaalum run aagum

"""
try:
    a=10
    b=20
    c=a-c
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("this is a finally statement")
print("===========================")
# ippo pandrathu correct program
# ippovum finally print pannum
try:
    a=10
    b=20
    c=a-b
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("this is a finally statement")