import sqlite3 #open-source sample DB (Other DBs have there own package)

#Define connection with DB
connection = sqlite3.connect('E:\\pythontest.db')

#Define cursor object
cursor = connection.cursor()

#SQL queries for table creation
sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'

sql2 = '''
CREATE TABLE EMPLOYEE (
EMPID INT(6) NOT NULL,
NAME CHAR(20) NOT NULL,
AGE INT,
SEX CHAR(1),
INCOME FLOAT)
'''

#Execute table creation queries
cursor.execute(sql1)
cursor.execute(sql2)

#Insert Data into table
rec = (123456,'sourav',29,'M',10000)
sql3 = '''
INSERT INTO EMPLOYEE VALUES (?,?,?,?,?)
'''

try:
	cursor.execute(sql3, rec)
	connection.commit()
except Exception as e:
	print('Error : ', str(e))
	connection.rollback()

connection.close()
