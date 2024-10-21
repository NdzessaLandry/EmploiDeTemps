import psycopg2 as ps

conn=ps.connect(
	database="postgres",
	user="postgres",
	password="40503",
    port="5432",
    host='localhost')

cur=conn.cursor()
cur.execute('CREATE DATABASE LTBM;')

conn.close()
