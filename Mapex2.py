

#Main Program
print("Enter List Of Elements Seperated By Space Of First List :")
lst1=[int(val) for val in input().split()]
print("Enter List Of Elements Seperated By Space Of First List :")
lst2=[int(val) for val in input().split()]
sum=list(map(lambda x,y:x+y,lst1,lst2))
print("First List Elements :{}".format(lst1))
print("Second List Of Elements :{}".format(lst2))
print("Sum Of Both List Elements :{}".format(sum))

def sumop(x,y):
    return x+y

#Main Program
lst1=[10,20,30,40,50,60]
lst2=[10,30,50,30,200,20]
obj=list(map(sumop,lst1,lst2))
sum=list(obj)
print("First List Elements :{}".format(lst1))
print("Second List Elements :{}".format(lst2))
print("Sum Of Both Elements :{}".format(sum))

sumop=lambda x,y:x+y

#Main Program
lst1=[10,20,30,40,50,60]
lst2=[800,5433,6544,433,64,32]
obj=list(map(sumop,lst1,lst2))
print("First List :",lst1)
print("Second List :",lst2)
print("Sum Both List :",obj)