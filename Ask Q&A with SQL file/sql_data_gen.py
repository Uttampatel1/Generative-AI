import sqlite3
from faker import Faker

# Connect to the database (replace 'your_database.db' with the actual name of your database file)
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# Create a Faker instance
fake = Faker()

# Create a new table named STUDENT_NEW
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT_NEW (
        Name TEXT,
        Department TEXT,
        Grade TEXT,
        Marks INTEGER
    )
''')

# Insert dummy data into the STUDENT_NEW table
for _ in range(50):  # Adjust the range to generate more or fewer rows
    name = fake.name()
    department = fake.random_element(elements=('Data Science', 'DEVOPS',"web devloper","LLMs","Apps","Designer"))
    grade = fake.random_element(elements=('A', 'B', 'C'))
    marks = fake.random_int(min=0, max=100)

    # Insert the generated data into the new table
    cursor.execute("INSERT INTO STUDENT_NEW VALUES (?, ?, ?, ?)", (name, department, grade, marks))


print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT_NEW''')
for row in data:
    print(row)

# Commit the changes and close the connection
connection.commit()
connection.close()


# from dotenv import load_dotenv
# load_dotenv()

# import sqlite3

# ## conect sqllite3 database
# connection = sqlite3.connect("student.db")


# cursor=connection.cursor()

# ## create the table
# table_info="""
# Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
# SECTION VARCHAR(25),MARKS INT);

# """

# cursor.execute(table_info)

# ## Insert Some more records

# cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
# cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
# cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
# cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
# cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

# ## Disspaly ALl the records

# print("The isnerted records are")
# data=cursor.execute('''Select * from STUDENT''')
# for row in data:
#     print(row)

# ## Commit your changes int he databse
# connection.commit()
# connection.close()

