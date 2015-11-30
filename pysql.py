from django.shortcuts import render_to_response
import pymysql

db = pymysql.connect(user='root',db='django_test',passwd='121212',host='localhost',port=4580)
cursor = db.cursor()
cursor.execute('select name from books order by name')
name = [row[0] for row in cursor.fetchall()]
db.close
print (name)

