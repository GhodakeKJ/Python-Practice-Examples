import functools

print("Enter List Of Elements Seperated By Space :")
lst=[int(val) for val in input().split()]
maxnumber=functools.reduce(lambda a,b:a if a>b else b,lst)
minnumber=functools.reduce(lambda a,b:a if a<b else b,lst)

print("Given List Elements :",lst)
print("Maximum Number In List :",maxnumber)
print("Minimum Number In List :",minnumber)