import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()


categories = ['Business_MGMT', 'DatabaseMGMT', 'Business_Stats', 'Marketing', 'Business_App_Development']

for category in categories:
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {category.replace(" ", "_")} (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                    )''')


conn.commit()
conn.close()