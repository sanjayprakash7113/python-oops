a = [10, 15, 22, 37, 40]
b={}
for i in a:
    if i%2==0:
        b[i]="even"
    else:
        b[i]="odd"
print(b)



    
a = [1, 2, 3, 4]
b={}
for i in a:
    if i in b:
        b[i]=i
    else:
        b[i]=i+i
print(b)

a = [2, 3, 4, 5]
b={}
for i in a:
    b[i]=i*i
print(b)

a = ["apple", "cat", "banana", "dog"]
b={}
for i in a:
    b[i]=len(i)
print(b)

a = [7, 8, 9, 10]
b={}
for i in a:
    if i%2==0:
        b[i]="even"
    else:
        b[i]="odd"
print(b)
    

a = [2, 3, 4, 5, 6, 7, 8, 9]
b = {}

for i in a:
    if i < 2:
        b[i] = False
        continue
    is_prime = True
    for n in range(2, int(i**0.5) + 1):
        if i % n == 0:
            is_prime = False
            break
    b[i] = is_prime

print(b)



a = [11, 12, 15, 20, 7]
b={}
for i in a:
    if i%2==0:
        b[i]=True
    else:
        b[i]=False
print(b)
















