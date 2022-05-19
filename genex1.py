def karan(x,y):
    while(x>=y):
        yield x
        x=x-1

obj=karan(10,1)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break