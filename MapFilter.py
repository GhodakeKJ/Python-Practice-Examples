"""
print("Enter The Names Seperated By Space :")
lst=[str(val) for val in input().split()]
upercase=list(filter(lambda n:n.isupper(),lst))
lowercase=list(filter(lambda n:n.islower(),lst))

print("Given Names In List :",lst)
print("Upper Case Name In List :",upercase)
print("Lower Case Name In List :",lowercase)   """

print("Enter The Names Seperated By Space :")
lst=[str(val) for val in input().split()]
uppercase=list(map(lambda n:n.isupper(),lst,list=(filter(lambda n:))))
