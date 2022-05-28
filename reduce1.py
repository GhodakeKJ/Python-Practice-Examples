import functools

line=lambda a,b:(a+" "+b)
print("Enter List Of Words Seperated By Space :")
lst=[str(val)for val in input().split()]
linewords=functools.reduce(line,lst)
print("Fiven Words List  :",lst)
print("One Line In All Words :",linewords)