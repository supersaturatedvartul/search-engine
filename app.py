content =  ["Python is an multi-paradigm Language. It is used in Machine Learning.","Java is Object-oriented Language used in large enterprise level apps.","JavaScript is language used to operate on web browser to create web apps and websites.","C is Procedural Language that uses functions to implement specific tasks.","Matplotlib is Python Library used for Data Visualization.","Numpy is Python Library used for performing complex mathematical operations, it allows to used multidimensional arrays.","SpringBoot is Java Framework used in Web Development.","Node.js is a engine that allows user to run JS outside the browser."]

a = input("Enter the Language you want to search about:")
a = a.lower()
results = []
for i in content:
    if a in i.lower():
        results.append(i)

if len(results) == 0:
        print(f"No results found for {a.capitalize()}")
else:
    for j in range(0,len(results)):
            print(results[j])
    
