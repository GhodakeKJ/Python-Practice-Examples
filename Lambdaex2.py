big=lambda a,b:a if a>b else b


#Main Program

x=int(input("Enter First Value  :"))
y=int(input("Enter Second Value :"))
result=big(x,y)
print("( {} and {} ) = {} Is Big".format(x,y,result))