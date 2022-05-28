def show(sno,sname,*marks,cnt="India",crs="Python",**keyvalue):
    print("="*50)
    print("Student Number:",sno)
    print("Student Name  :",sname)
    print("=" * 50)
    print("Student Marks :")
    for val in marks:
        print("\t{}".format(val))
    print("=" * 50)
    print("Student Country  :",cnt)
    print("Student Courrse  :",crs)
    print("=" * 50)
    for key,value in keyvalue.items():
        print("\t{}\t\t{}".format(key,value))
    print("=" * 50)



#Main Program
show(101,"Rrossum",78,86,94,hobby1="Reading",hobby2="Developing",hobby3="Watching Games")
show(102,"Scott",67,44,63,game="Pubg",game2="Free-Fire",game3="Ludo")
show(110,"Karan",75,88,85,cnt="USA",crs="Android",app1="Cricket11",app2="Facebook",app3="Instagram")