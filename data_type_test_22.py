nums = [2, 1, 5, 1, 3, 2]
k = 3   
b=0    
for i in range(len(nums)-k+1):
    s=0
    for j in range(i,k+i):
        s=s+nums[j]
        if b<s:
            b=s
print(b)



nums = [2, 1, 5, 1, 3, 2]
K = 7

l=0
c=0
max_l=0

for i in range(len(nums)):
    c+=nums[i]
    while c>k:
        c-=nums[l]
        l+=1
    max_l=max(max_l,i-l+1)
print(max_l)
