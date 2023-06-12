# how to connect mysql to db .In order to connect MySQL with any programming language, including Python, you need a
# connector that acts as a bridge between the MySQL database server and the programming language.

# open cmd
# pip install mysql-connector/
# pip install --upgrade mysql-connector-python


# 1) import the MySQL Connector using the command "import mysql.connector".
# To establish a connection, use the "connect()" method with parameters for username, password, host, and database name.
# The connection object is stored in a variable called "mydb".
# To execute SQL statements, use the "execute()" method on a cursor object obtained from the connection.
# For example, to fetch all databases, use "mycursor.execute('SHOW DATABASES')".
# Use a loop to iterate import mysql.connectorover the result set obtained from the cursor, and print the values.
# To fetch specific data from a table, use the SQL SELECT statement with the table and database names specified.
# Fetch methods like "fetchall()" and "fetchone()" can be used to retrieve the data from the result set.
# The fetched data can be storedimport mysql.connector in variables or printed directly.
# Additional operations like inserting data can also be performed using the "execute()" method.


import mysql.connector

# mydb=mysql.connector.connect(host="localhost",user="root",password="root")
mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="divya")

cursor = mydb.cursor()
cursor.execute("show databases")

for i in cursor:
    print(i)

# Execute query
cursor.execute("SELECT * FROM student")

# Fetch results
result = cursor.fetchall()
for row in result:
    print(row)

# Close cursor and connection
cursor.close()
mydb.close()
