a = [1, 2, 2, 3, 1, 4, 2]
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(b)


d = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
a=0
b=0
for i in d:
    if d[i]>a:
        a=d[i]
        b=i
print(b)

s = "programming"
a={}
for i in s:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
print(a)

s = "swiss"
a={}
for i in s:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1

for i in a:
    if a[i]==1:
        print(i)
        break


d = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
a=[]
for i in d:
    if d[i]%2==0:
        a.append(i)
print(a)


d={"a":1,"b":2,"c":1}
a={}
for i in d:
    v=d[i]
    if v not in a:
        a[v]=[]
        a[v].append(i)
print(a)



        





