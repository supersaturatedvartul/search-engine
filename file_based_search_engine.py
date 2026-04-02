file = open('webpage.txt','r')
content = file.readlines()

print("*--------------------------------------------*")
a = input("What do you want to search?:")
a = a.lower()

results = []

for i in content:
        if a in i.lower():
             wordcount = i.lower().count(a)
             results.append((i,wordcount))

results.sort(key= lambda x:x[1],reverse=True)

if len(results) == 0:
    print(f"No Results found for {a.capitalize()}")
else:
    for j in results:
        print(f'{j[0]},({j[1]})')
print("*-----------------------------*")
        

file.close()