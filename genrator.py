def generator(k,g):
    while(k<=g):
        yield k
        k=k+1

obj=generator(1,10)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break
print("=============================================")
def gen(k,v,r):
    while(k<=v):
        yield k
        k=k+r

obj=gen(100,200,10)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break