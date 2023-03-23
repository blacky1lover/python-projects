



for i in range(0, 10, 2):
    print(i, "this is a even number".title())
print("=====================")
for j in range(1, 10, 2):
    print(j, "this is a odd number".title())
print("========================")
print("""
      1 is a adding method
      2 is a subtraction method
      3 is a multiplication method
      4 is a dividing method""".title())
for i in range(5):
    a = int(input("enter a number = ".title()))
    b = int(input("enter a number = ".title()))
    c = a + b
    d = a - b
    e = a * b
    f = a // b
    choice = int(input("enter your method = ".title()))
    if choice == 1:
        print(c)
    elif choice == 2:
        print(d)
    elif choice == 3:
        print(e)
    elif choice == 4:
        print(f)
    else:
        print("syntax error".title())
