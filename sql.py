import sqlite3

#Connect to Sqlite

connection=sqlite3.connect("student.db")

##Cretae a Cursor

cursor=connection.cursor()

##Create the table
table_info="""
Create table if not exists STUDENT(NAME VARCHAR (20), CLASS VARCHAR(20),
SECTION VARCHAR(20), MARKS INT);

"""

cursor.execute(table_info)

##Insert Records

cursor.execute(''' INSERT INTO STUDENT VALUES('Alice', 10, 'A', 85)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Bob', 9, 'B', 78)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Charlie', 10, 'A', 92)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('David', 8, 'C', 74)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Emma', 9, 'B', 88)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Frank', 10, 'A', 81)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Grace', 8, 'C', 95)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Hannah', 9, 'B', 79)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Ian', 10, 'A', 87)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Jack', 8, 'C', 90)''')


##Display all records

print("The records are")

data=cursor.execute('''Select * From STUDENT''')


for row in data:
    print(row)

## Close Connection

connection.commit()
connection.close()