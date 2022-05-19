big=lambda a,b,c:"All Values Are Same" if (a==b==c) else a if(b<=a>c) else b if(a<b>c) else c


#Main Program

x=float(input("Enter First Value :"))
y=float(input("Enter Second Value :"))
z=float(input("Enter Third Value :"))
result=big(x,y,z)
print(" ( {} , {} , {} ) = {}".format(x,y,z,re1sult))