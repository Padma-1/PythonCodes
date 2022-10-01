##8 1 2 2 3
##[4, 0, 1, 1, 3]
##finding how many numbers are smaller than given number
#method 1
"""nums=list(map(int,input().split()))
l=[]
for i in range(len(nums)):
       c=0
       for j in range(len(nums)):
           if nums[i]>nums[j]:
               c+=1
       l.append(c)
print(l)"""
               
#To reduce the time complexity(method 2)
nums=list(map(int,input().split()))
arr=sorted(nums)#[1, 2, 2, 3, 8]
d={}
count=0
for i in range(len(nums)):
       if arr[i] not in d:
              d[arr[i]]=count#{1: 0, 2: 1, 3: 3, 8: 4}
              count+=1
       else:#for repeated elements
              count+=1
for i in range(len(nums)):
       nums[i]=d[nums[i]]
print(nums)#[4, 0, 1, 1, 3]
