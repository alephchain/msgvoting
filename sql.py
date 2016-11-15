import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=sql.steemsql.com;'
                                'Database=DBSteem;'
                                'uid=steemit;pwd=steemit')
cursor = connection.cursor()
SQLCommand = "SELECT author, title, body FROM TxComments WHERE CONTAINS(body, '@arcange')"
cursor.execute(SQLCommand)
# do whatever you want with the retrieved data
connection.close()