import functools

print("Enter The List Of Names/Words Seperated By Space :")
lst=[str(val) for val in input().split()]
line=functools.reduce(lambda a,b:a+" "+b,lst)
print("List Of Elements :",lst)
print("Text Line Of Elements :",line)