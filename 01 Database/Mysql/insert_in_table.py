import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(1232,'sudh',132.312,123,'pawan')")
mydb.commit() # change happen only after the commit command

mydb.close()
