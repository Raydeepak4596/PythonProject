import sqlite3
conn=sqlite3.connect("mydatabase.db")
# ========== for create table======
# conn.execute('''
#     Create table Student(st_ID AUTO INCREMENT PRIMARY KEY ,st_name VARCHAR(50),st_class VARCHAR(10),st_email VARCHAR(30))

# ''')
# conn.close()
# =========create table end=====



# =================inset data=======
# ins='''
#     insert into Student(st_name,st_class,st_email)values("Deepak","BCA","raydeep4@gmail.com")
# '''
# conn.execute(ins)
# conn.commit()
# conn.close()


# ============end insert data=======


# data=conn.execute("select * from Student")
# print("St_id","St_name"," St_Class","St_email")
# for d in data:
#     # print(d)
#     print(d[0],"    ",d[1],"    ",d[2],"    ",d[3])

