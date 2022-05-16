#Practice9.py
#Generate 1 to nth number where nth is +ve By Using while & for loop statements
lst=[10,20,30,40,50,"Python","java","Django","UI","JScript"]
print("="*60)
print("By Using For Loop Statements")
for val in lst:
	print("\t {}".format(val))

print("="*60)
print("By Using while Loop Statements")
i=0
while(i<len(lst)):
	print("\t{}".format(i),end="		")
	i=i+1