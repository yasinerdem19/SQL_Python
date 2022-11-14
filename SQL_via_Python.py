#SQL via python
from dbmodule import connect
#create connection obj
Connection=connect('dbname','username','psw')
#create cursor
Cursor=Connection.cursor()
#run
Cursor.execute('select * from table')
Results=cursor.fetchall()
