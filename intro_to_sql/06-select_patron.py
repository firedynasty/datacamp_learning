import sqlite3

# Step 2: Connect to SQLite database named 'library.db'
conn = sqlite3.connect('library.db')

# Step 3: Create a cursor object
cursor = conn.cursor()

# Step 4: Execute the query to select all data from the 'patrons' table
cursor.execute('SELECT * FROM patrons')

# Step 5: Fetch all rows from the executed query
rows = cursor.fetchall()

# Step 6: Get the field names
field_names = [description[0] for description in cursor.description]

# Step 7: Print the field names
print("Field names:", field_names)

# Step 8: Print the fetched rows
for row in rows:
    print(row)

# Step 9: Close the connection
conn.close()

