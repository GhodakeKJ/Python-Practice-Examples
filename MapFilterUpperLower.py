

#Main Program

print("Enter The List Of Names Seperated By Space :")
lst=[str(val) for val in input().split()]
uppercase=list(map(lambda n:n.lower(),(filter(lambda n:n.isupper(),lst))))
lowercase=list(map(lambda n:n.upper(),(filter(lambda n:n.islower(),lst))))
print("Names In Given List :",lst)
print("Upper Case Name List :",uppercase)
print("Lower Case Name List :",lowercase)