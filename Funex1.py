def kvrrange(x,y):
    while(x<=y):
        yield x
        x=x+1
        
#Main Program
kvrobj=kvrrange(1,10)
while(True):
    try:
        print(next(kvrobj))
    except StopIteration:
        break
