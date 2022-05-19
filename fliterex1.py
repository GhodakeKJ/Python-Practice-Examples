def psnum(x):          #By Using Defination Function
    if x>0:
        return True
    else:
        return False
def nslist(s):          #By Using Defination Function
    if s<0:
        return True
    else:
        return False

#Main Program
print("Enter List Of Values Seperated By Space :")
lst=[int(val) for val in input().split()]
pslist=list(filter(psnum,lst))
nslist=tuple(filter(nslist,lst))          #Function Call
print("Type Of pslst =",type(pslist))
print("="*60)
print("Given List ={}".format(lst))       #Function Call
print("="*60)
print("Positive List ={}".format(pslist))
print("="*60)
print("Negative List ={}".format(nslist))             #Function Call
print("="*60)