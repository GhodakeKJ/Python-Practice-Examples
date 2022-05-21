def uppername(n):
    if (n.isupper()):
        return True
    else:
        return False
def lowername(n):
    if(n.islower()):
        return True
    else:
        return False
def mixedname(n):
    if not n.isupper() or (n.islower()):
        return True
    else:
        return False


#Main Program

print("Enter The Names Seperated By Space :")
lst=[str(val) for val in input().split()]
upercase=list(filter(uppername,lst))
lowercase=list(filter(lowername,lst))
mixedcase=list(filter(mixedname,lst))
print("Given Names In List :",lst)
print("Upper Case Name In List :",upercase)
print("Lower Case Name In List :",lowercase)
print("Mixed Case Name In List :",mixedcase)