#Practice8.py
#Generate 1 to nth number where nth is +ve
n=int(input("Enter A Number :"))
print("="*60)
print("By Using while Loop Statement")
if(n<=0):
	print("{} Is Invalid Input ... Enter +ve Number".format(n))
else:
	i=1
	while(i<=n):
		print("\t{}".format(i))
		i=i+1
