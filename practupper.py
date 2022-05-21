print("Enter List Of Names Seperated By Space")
lst=(str(val)for val in input().split())
uppercase=list(map(lambda n:n.lower(),(filter(lambda n:n.isupper(),lst))))
lowercase=list(map(lambda n:n.upper(),(filter(lambda n:n.islower(),lst))))
print("Given Names In List :",lst)
print("Lower to Upper Case Names In List :",uppercase)
print("Upper to Lower Case Names In List :",lowercase)

