#Practice14.py
#Program For Multiplication Of Nth number
n=int(input("Enter Any Number :"))
print("="*50)
if(n<=0):
	print(" {} is invalid input enter +ve number".format(n))
else:
	print("="*50)
	print("Multiplication Table Of  : \t{}".format(n))
	print("="*50)
	for i in range(1,11):
		print("\t {} \t X \t {} \t=\t {}".format(n,i,n*i))
print("="*50)
