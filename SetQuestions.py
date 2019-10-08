#!/usr/bin/python

# sudo mysql -u root
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test'; 
import mysql.connector as mysql

# RDS information
username='root'
password='password'
database_name='test'
host='localhost'

# Now connecting the Database
conn=mysql.connect(user=username,password=password,database=database_name,host=host)

# Now generating a SQL language cursor 
cur = conn.cursor()
table_name = 'Test'
sql = f"INSERT INTO {table_name}(Question,Option1,Option2,Option3,Option4,Answer) VALUES (%s,%s,%s,%s,%s,%s)"

with open('file.txt','r') as file:
    questions = file.readlines()
    for i in questions:
        question,option1,option2,option3,option4,answer = i.split('##')
        cur.execute(sql,(question,option1,option2,option3,option4,answer))

conn.commit()
conn.close()
