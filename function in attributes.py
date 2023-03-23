"""
epdila ulla kuduthu print pannala using user define function
function odaya adddresum paakalam
"""
# class methods


class student:
    name = "lamdy"
    place = "canada"

    def listhere():
        print("name : ", student.name)
        print("place : ", student.place)


student.listhere()  # ipdium print pannalam
print(student.__dict__)
print(getattr(student, "listhere")) # function oda address paakalam
getattr(student, "listhere")()  # ipdium print pannalam
student.__dict__["listhere"]()  # ipdium print pannalam
