from db import connection

search = input("What's in your Mind:")

search = search.lower()

conn = connection()

cursor = conn.cursor()

cursor.execute("SELECT content FROM contentable where content like %s",(f"%{search}%",))

retrieval = cursor.fetchall()

result = []

for i in retrieval:
    wordcount = i[0].count(search)
    result.append((i[0],wordcount))

result.sort(key=lambda x:x[1],reverse=True)

if len(result) == 0:
    print(f"No Results found for {search.capitalize()}")
else:
    for j in result:
        print(f'{j[0].capitalize()}, [Score:{j[1]}]')
        print('\n')


