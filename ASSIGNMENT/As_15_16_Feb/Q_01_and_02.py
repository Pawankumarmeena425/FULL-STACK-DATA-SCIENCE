# *******************************************************Answer no : 01******************************************************************

# Database : A database is an organized collection of structured information, or data, typically stored electronically in a computer system. 
# sql : structure query language , sql is a database arrange in the relational tabuler form in which data arrange in a structure
# NOSQL : not only structure query language , nosql is a non relational in nature and data arrange in a random manner





#******************************************************* Answer no : 02*****************************************************************


""" --->>> DLL : Dynamic Link Library -->> A DLL is a library that contains code and data that can be used by more than one program at the same time.
    --->>> DLL files contain compiled code
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

# ALTER command : ALTER  command are use to  adds, deletes, or modifies columns in a table.
# CREATE command : create  comman are use to creadte database , table  

mycursor.execute("CREATE DATABASE  if not exists Assignment")
mycursor.execute("CREATE TABLE if NOT exists Assignment.ass_table(c1 INT,c2 VARCHAR(50), c3 FLOAT , c4 INT , c5 VARCHAR(30) )")
        
mycursor.execute("ALTER TABLE Assignment.ass_table ADD Email varchar(50)")
mycursor.execute("insert into Assignment.ass_table values(1232,'sudh',132.312,123,'pawan','Pawan@gmail.com')")

mycursor.execute("insert into Assignment.ass_table (Email)  values ('pawankumar@gmail.com')")
mydb.commit()
mycursor.execute("select *from Assignment.ass_table")
for i in mycursor.fetchall():
    print(i)

# DROP command : drop command are use to delete colunms or table 
mycursor.execute("DROP TABLE Assignment.ass_table")
# TRUNCATE command : it is use to delete content inside the table but not delete table

mydb.commit()





mydb.close()





