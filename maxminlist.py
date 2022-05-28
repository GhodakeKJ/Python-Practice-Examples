maxnum=lambda obj:max(obj)
minnum=lambda obj1:min(obj1)

print("Enter List Of Values Seperated By Space  :")
lst=[float(val)for val in input().split()]
maxval=maxnum(lst)
minval=minnum(lst)
print("Given List Of Elements   :",lst)
print("Maximum Value In List Is :",maxval)
print("Minimum Value In List Is :",minval)