
import sqlite3

#def drop_all_tables(database_file)


conn = sqlite3.connect('quiz_bowl.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create students table
cursor.execute('''CREATE TABLE IF NOT EXISTS DatabaseMGMT (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business_MGMT (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business_Stats (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Marketing (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Business_App_Development (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')



