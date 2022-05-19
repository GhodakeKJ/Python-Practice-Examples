def big(a,b):
    if a>b:
        return a
    else:
        return b

def small(a,b):
    if(a<b):
        return a
    else:
        return b
def zero(a,b):
    if(a==b):
        return "Both Are Same"
    else:
        return "Both Numbers Are Not Same"

#Main Program
k=int(input("Enter First Number :"))
g=int(input("Enter Second Number :"))
result=(big(k,g))
print("( {} And {} ) = {} Is Number Big".format(k,g,result))
result1=(small(k,g))
print("( {} And {} ) = {} Is Number Small".format(k,g,result1))
result2=zero(k,g)
print("( {} And {} ) = {} ".format(k,g,result2))