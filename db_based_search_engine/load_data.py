from db import connection

conn = connection()

cursor = conn.cursor()
with open('webpage.txt','r') as file:
    content = file.readlines()
for i in content:
    i = i.strip()
    if i:
        cursor.execute("INSERT into contentable (content) VALUES (%s)",(i.lower(),))
conn.commit()
conn.close()
