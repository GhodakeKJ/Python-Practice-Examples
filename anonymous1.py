'''def add(a,b):  #By Normal Defination Function
    c=a+b
    return c

x=float(input("Enter First  Value For Addition  :"))
y=float(input("Enter Second  Value For Addition :"))
result=x+y
print("Sum :",result)'''

# By Anonymous Function
addop=lambda a,b:a+b

sumlist=addop(10,20)

print("SUM OF LIST  :",sumlist)