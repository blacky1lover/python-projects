"""
find  a book to give to library to delay fine
0 days= no fine
1-5 days = 0.5
5-10 days = 1
10-30 days =5
above 30 days = membership cancel"""
d = int(input("enter no.of days = ".title()))
if d == 0:
    print("great you dont want to pay a fine".title())
elif d >= 1 and d <= 5:
    print("you want to pay a fine".title(), d * 0.5)
elif d > 5 and d <= 10:
    print(" you  want to pay a fine".title(), d * 1)
elif d > 10 and d <= 30:
    print(" you  want to pay a fine".title(), d * 5)
else:
    print('you want cancel a membership'.title())
