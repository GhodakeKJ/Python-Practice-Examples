#practice20.py
lst=[10,20,30,40,50,60,70,110,200]
s=0
for val in lst:
	print("\t Sum :{}".format(val))
	s=s+val
else:
	print("="*50)
	print("\t Sum :{}".format(s))
	print("-"*50)
	print("\t Average : {}".format(s/len(lst)))
	print("="*50)
