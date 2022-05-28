import functools
print("Enter List Of Values Seperated By Space  :")
lst=[str(val)for val in input().split()]
uppercase=list(map(lambda  n:n.lower(),list(filter(lambda n:n.isupper(),lst))))
lowercase=list(map(lambda  n:n.upper(),list(filter(lambda n:n.islower(),lst))))
print("Given List Of Elements :",lst)
print("Upper Case Names In List  :",uppercase)
print("Lower Case Names In List  :",lowercase)