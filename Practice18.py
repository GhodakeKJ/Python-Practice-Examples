#Practice18.py
#Programwhile in while loop statements
i=1
while(i<=5):
	print("="*50)
	print("="*50)
	print("Value Of  i===>Outer for loop statements : {}".format(i))
	j=1
	while(j<=3):
		print("Value Of  j===>Outer for loop statements : {}".format(j))
		j=j+1
	else:
		print("I Am Out From inner while Loop")
		i=i+1
else:
	print("I Am Out From Outer while loop")
print("="*50)