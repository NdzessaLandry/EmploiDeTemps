import psycopg2 as pg

conn=pg.connect(database='projetlycee',password='40503',user='postgres',port="5432",host='localhost')

cur=conn.cursor()
cur.execute(""" select  from classe""")
print(cur.fetchall())
cur.close()
conn.close()