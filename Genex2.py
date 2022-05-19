def karan(x,y,z):
    while(x<=y):
        yield x
        x=x+z

obj=karan(0,100,10)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break