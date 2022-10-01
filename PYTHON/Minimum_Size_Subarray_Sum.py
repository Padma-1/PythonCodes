#finding minimum length of contigous subarray of sum1>=s.
nums=list(map(int,input().split()))#[2,3,1,2,4,3]
s=int(input())#7
i=0
cur_sum=0
z=[]
for j in range(0,len(nums)):
       cur_sum+=nums[j]
       while (cur_sum>=s):
              z.append(len(nums[i:j+1]))#[[2, 3, 1, 2], [3, 1, 2, 4], [1, 2, 4], [2, 4, 3], [4, 3]]--->length are [4, 4, 3, 3, 2]
              cur_sum-=nums[i]
              i+=1
print(min(z))#to print minimum sub array length--[4,3] is minimum subarray having length 2.
