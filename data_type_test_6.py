nums = [2, 2, 1, 1, 1, 2, 2]

le=0
count=None

for i in nums:
    if le==0:
        count=i
    if i==count:
        le+=1
    else:
        le-=1
print(count)


nums = [100, 4, 200, 1, 3, 2]
s=set(nums)
lon=0
for i in s:
    if i-1 not in s:
        current=i
        l=1
        while current+1 in s:
            current+=1
            l+=1
        lon=max(lon,l)
print(lon) 



nums = [9, 4, 9, 6, 7, 4]
b={}
for i in nums:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for k,v in b.items():
    if v==1:
        print(k)



        

nums = [1, 2, 3, 4]
n = len(nums)

res = [1] * n

# left products
left = 1
for i in range(n):
    res[i] = left
    left *= nums[i]

# right products
right = 1
for i in range(n-1, -1, -1):
    res[i] *= right
    right *= nums[i]

print(res)

       
nums = [3, 0, 1]
nums.sort()
i=0
for j in nums:
    if j==i:
        i=i+1
    else:
        print(i)
        break
        







