import mysql.connector

with open("usuarios.sql") as U:
    sql = U.read()

conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="Root123!" 
)
cursor = conn.cursor()

for statement in sql.split(";"):
    if statement.strip():
        print(statement)
        cursor.execute(statement)
        conn.commit()
        print("statement executed")

cursor.close()
conn.close()