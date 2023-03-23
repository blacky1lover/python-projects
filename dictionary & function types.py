user = {
    "name":"money",
    "age":"20",
    "skills":"professional killer"
}
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())
print("==================")
user.update({"gender":"male"})
print(user)
print("==================")
user["age"]=30
print(user)
print("==================")
user.pop("age")
print(user)
print("==================")
