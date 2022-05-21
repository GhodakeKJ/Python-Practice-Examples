
print("Enter The List Of Names Seperated By Space :")
lst=[str(val) for val in input().split()]
uppername=list(filter(lambda n : n.isupper(),lst))
lowername=list(filter(lambda n : n.islower(),lst))
mixedname=list(filter(lambda n : not n.isupper() or (n.islower())))
print("Given List Of Names :",lst)
print("Upper Names In Lists :",uppername)
print("Lower Names In Lists :",lowername)
#print("Mixed Names In Lists :",miKaran all is well INDIA IS MY COUNTRY How I CAN help You PytHonxedname)