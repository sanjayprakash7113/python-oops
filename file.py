f=open("data.py","w")
f.write("hello world")
f.close()


f=open("data.py","r")
print(f.read())
f.close()

f=open("data.py","a")
f.write("\nthis is new line")
f.close()

with open("data.py","r") as f:
    print(f.read())

with open("data.py","r") as f:
    data=f.read()
    b=data.split()
    print(len(b))
c=0
with open("data.py","r") as f:
    for i in f:
        word=i.split()
        for j in word:
            if j=="world":
                c=c+1
print(c)

