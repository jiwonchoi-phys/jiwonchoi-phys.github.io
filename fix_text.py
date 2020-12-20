import os

location = os.getcwd()+"/_posts"
os.chdir(location)
print(location)
file = "2020-12-20-cmft-1-1.md"
texts = []

with open(file,'r+') as f:
    for line in open(file):
        print(line)
        line = line.replace("rarr", "rightarrow")
        line = line.replace("bold","mathbf")
        line = line.replace("dag","dagger")
        line = line.replace("infin","infty")
        line = line.replace("isin","in")
        line = line.replace("|","\middle|")
        print("->",line)
        texts.append(line)

for i in range(len(texts)):
    print(texts[i])

newfile = open('modified.md','w')
for i in range(len(texts)):
    newfile.write(str(texts[i]))
    print(texts[i])

newfile.close()
'''
new = open(,'w')
for i in range(len(texts)):
    f.write(texts[i])
new.close()
'''