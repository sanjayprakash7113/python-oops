a = [1, 3, 2, 1, 4, 1, 3, 3, 3]

freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_key = None
max_val = 0

for k in freq:
    if freq[k] > max_val:
        max_val = freq[k]
        max_key = k

print(max_key)


d = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
b={}
for i in d:
    if d[i]>=10:
        b[i]=d[i]
print(b)

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 25}
b={}
for i in d1:
    b[i]=d1[i]
for i in d2:
    if i in b:
        b[i]=b[i]+d2[i]
    else:
        b[i]=d2[i]
print(b)

s = "programming"
b={}
for i in  s:
    if i in b:
        print(i)
        break
    else:
        b[i]=1

s = "hello world"
a="aeiou"
b={}
c={}
for i in s:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
for i in b:
    if i in a:
        c[i]=b[i]
        i=c
print(c)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b={}
for i in a:
    c=i%3
    if c not in b:
        b[c]=[]
    b[c].append(i)
print(b)

a = [1, 2, 3, 2, 4, 1, 5, 1]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print(list(set(c)))
