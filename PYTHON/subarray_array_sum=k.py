##Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
##
## 
##
##Example 1:
##
##Input: nums = [1,1,1], k = 2
##Output: 2
##Example 2:
##
##Input: nums = [1,2,3], k = 3
##Output: 2

nums=[4,-2,-1,1,-2,3,-3]
n=len(nums)
k=2
c=0
p_s=[0]*n
p_s[0]=nums[0]
for i in range(1,n):
    p_s[i]=p_s[i-1]+nums[i]
d={0:1}
for i in range(n):
    if p_s[i]-k in d:
        c+=d[p_s[i]-k]
    if p_s[i] in d:
        d[p_s[i]]+=1
    else:
        d[p_s[i]]=1
print(d)
        
