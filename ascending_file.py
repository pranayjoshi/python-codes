def FileSort(filew):
    s = []
    with open(filew, "r") as fd:
        for line in fd:
            line = line.replace("\r", "").replace("\n", "")
            s.append(line)
    s.sort()
    return s
k = FileSort("file.txt")
f=open('f1.txt','w')
for ele in k:
    f.write(ele+'\n')

f.close()
