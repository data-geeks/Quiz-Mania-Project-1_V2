#!/usr/bin/python

# sudo mysql -u root
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test'; 
import mysql.connector as mysql
import xml.etree.cElementTree as ET

# RDS information
username='root'
password='push010808'
database_name='mydatabase'
host='localhost'

# Now connecting the Database
conn=mysql.connect(user=username,password=password,database=database_name,host=host)

# Now generating a SQL language cursor 
cur = conn.cursor()
print("Hey Welcome to Test Adder")
print("Remember the Test Table name starts with TestTime")
print("e.g., TestTime_aws_b ( where aws is testname and b defines the level)")
table_name = input('Enter the table name please: ')
sql = f"INSERT INTO {table_name}(Question,Option1,Option2,Option3,Option4,Answer) VALUES (%s,%s,%s,%s,%s,%s)"

textfile='''
with open('file.txt','r') as file:
    questions = file.readlines()
    for i in questions:
        question,option1,option2,option3,option4,answer = i.split('##')
        cur.execute(sql,(question,option1,option2,option3,option4,answer))
'''

filename = input("please the enter the test xml file with extension to enter into database: ")
tree = ET.ElementTree(file=filename)  # main file
root = tree.getroot()  # Root node doc
for elem in root:
    question = elem[0].text
    option1 = elem[1].text
    option2 = elem[2].text
    option3 = elem[3].text
    option4 = elem[4].text
    answer = elem[5].text
    # to save everything in database
    cur.execute(sql,(question,option1,option2,option3,option4,answer))

conn.commit()
conn.close()
