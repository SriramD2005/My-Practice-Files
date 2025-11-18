import pymysql as pys
try:
    connection = pys.connect(host="localhost",user = 'root', password='sriram2005',database="myfirstdatabase")
    cursor = connection.cursor()
    cursor.execute("use myfirstdatabase;")
except Exception as e:
    print(e)