
def psnumbers(p):
    if p>0:
        return True
    else:
        return False
def nsnumbers(n):
    if n<0:
        return True
    else:
        return False

#Main Program
print("Enter The List Of Values Seperated By Space :")
lst=[float(val) for val in input().split()]
positive=list(filter(psnumbers,lst))
negativ=list(filter(nsnumbers,lst))
print("The Given List Of Value Are :{}\n".format(lst))
print("Positive Numbers :{}".format(positive))
print("Negative Numbers :{}".format(negativ))


