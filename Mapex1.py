#Main Program
print("Enter The List Of Numbers Seperated By Space :")   #By map function
lst=[int(val)for val in input().split()]
squares=list(map(lambda n:n**2,lst))
print("Given List Of Elements =",lst)
print("Square Root Of Given Elements :",squares)

squares=lambda n:n**2      #By Anonumous Function

#Main Program
print("Enter List Of Values Seperated By Space :")
lst=[int(val)for val in input().split()]
obj=list(map(squares,lst))
print("Original List :",lst)
print("Square Root Elements :",obj)

def squares(n):
    return (n ** 2)

#Main Program
print("Enter List Of Elements Seperated By Space :")
lst=[int(val) for val in input().split()]
obj=map(squares,lst)
squareroot=list(obj)
print("Type Of obj :",obj)
print("Original Elements :",lst)
print("Squares Root Elements :{}".format(squareroot))
