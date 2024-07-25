"""
Module to practice with mySQL DELETE statements

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
# Delete a row in the table
# Create the SQL sentence
sql_sentence = 'DELETE FROM personas WHERE id = %s'
# Create the values to delete
values = 3
cursor.execute(sql_sentence, (values,))
# Commit the changes to the database
personas_db.commit()
print('Row deleted successfully')
personas_db.close()

