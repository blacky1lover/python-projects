"""
oru file iruntha atha read or any other work pannum
antha file illana namma ulla ethuna message kuduthaal print aagum

 or

normal ah print aagum
"""
try:
    f = open("sample.py")
except FileNotFoundError  as fe:
    print(" ipdi oru file illa lamdy")
    # or ipdium kudukalam
    print(fe)
else:
    print(f.read())

