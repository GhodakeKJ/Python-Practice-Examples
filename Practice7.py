#Practice7.py
#Get Input Of Three Values And Diside Who among big of them
#By Using if...elif...else condition

a=int(input("Enter First Number  :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third  Number :"))
if(a==b)and(b==c):
    print("All Values Are Same")
elif(a>b)and(a>c):
    print(" A Is Big")
elif(b>a)and(b>c):
    print("B Is Big")
else:
    print("C Is Big")