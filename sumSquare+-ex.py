import functools

#Main Program

print("Enter List Of Elements Seperated by Space :")
lst=[int(val)for val in input().split()]
psslist=functools.reduce(lambda a,b:a+b,list(map(lambda a:a**2,list (filter(lambda a:a>0,lst)))))
nsslist=functools.reduce(lambda a,b:a+b,list(map(lambda a:a**2,list (filter(lambda a:a<0,lst)))))

print("Given List Of Elements :",lst)
print("Sum Suares Positive List Elements :",psslist)
print("Negative Square Sum Of List Elements :",nsslist)