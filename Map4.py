
#Main Program
print("Enter List Of Values For First List :")
lst1=[int(val) for val in input().split()]
pslist=list(map(lambda n:n**2,list(filter(lambda n: n>0,lst1))))
nslist=list(map(lambda n:n**2,list(filter(lambda n:n<0,lst1))))
print("Given List Of Elements :",lst1)
print("Positive Elements List :",pslist)
print("Negative Elements List :",nslist)