#Positive Negative Findind By Filter Function

psnum=lambda a:a>0
nsnum=lambda a:a<0
zeros=lambda a:a==0
print("Enter List Of Values Seperated By Space  :")
lst=[int(val)for val in input().split()]

positive=list(filter(psnum,lst))
negative=list(filter(nsnum,lst))
zoro1=list(filter(zeros,lst))
print("Given List Of Elements   :",lst)
print("Positive Elements :",positive)
print("Negative Elements :",negative)
print("Zeros Elements :",zoro1)