import functools

print("Enter List Of Values Seperated By Space  :")
lst=[int(val)for val in input().split()]
positive=functools.reduce(lambda a,b:a+b,list(map(lambda a:a**2,list(filter(lambda a:a>0,lst)))))
negative=functools.reduce(lambda a,b:a+b,list(map(lambda a:a**2,list(filter(lambda a:a<0,lst)))))
print("Given List Of Elements   :",lst)
print("Positive Elements :",positive)
print("Negative Elements :",negative)