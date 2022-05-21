multipliocation=lambda x,y:x*y

#Main Program
print("Enter Fisrt List Elements :")
lst1=[int(val) for val in input().split()]
print("Enter Second List Elements :")
lst2=[int(val) for val in input().split()]
obj=list(map(multipliocation,lst1,lst2))
print("First List Elements :",lst1)
print("Second List Elements :",lst2)
print("Multiplication Of Both List :",obj)

def multip(x,y):
    return x*y

#Main Program
lst=[2,3,4,5,7,10]
lst1=[8,6,4,7,4,3]
obj=list(map(multip,lst,lst1))
print("First List Elements :",lst)
print("Second List Elements :",lst1)
print("Multiplication Of Both List :",obj)

print("Enter First List Elements :")
lst1=[int(val) for val in input().split()]
print("Enter Second List Elements :")
lst2=[int(val) for val in input().split()]
multi=list(map(lambda x,y:x*y,lst1,lst2))
print("First Elements List :",lst1)
print("Second Elements List :",lst2)
print("Multiplication Of Both List :",multi)