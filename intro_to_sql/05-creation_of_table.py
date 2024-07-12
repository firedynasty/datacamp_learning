import pandas as pd
import sqlite3

# Create DataFrame for patrons
patrons_data = {
    'card_num': [54378, 94722, 45783, 90123],
    'name': ['Izzy', 'Maham', 'Jasmin', 'James'],
    'member_year': [2012, 2020, 2022, 1989],
    'total_fine': [9.86, 0, 2.05, 0]
}

patrons_df = pd.DataFrame(patrons_data)

# Create DataFrame for checkouts
checkouts_data = {
    'id': [567, 568, 569, 570],
    'start_date': ['2022-05-13', '2022-06-10', '2022-06-27', '2022-08-14'],
    'due_date': ['2022-05-27', '2022-06-24', '2022-07-11', '2022-08-28'],
    'card_num': [54378, 54378, 45783, 90123],
    'book_id': [638, 322, 156, 912]
}

checkouts_df = pd.DataFrame(checkouts_data)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('library.db')

# Convert DataFrames to SQLite tables
patrons_df.to_sql('patrons', conn, if_exists='replace', index=False)
checkouts_df.to_sql('checkouts', conn, if_exists='replace', index=False)

# Verify the data by querying the tables
cursor = conn.cursor()
print("Patrons Table:")
cursor.execute('SELECT * FROM patrons')
for row in cursor.fetchall():
    print(row)

print("\nCheckouts Table:")
cursor.execute('SELECT * FROM checkouts')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()

import pandas as pd
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('library.db')



# Data for the books DataFrame
books_data = {
    'id': [638, 912, 322, 156],
    'title': ['Being Mortal', 'Educated', 'Night', 'Where the Wild Things Are'],
    'author': ['Atul Gawande', 'Tara Westover', 'Elie Wiesel', 'Maurice Sendak'],
    'genre': ['Non-Fiction', 'Non-Fiction', 'Non-Fiction', 'Childrens'],
    'pub_year': [2015, 2018, 1956, 1963]
}

# Creating the books DataFrame
books_df = pd.DataFrame(books_data)
books_df.to_sql('books', conn, if_exists='replace', index=False)

# Verify the data by querying the tables
cursor = conn.cursor()
print("Books Table:")
cursor.execute('SELECT * FROM books')

# Step 6: Get the field names
field_names = [description[0] for description in cursor.description]

# Step 7: Print the field names
print("Field names:", field_names)

for row in cursor.fetchall():
    print(row)
    
# Close the connection
conn.close()


