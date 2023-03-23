"""
del keyword vechi ulla irukura
data va delete panna porom
ethu poi irukunu dictionary use panni paarom
"""


class student():
    name = "lamdy"
    age = 1


student.year = 2

print(student.year)
student.skills = "extraordinary skills"

print(student.skills)
print(student.__dict__)
del student.year

print(student.__dict__)
