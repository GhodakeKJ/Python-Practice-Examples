def kvr(n):
    if n.isupper():
        return True
    else:
        return False
def karan(k):
    if k.islower():
        return True
    else:
        return False
def mixed(m):
    if m.isupper() or m.islower():
        return False
    else:
        return True

#Main Program
print("Enter The Name Separated By Space :")
lst=[str(val) for val in input().split()]
uppername=list(filter(kvr,lst))
lowername=list(filter(karan,lst))
bothmix=list(filter(mixed,lst))
print("Names In Given List :{}".format(lst))
print("Upper Names In Given List :{}",uppername)
print("Lower Names In Given List :{}",lowername)
print("Mixed Names In Given List :{}",bothmix)