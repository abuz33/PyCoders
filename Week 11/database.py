import psycopg2

conn = psycopg2.connect("dbname=dvdrental user=postgres password=Asude1608.")
cur = conn.cursor()
command = '''Select * from actor'''
# create a table
result = cur.execute(command)
# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

print(result)
