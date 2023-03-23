"""

"""


class sample():
    a = 10
    b=10.2
    print(type(a))
    print(type(b))
adding=sample()
print(type(sample))
# class oda object tha adding ah nu kettu irukke
print(isinstance(adding,sample))
# int oda class kuduthuttu ulla atha irukka nu kettun irukke
print(isinstance(10,int))
#naan float kuduthuttu int irukka nu kettu irukke athanaala false nu varum
print(isinstance(10.2,int))