# ************************************************************Answer no : 06*****************************************************************


# python code to connect MySQL to python.
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",  #------>>>>> connection establishment
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE  if not exists Question")
mydb.close()

# cursor method : A cursor in SQL Server is a database object that allows us to retrieve each row at a time and manipulate its data.ursor's purpose is to update the data row by row, change it, or perform calculations that are not possible when we retrieve all records at once.

# execute method ; he execute command is used to execute a stored procedure.



# ************************************************ Answer no : 07**************************************************************

# 1. FROM   --->>> Tables are joined to get the base data.
# 2. WHERE	--->>>  The base data is filtered.
# 3. GROUP BY   -->>> The filtered base data is grouped.
# 4 . HAVING	--->>> The grouped base data is filtered.
# 5 . SELECT	--->>> The final data is returned.
# 6 . ORDER BY	--->>> The final data is sorted.
# 7 . LIMIT	     --->>>> The returned data is limited to row count.
