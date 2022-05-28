square=lambda a:a**2

print("Enter List Of Values Seperated By Space  :")
lst=[int(val)for val in input().split()]
square_root=list(map(square,lst))

print("Given List Elements  :",lst)
print("Square Root Of Given List :",square_root)