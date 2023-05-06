import mysql.connector

database = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Windbre4r"

	)
#prepare a cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")