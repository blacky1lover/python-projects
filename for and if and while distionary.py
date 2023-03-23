user={
    "name":"money",
    "age":"20",
    "skills":"professional killer"
}
for x in user:
    print(x)
    print(user[x])
    print(x, " ", user[x])
for x in user.keys():
    print(x)
for x in user.values():
    print(x)

for x in user.items():
    print(x)
if "age" in user:
    print("yes")
if "20" in user.values():
    print("yes")
if "gender" in user:
    print("yes")
else:
    print("no")
