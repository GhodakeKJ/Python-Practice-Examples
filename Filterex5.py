#By Using Defination Functions
def positive(p):
    if p>0:
        return True
    else:
        return False
def nagative(n):
    if n<0:
        return True
    else:
        return False
def zero(z):
    if z==0:
        return True
    else:
        return False

#Main Program
print("Enter Your Values Seperated By Space  :")
lst=[int(val) for val in input().split()]
print("Given List Of Values :",lst)
positivenum=list(filter(positive,lst))
print("Positive Values  :",positivenum)
negativenum=list(filter(nagative,lst))
print("Negative Values :",negativenum)
zeros=tuple(filter(zero,lst))
print("Zeros In Values :",zeros)