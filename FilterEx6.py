upperc=lambda u:u.isupper()
lowerc=lambda l:l.islower()
mixc=lambda m: not (m.isupper() or m.islower())

#Main Program

print("Enter The Names Seperated By Space :")
lst=[str(val) for val in input().split()]
print("Given List Of Names :",lst)
upperwords=list(filter(upperc,lst))
print("Names Are In Upper :",upperwords)
lowerwords=tuple(filter(lowerc,lst))
print("Names In Lower :",lowerwords)
mixedletters=list(filter(mixc,lst))
print("Mixed capital/Small :",mixedletters)