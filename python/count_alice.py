from fileinput import close

file=open("Alice.txt","r")

words=file.read()

words=words.split()

count={}

for word in words:
    count[word]=words.count(word)

finalcount=sorted(count.items(),key=lambda x:(-x[1],x[0]))

ans=str(finalcount[:1])

print(ans[2:-2].replace(',',""))

file.close()