import functools
addop=lambda a,b:a+b
lst=[10,20,30,40,50]
sumlist=functools.reduce(addop,lst)
print("Given List Elements :",lst)
print("Sum Of List Elements :",sumlist)