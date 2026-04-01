content =  ["Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.",
            "Java is a high-level, general-purpose, memory-safe, object-oriented programming language. It is intended to let programmers write once, run anywhere (WORA), meaning that compiled Java code can run on all platforms that support Java without the need to recompile. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them. ",
            "JavaScript (JS) is a programming language and core technology of the Web, alongside HTML and CSS. It was created by Brendan Eich in 1995. As of 2025, the overwhelming majority of websites (98.9%) uses JavaScript for client side webpage behavior.",
            "C is a general-purpose programming language created in the 1970s by Dennis Ritchie. By design, C gives the programmer relatively direct access to the features of the typical CPU architecture, customized for the target instruction set. It has been and continues to be used to implement operating systems (especially kernels), device drivers, and protocol stacks, but its use in application software has been decreasing. C is used on computers that range from the largest supercomputers to the smallest microcontrollers and embedded systems.",
            "Matplotlib (portmanteau of MATLAB, plot, and library) is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural 'pylab' interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.",
            "NumPy (pronounced NUM-py) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The predecessor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers.",
            "Spring Boot is an open-source Java framework used for programming standalone, production-grade Spring-based applications with a bundle of libraries that make project startup and management easier. Spring Boot is a convention-over-configuration extension for the Spring Java platform intended to help minimize configuration concerns while creating Spring-based applications.",
            "Node.js is a cross-platform, open-source JavaScript runtime environment that can run on Windows, Linux, Unix, macOS, and more. Node.js runs on the V8 JavaScript engine, and executes JavaScript code outside a web browser. According to the Stack Overflow Developer Survey, Node.js is one of the most commonly used web technologies."]

a = input("Enter the Language you want to search about:")
a = a.lower()
results = []
for i in content:
    if a in i.lower():
        wordcount = i.lower().count(a)
        results.append((i,wordcount))

results.sort(key= lambda x: x[1],reverse=True)
if len(results) == 0:
        print(f"No results found for {a.capitalize()}")
else:
    for j in range(0,len(results)):
            print(f"\n{results[j][0]}, Word Count:{results[j][1]}")
    
