potive=lambda n:n>0     #By Using Anonymous Functions
nagative=lambda n:n<0   #By Using Anonymous Functions
zero=lambda n:n==0      #By Using Anonymous Functions

#Main Program
print("Enter The Values Seperated By Space :")
lst=[int(val) for val in input().split()]
print("="*80)
print("Given Values Are :",lst)
print("="*80)
pslist=list(filter(potive,lst))
print("Positive Value Are :",pslist)
print("="*80)
nslist=tuple(filter(nagative,lst))
print("Negative Value Are :",nslist)
print("="*80)
zeros=list(filter(zero,lst))
print("Zeros Are in Values :",zeros)