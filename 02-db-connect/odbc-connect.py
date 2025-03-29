#pip install pyodbc
#pip install pymssql
#pip list
import pyodbc 
conn_str = (
    r'DRIVER={ODBC Driver 18 for SQL Server};'
    r'SERVER=(localdb)\MSSQLLocalDB;'
    r'DATABASE=EFDB;'
    r'Trusted_Connection=yes;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute('SELECT * FROM Products')
''' commented code
for row in cursor:
    print('row = %r' % (row,))
'''
records = cursor.fetchall()
for r in records:
    print(f"{r.Id}\t{r.Name}\t{r.Description}")