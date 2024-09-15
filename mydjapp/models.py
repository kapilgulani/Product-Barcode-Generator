import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db="djangobatch56"
)

print("Successfully connected to MySQL database....")