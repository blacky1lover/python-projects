"""
ulla kuduthathu la delete aiduchu lamdy
namma ulla poi dctionary use panni ulla poi paartha anga
namma entha key kuduthomo athu irukathu
"""


class student():
    name = "lamdy"
    age = 1


student.year = 2

print(student.year)

student.skills = "extraordinary skills"

print(student.skills)
# namma compare pandrathukaga inga dict use panni irukom
print(student.__dict__)
delattr(student, 'skills')

print(student.__dict__)
