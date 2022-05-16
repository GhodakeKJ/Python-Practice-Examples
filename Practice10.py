#Practice10.py
#Program for generating even numbers by using while loop statements
n=int(input("Enter Any Number :"))
if(n<=0):
	print("{} Is Invalid Number Enter +ve Number ".format(n))
else:
	i=2
	while(i<=n):
		print("\t{}".format(i))
		i=i+2