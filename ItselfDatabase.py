import sqlite3
conn=sqlite3.connect("selfpracticedatabace.db")
# inn=input("enter name")
inr=input("enter roll")
# inc=input("enter class")



# conn.execute('''
#     insert into MyAccount(Student_name,Student_roll,Student_class) values(?,?,?)
    
# ''' ,(inn,inr,inc,))



# conn.commit()

# d=conn.execute("SELECT * from MyAccount ")
# for i in d:
#     print(i)

conn.execute("DELETE  FROM MyAccount where Student_id="+inr)
conn.commit()
conn.close()