#Practice19.py
#Program for in while loop statementsfor i in range(1,7):
for i in range(1,7):
	print("="*50)
	print("Value Of  i===>Outer for loop statements : {}".format(i))
	j=1
	while(j<=3):
		print("Value Of  j===>Outer for loop statements : {}".format(j))
		j=j+1
	else:
		print(" I Am Out From inner while Loop")
		print("="*50)
else:
	print(" I Am Out From Outer for loop")
print("="*50)