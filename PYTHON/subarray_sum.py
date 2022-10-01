#find subarray of anylength whose sum is key..and those elements must be in continous manner
#1 4 0 0 3 6
#7
#o/p:-->1 4
"""l = list(map(int,input().split()))
key=int(input())
temp=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if sum(l[i:j+1])==key:
            print(i,j)
            temp=1
    if temp==1:#to break for loop
        break
else:
    print("not found")"""

l=list(map(int,input().split()))
key = int(input())
cur_sum=l[0]
i=0
for j in range(1,len(l)):
    while(cur_sum>key and i<j-1):#until i crosses j
        cur_sum-=l[i]
        i+=1
    if cur_sum==key:
        print(i,j-1)
        break
    if cur_sum<key:
        cur_sum+=l[j]
else:
    print("not found")
        
