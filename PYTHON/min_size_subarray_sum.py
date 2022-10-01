##Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
##
##Example: 
##
##Input: s = 7, nums = [2,3,1,2,4,3]
##Output: 2
##Explanation: the subarray [4,3] has the minimal length under the problem constraint.
##
##
s=7
nums=[2,3,1,2,4,3]#[1,2,3,2,5,6]
n=len(nums)
c_s=0
i=0
a=[]
for j in range(0,n):
    c_s+=nums[j]
    while(c_s>=s):
        a.append(len(nums[i:j+1]))
        c_s-=nums[i]
        i+=1
if a==[]:
    return 0
else:
    return 0



