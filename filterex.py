import functools

print("Enter List Of Elements Seperated By Space :")
lst=[int(value)for value in input().split()]
sumop=functools.reduce(lambda x,y:x+y,lst)
print("Given List Elements :",lst)
print("Sum Of List Elements :",sumop)

print("Enter List Of Elements Seperated By Space :")
lst1=[float(val) for val in input().split()]
multiplay=functools.reduce(lambda a,b:a*b,(filter(lambda n:n>0,lst1)))
print("Given List Elements :",lst1)
print("Multiplication Of List Elements :",multiplay)