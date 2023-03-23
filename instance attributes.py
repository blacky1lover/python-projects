"""
instance attributes apdina
spot laye oru object create pandrathu tha instance attributes
"""
class user:
    name="lamdy"
who_is=user()
print(user.__dict__)
print(user.name) # class attributes
print(who_is.__dict__)
print(who_is.name) # instance attributes
who_is.name="cylinder"
print(who_is.name)
user.name=1
print(user,who_is.__dict__)
who_is=user
print(user.__dict__)
print(who_is.__dict__)