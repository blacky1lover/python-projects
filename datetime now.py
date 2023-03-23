# printing a current date
import datetime as ab

aks = ab.date.today()
print(aks)
print("===========================================")
# printing a we want to see a date which date and month
new = ab.date(2023, 3, 10)
print(new)
print(new.year)
print(new.month)
print(new.day)
print("================================================")
# we want to see a time which time to see
a=ab.time(10,20,45,233)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
print("==============================================")
ct=ab.datetime.now()
print(ct)
print("==============================================")
# creating a time
b=ab.datetime(2023,3,10,10,20,50,455)
print(b)
print(b.year)
print(b.month)
print(b.day)
print(b.hour)
print(b.minute)
print(b.second)
print(b.microsecond)
print("=================================================")
# finding a date and time diffference
# or
# counting a date
cur=ab.datetime.now()
bd=ab.datetime(2024,3,10,6,00,45,456)
differ=cur-bd
print(differ)
print('==================================================')
