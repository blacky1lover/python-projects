"""
2:21:30 video will will run
nested if apdina simple
oru if kulla innoru if podurathu tha nested if
ippo namma example ku
grade vekka porom
"""
m1 = int(input("enter your tamil mark = ".title()))
m2 = int(input("enter your english mark = ".title()))
m3 = int(input("enter your maths mark = ".title()))
tot = m1 + m2 + m3
average = tot / 3
if m1 > 35 and m2 > 35 and m3 > 35:
    print("you pass")
    if average >= 90 and average <= 100:
        print("a grade".title())
    elif average >= 65 and average < 90:
        print("b grade ".title())
    elif average >= 37 and average < 65:
        print("c grade".title())
    else:
        print("d grade".title())
else:
    print("you fail")
print("total ", tot)
print("average", average)
