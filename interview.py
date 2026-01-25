a=1234
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
print(b)


a="python"
b=""
for i in a:
    b=i+b
print(b)
    
a= [1, 2, 2, 3, 4, 3]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

a=1221
temp=a
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
if b==temp:
    print("palindrom")
else:
    print("not palindrom")

a="education"
b="aeiouAEIOU"
c=0
for i in a:
    if i in b:
        c=c+1
print(c)



a= [10, 5, 20, 8]
b=0
c=a[0]
for i in a:
    if i>c:
        b=c
        c=i
    else:
        if b<i and c!=i:
            b=i
print(b)


a="banana"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
        




