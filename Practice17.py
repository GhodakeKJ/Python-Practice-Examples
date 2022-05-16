#Practice17.py
#Program for in for loop statements
for i in range(1,7):
	print("="*50)
	print("Value Of  i===>Outer for loop statements : {}".format(i))
	for j in range(1,4):
		print("Value Of  j===>Outer for loop statements : {}".format(j))
	else:
		print("\t I Am Out From Inner for loop")
		print("-"*50)
else:
	print(" I Am Out From Outer For Loop")