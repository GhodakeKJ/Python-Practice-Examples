#Practice6.py

a=int(input("Enter First Number  :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third  Number :"))
if(a==b)and(b==c):
    print("All Values Are Same")
else:
    if(a>b)and(a>c):
        print("({},{},{})={}".format(a,b,c,a))
    else:
        if(b>a)and(b>c):
            print("({},{},{})={}".format(a, b, c, b))
        else:
            print("({},{},{})={}".format(a, b, c, c))