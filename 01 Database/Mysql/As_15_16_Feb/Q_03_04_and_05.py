
# *******************************************Answer no : 03************************************************************************
# DML : Data Manuplation Language . The DML commands in Structured Query Language change the data present in the SQL database
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE  if not exists Assignment3")
mycursor.execute("CREATE TABLE if NOT exists Assignment3.ass_table(c1 INT, Name VARCHAR(50), c3 FLOAT , c4 INT , Gmail VARCHAR(30) )")
# INSERT command : Insert command are use to insert values in the table
mycursor.execute("INSERT INTO Assignment3.ass_table (c1 , Name , c3 , c4  , Gmail  ) VALUES (312,'pawan',321.32,3242,'pawan@gmail.com')")


#UPDATE Command :   update command are use to update values in the table
mycursor.execute("UPDATE Assignment3.ass_table SET Gmail = 'pawna3121231@gmail.com' WHERE Name = 'pawan' ")


# DELETE command : delete command are use to delete single or multiple existing data in the table
mycursor.execute("DELETE FROM Assignment3.ass_table WHERE Name = 'pawan' ")





#  ********************************************************Answer no : 04**************************************************************
# DQL : Data Query Language , DQL is used to fetch the data from the database.

mycursor.execute("INSERT INTO Assignment3.ass_table (c1 , Name , c3 , c4  , Gmail  ) VALUES (312,'rakesh',321.32,3242,'rakesh@gmail.com')")

# SELECT command : it is use to fetch data 
mycursor.execute("SELECT *from Assignment3.ass_table")
for i in mycursor.fetchall():
    print(i)



#  ****************************************************Answer no : 05*****************************************************************
# Primary Key : A primary key is used to ensure that data in the specific column is unique. A column cannot have NULL values.
# For Example : STUD_NO, as well as STUD_PHONE both, are candidate keys for relation STUDENT but STUD_NO can be chosen as the primary key (only one out of many candidate keys).
#  
# Foreign Key: 
# A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables. It is a column (or columns) that references a column (most often the primary key) of another table. 
#STUD_NO in STUDENT_COURSE is a foreign key to STUD_NO in STUDENT relation.  

mydb.commit()
mydb.close()