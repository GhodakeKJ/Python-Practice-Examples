#Practice11.py
#Program for generating odd numbers by using while loop statements
n=int(input("Enter Any Number :"))
if(n<=0):
	print("\t {} Is Invalid Input Enter +ve Number:")
else:
	i=1
	while(i<=n):
		print("\t{}".format(i),end= "    ")
		i=i+2