list
def collection(obj):
    print("="*50)
    print("Type Of Of obj :",type(obj))
    print("-" * 50)
    for val in obj:
        print("\t{}".format(val))
    print("=" * 50)

def display(obj):
    print("=" * 50)
    print("Type Of Of obj :", type(obj))
    print("-" * 50)
    for key,value in obj.items():
        print("{}\t\t\t{}".format(key,value))


list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
collection(list)

set ={"Apple","Mango","Cherry","Kiwi","Banana","Grapes"}
collection(set)

tuple=("Python","Django","Java","Data Science","Machine Learning","Android")
collection(tuple)

dict={"Rossum":1991,"Gosling":1980,"Ritche":1987,"Scott":2001}
display(dict)
print("="*50)
