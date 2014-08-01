from views import db
from datetime import datetime
from config import DATABASE_PATH
import sqlite3

with sqlite3.connect(DATABASE_PATH) as conn:
	c = conn.cursor()
	# temporarilt change name of ftasks table
	c.execute("""ALTER TABLE ftasks RENAME TO old_ftasks""")
	
	# recreate a new ftasks table with updated schema
	db.create_all()

	# retrieve data from old_ftasks table
	c.execute("""SELECT name, due_date, priority, status
			FROM old_ftasks ORDER BY task_id ASC""")

	# save all rows as list of tuples
	# set posted date to today and user_id to 1
	data = [(row[0], row[1], row[2], row[3], datetime.now(),1) for row in c.fetchall()]

	# insert data to new ftasks table
	c.executemany("""INSERT INTO ftasks (name, due_date, priority, 
				status, posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?)""", data)

	#delete old ftasks table
	c.execute("DROP TABLE old_ftasks")