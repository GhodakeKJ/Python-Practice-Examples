
def fun1():
    yield "Python"
    yield "Java"
    yield "Django"
    yield "Android"

#Main Program
result=fun1()
print(next(result))
print(next(result))
print(next(result))
print(next(result))

