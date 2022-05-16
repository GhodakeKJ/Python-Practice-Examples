#Practice12.py
#Program for calculating sum of nth number where nth must be +ve

n=int(input("Enter Any Number For Sum :"))
if(n<=0):
	print("="*50)	
	print(" {} Is Invalid Input Enter Posotive Value/Number".format(n))
else:
	
	s=0
	i=1
	while(i<=n):
		print("\t{}".format(i))
		i=i+1
		s=s+i
	else:
		print("="*50)
		print(" Sum Of {} :".format(s))
print("="*50)