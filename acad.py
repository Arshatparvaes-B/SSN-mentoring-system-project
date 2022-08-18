from main import cat1,cat2
import ARRAY

def math(arr,n=3):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def beee(arr,n=4):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def phy(arr,n=5):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def pds(arr,n=6):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def hse(arr,n=7):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

def evs(arr,n=8):
    marks=ARRAY.Arr()
    for i in arr:
        marks.append([i[0],i[1],i[n]])
    return marks

for i in math(cat1):
    print(i)
print()
for i in evs(cat1):
    print(i)



