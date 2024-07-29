"""
Module to practice with mySQL INSERT statements

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
# Insert a new row into the table
# The %s and %i are placeholders for the values that will be inserted
sql_sentence = 'INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'
values = ("Juan", "Perez", 45)
cursor.execute(sql_sentence, values)
# Commit the changes to the database
personas_db.commit()
personas_db.close()
