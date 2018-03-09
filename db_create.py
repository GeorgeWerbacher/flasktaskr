# project/db_create.py
import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	# Get a cursor object used to execute SQL commands
	c = connection.cursor()

	# Create the Table
	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
		status INTEGER NOT NULL)""")

	# Insert Dummy Data into the table
	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status)'
		'VALUES("Finish this tutorial", "3/25/2018", 10, 1)'
		)
	