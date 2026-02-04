nums = [0, 1, 0, 3, 12]
pos=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[pos]=nums[i]
        pos+=1
for j in range(pos,len(nums)):
    nums[j]=0
print(nums)


p= [7, 1, 5, 3, 6, 4]
profit=[]
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]<p[j]:
            profit.append(p[j]-p[i])
print(max(profit))


current=p[0]
max_pri=0
for i in p:
    if i<current:
        current=i
    else:
        max_pri=max(max_pri,i-current)
print(max_pri)


nums = [-2,1,-3,4,-1,2,1,-5,4]
p=nums[0]
for i in range(len(nums)):
    s=0
    for j in range(i,len(nums)):
        s=s+nums[j]
        if s>p:
            p=s
print(p)



nums = [-2,1,-3,4,-1,2,1,-5,4]
a=nums[0]
cur=nums[0]

for i in range(1,len(nums)):
    cur=max(nums[i],cur+nums[i])
    a=max(a,cur)
print(a)



