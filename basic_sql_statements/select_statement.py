"""
Module to practice with mySQL SELECT statements

Daniel Zapata - 2024
"""

import mysql.connector as mysql

# Connect to the database
personas_db = mysql.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="personas_db")

# Create a cursor to interact with the database
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
# Fetch all the rows from the cursor
personas = cursor.fetchall()

for persona in personas:
    print(persona)

# Close the cursor and the connection
cursor.close()
personas_db.close()
