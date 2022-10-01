##2 11 5 7
##9
##[0, 3]
nums=list(map(int,input().split()))
target=int(input())
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j])==target:
          print([i,j])
