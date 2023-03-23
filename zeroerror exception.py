"""
namma zero vaala division panna koodathu
or
panna mudiyathu
athu error varum athanala
 namma exception kuduthu paakrom
 or ulla ethuna message kuduthaal athu print aagum

"""
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(e)
    # ipdium kudukalam
    print("zero vaala entha number aium divide panna mudiyathu lamdy".title())
    # or
    print("denominator cant be zero lamdy".title())
