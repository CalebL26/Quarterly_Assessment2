import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Define a function to add data to a table
def add_data_DatabaseMGMT(question,answer):
        cursor.execute(f'''INSERT INTO DatabaseMGMT (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

add_data_DatabaseMGMT("What is a database?", "A) A collection of files", "B) A collection of data", "C) A network of computers", "D) None of the above", "B) A collection of data")
add_data_DatabaseMGMT("What is SQL?", "A) A programming language", "B) A database management system", "C) A networking protocol", "D) None of the above", "A) A programming language")
add_data_DatabaseMGMT("What is a table?", "A) A database schema", "B) A grid of data", "C) A database index", "D) None of the above", "B) A grid of data")
add_data_DatabaseMGMT("What is a primary key?", "A) A unique identifier", "B) A common field", "C) A data type", "D) None of the above", "A) A unique identifier")
add_data_DatabaseMGMT("What is normalization?", "A) Making data consistent", "B) Reducing redundancy", "C) Organizing data", "D) None of the above", "B) Reducing redundancy")
add_data_DatabaseMGMT("What is a query?", "A) A question", "B) A database object", "C) A search result", "D) None of the above", "A) A question")
add_data_DatabaseMGMT("What is data integrity?", "A) Keeping data secure", "B) Ensuring data consistency", "C) Managing data access", "D) None of the above", "B) Ensuring data consistency")
add_data_DatabaseMGMT("What is a transaction?", "A) A database operation", "B) A network connection", "C) A data type", "D) None of the above", "A) A database operation")
add_data_DatabaseMGMT("What is a view?", "A) A stored query", "B) A database administrator", "C) A database table", "D) None of the above", "A) A stored query")
add_data_DatabaseMGMT("What is data mining?", "A) Extracting data", "B) Analyzing data", "C) Storing data", "D) None of the above", "B) Analyzing data")


def add_data_bmgt(question,answer):
        cursor.execute(f'''INSERT INTO Business_Data_MGMT (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

add_data_bmgt("Which of the following is not an example of DBMS?", "A) MySQL B) Google C) Microsoft Access", "B")
add_data_bmgt("What is a database?", "A) Organized collection of data that cannot be updated B) Organized collection of data or information that can be accessed, updated, and managed C) Collection of data or information without organizing", "B")
add_data_bmgt("What is DBMS?", "A) A collection of queries B) DBMS stores, modifies, and retrieves data C) DBMS is a programming language", "B")
add_data_bmgt("Which of the following is a feature of the database?", "A) Lack of authentication B) User interface provided C) Store data in multiple locations", "B")
add_data_bmgt("What is the full form of DBMS?", "A) Data of Binary Management System B) Database Management System C) Database Management Service", "B")
add_data_bmgt("Which type of data can be stored in the database?", "A) Image oriented data B) All of the above C) Text, files containing data", "B")
add_data_bmgt("Which of the following is not a feature of DBMS?", "A) High level of security B) Single-user access only C) Support ACID Property", "B")
add_data_bmgt("Who created the first DBMS?", "A) Edgar Frank Codd B) Charles Bachman C) Charles Babbage", "B")
add_data_bmgt("In which of the following formats data is stored in the DBMS?", "A) Image B) Table C) Graph", "B")
add_data_bmgt("Which of the following is not a type of database?", "A) Hierarchical B) Decentralized C) Network", "B")


def add_data_BStats(question,answer):
        cursor.execute(f'''INSERT INTO Business Stats (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

add_data_BStats("What is statistics?", "A) A branch of mathematics", "B) A data analysis technique", "C) A probability theory", "D) None of the above", "A) A branch of mathematics"),
add_data_BStats("What is a population?", "A) A group of individuals", "B) A sample", "C) A statistical measure", "D) None of the above", "A) A group of individuals"),
add_data_BStats("What is a sample?", "A) A population", "B) A group of individuals", "C) A subset of a population", "D) None of the above", "C) A subset of a population"),
add_data_BStats("What is central tendency?", "A) A statistical measure", "B) A data distribution", "C) A probability theory", "D) None of the above", "A) A statistical measure"),
add_data_BStats("What is dispersion?", "A) The spread of data", "B) The center of data", "C) The shape of data", "D) None of the above", "A) The spread of data"),
add_data_BStats("What is correlation?", "A) A causal relationship", "B) A measure of association", "C) A statistical measure", "D) None of the above", "B) A measure of association"),
add_data_BStats("What is regression?", "A) A data analysis technique", "B) A statistical measure", "C) A probability theory", "D) None of the above", "A) A data analysis technique"),
add_data_BStats("What is probability?", "A) The likelihood of an event", "B) A statistical measure", "C) A sample space", "D) None of the above", "A) The likelihood of an event"),
add_data_BStats("What is hypothesis testing?", "A) A statistical inference", "B) A data analysis technique", "C) A probability theory", "D) None of the above", "A) A statistical inference"),
add_data_BStats("What is a confidence interval?", "A) A range of values", "B) A statistical measure", "C) A probability theory", "D) None of the above", "A) A range of values")


def add_data_Mkt(question,answer):
        cursor.execute(f'''INSERT INTO Marketing (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")
        
add_data_Mkt("What is marketing?", "A) Selling products", "B) Promoting products", "C) Managing finances", "D) None of the above", "B) Promoting products"),
add_data_Mkt("What is a target market?", "A) A market with many competitors", "B) A group of consumers with similar needs", "C) A market with high demand", "D) None of the above", "B) A group of consumers with similar needs"),
add_data_Mkt("What is the marketing mix?", "A) A blend of marketing strategies", "B) A mix of marketing tools", "C) The 4 Ps: Product, Price, Place, Promotion", "D) None of the above", "C) The 4 Ps: Product, Price, Place, Promotion"),
add_data_Mkt("What is branding?", "A) Creating a logo", "B) Creating a unique name and image for a product", "C) Advertising products", "D) None of the above", "B) Creating a unique name and image for a product"),
add_data_Mkt("What is market segmentation?", "A) Selling products in different markets", "B) Dividing the market into smaller segments", "C) Analyzing market trends", "D) None of the above", "B) Dividing the market into smaller segments"),
add_data_Mkt("What is the purpose of a marketing plan?", "A) To outline business objectives and strategies", "B) To manage finances", "C) To design product logos", "D) None of the above", "A) To outline business objectives and strategies"),
add_data_Mkt("What is the role of market research?", "A) To create advertising campaigns", "B) To analyze consumer behavior", "C) To manage inventory", "D) None of the above", "B) To analyze consumer behavior"),
add_data_Mkt("What is the difference between advertising and public relations?", "A) Advertising is paid, PR is free", "B) Advertising focuses on selling, PR focuses on relationships", "C) Advertising is offline, PR is online", "D) None of the above", "B) Advertising focuses on selling, PR focuses on relationships"),
add_data_Mkt("What is a product?", "A) A tangible item", "B) An intangible item", "C) A service", "D) None of the above", "A) A tangible item"),
add_data_Mkt("What is a marketing channel?", "A) A social media platform", "B) A distribution path", "C) A product feature", "D) None of the above", "B) A distribution path")


def add_data_AppDevelop(question,answer):
        cursor.execute(f'''INSERT INTO Business_App_Development (question, answer) VALUES (?, ?)''', (question, answer))
        conn.commit()
        print("data added")

add_data_AppDevelop("What is the primary purpose of a while loop in programming?", "A) To execute a block of code a specific number of times", "B) To repeat a block of code until a certain condition is no longer true", "C) To perform mathematical calculations efficiently", "B")
add_data_AppDevelop("What is the main function of a for loop in programming?", "A) To execute a block of code repeatedly until a certain condition is met", "B) To iterate over a sequence and perform an action on each item", "C) To define a set of instructions to perform a task", "B")
add_data_AppDevelop("What is the primary purpose of defining functions?", "A) To execute a block of code repeatedly until a certain condition is met", "B) To organize code into reusable modules for easier readability", "C) To perform mathematical calculations on numeric datasets", "B")
add_data_AppDevelop("What are booleans?", "A) Booleans are data types used to represent numeric values", "B) Booleans are data types that represent true or false values", "C) Booleans are used to perform arithmetic operations in programming", "B")
add_data_AppDevelop("What does sequencing refer to in programming?", "A) Organizing data into structured formats like arrays and lists", "B) Arranging code statements in a specific order to execute tasks step by step", "C) Determining the flow of control within conditional statements", "B")
add_data_AppDevelop("What is the primary purpose of dictionaries in programming?", "A) Storing and organizing data in a sequential manner", "B) Mapping keys to corresponding values for efficient retrieval", "C) Performing mathematical operations on numeric datasets", "B")
add_data_AppDevelop("Name of the screen that recognizes touch input is?", "A) Digital screen", "B) Touch screen", "C) Point screen", "B")
add_data_AppDevelop("Which of these stores more data than a DVD?", "A) CD Rom", "B) Blue Ray disk", "C) Floppy disk", "B")
add_data_AppDevelop("What do functions do?", "A) Functions manipulate data within a program", "B) Functions define a set of instructions to perform a specific task", "C) Functions create graphical interfaces for user interaction", "B")
add_data_AppDevelop("What is the primary goal of prompt engineering?", "A) To design user-friendly interfaces for software applications", "B) To create clear instructions for achieving desired outcomes", "C) To optimize the efficiency of algorithms and data structures", "B")
