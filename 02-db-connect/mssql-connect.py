#pip install pyodbc
#pip install pymssql
#pip list
import pymssql 
conn = pymssql.connect(server='(localdb)\MSSQLLocalDB',database='EFDB')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Products')

for row in cursor:
    print('row = %r' % (row,))