import webbrowser
try: 
    from googlesearch import search 
except ImportError:  
            print("No module named 'google' found") 
l = []
query = "dwa"
i = 1
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(str(i) + "\t" + j) 
    print(str(j))
    l.append(j)
    i+=1
print("Which website do you want to see. Speak the no")
no_str = {
            "first" : 1,
            "second" : 2,
            "third"  : 3,
            "fourth" : 4,
            "fifth" : 5,
            "sixth" : 6,
            "seventh" : 7,
            "eight"  : 8,
            "ninth"  : 9,
            "tenth"  : 10,
}
awd = input()
final = no_str[awd]
webbrowser.open_new_tab(l[final])
