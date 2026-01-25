a = [1, 2, 3, 4, 5]
b={}
for i in a:
    if i%2!=0:
        b[i]=i*i
    else:
        continue
print(b)


a = [12, 34, 5, 210]
b={}
for i in a:
    b[i]=int(str(i)[::-1])
print(b)

a = [12, 3, 21, 5]
b={}
for i in a:
    s=0
    for j in str(i):
        s+=int(j)**2
        b[i]=s
print(b)


a = [12, 34, 5, 210]
b={}
for i in a:
    s=1
    for j in str(i):
        s=s*int(j)
        b[i]=s
print(b)
