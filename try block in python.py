"""
ithula keyword = try , except , Exception
itha vechi run time la enna error nu kandu pudikalam
correct ah irunthaal print aagathu

"""
try:
    a=10/0
except Exception  as e:
    print(e)
# ithu thappa irukku try use panni enna error nu print aagum
try:
    a=10
    b=20
    c=a-c
except Exception as e:
    print(e)
# ithu correct ah athanala answer print aagathu
# correct ah irukku answer print aaganumna
# adutha program
# try block else poi paaru da
try:
    a=10
    b=20
    c=a-b
except Exception as e:
    print(e)