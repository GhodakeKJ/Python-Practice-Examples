big=lambda a,b:"All Values Are Same" if a==b else a if a>b else b

#Main Program
x=float(input("Enter Fisrt Value  :"))
y=float(input("Enter Second Value :"))
result=big(x,y)
print("( {}  and {} ) = {} Is Big".format(x,y,result))