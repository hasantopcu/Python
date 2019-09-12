import pyodbc

mydb = pyodbc.connect('Driver={};'
                      'Server=;'
                      'Database=;'
                      'Trusted_Connection=yes;')


def getData():
  mycursor = mydb.cursor()
  mycursor.execute("Select column_name(s) from table_name ")
  result = mycursor.fetchall()
  columns =  []
  for column in mycursor.description:
    columns.append(column[0])
  dict_result = []
  for row in result:
    dict_result.append(dict(zip(columns , row)))   
  
if __name__ == "__main__":
  getData()
