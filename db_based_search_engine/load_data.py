from db import connection

conn = connection()

cursor = conn.cursor()
liblist = ['c.txt','java.txt','python.txt']

for i in liblist:
    with open(f'library/{i}','r') as file:
        content = file.readlines()
    for j in content:
        j = j.strip()
        if j:
            if len(j.split())>15:
                cursor.execute("INSERT into contentable (content) VALUES (%s)",(j.lower(),))
conn.commit()