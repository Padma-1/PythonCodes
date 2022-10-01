##SAMPLE INPUT 
##1
##5
##1 2 3 3 2
##SAMPLE OUTPUT 
##4
##Explanation
##The elements which occur in the array are 1,2,3.
##
##Let us consider 1 it has only one occurence so answer for 1 is 0.
##
##Let us consider 2 it has two occurence at 2 and 5 so |5-2|=3
##
##Let us consider 3 it has two occurence at 3 and 4 so |4-3|=1.
##
##So total sum=0+3+1=4.
##
##If there are more than two occrence we only need to consider the first and last.
"""TLE
t=int(input())
for i in range(t):
    x=int(input())
    arr=list(map(int,input().split()))
    sum1=0
    arr2=set(arr)
    for j in arr2:
        if arr.count(j)>1:
            arr1=[]
            for i in range(0,len(arr)):
                if j==arr[i]:
                    arr1.append(i+1)
            sum1+=((arr1[-1]-arr1[0]))
    print(sum1)
 
"""TLE
"""def res():
    arr1=arr[ ::-1]
    arr2=set(arr)
    d={}
    s=0
    for i in arr2:
        d[i]=[arr.index(i)+1,x-arr1.index(i)]
        s+=(d[i][1]-d[i][0])
    return s
   

t=int(input())
for i in range(t):
    x=int(input())
    arr=list(map(int,input().split()))
    print(res())
"""
##GOOD CODE:)
t=int(input())
for i in range(t):
    x=int(input())
    c=0
    arr=list(map(int,input().split()))
    d={}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]]=[]
            d[arr[i]].append(i+1)
            
        else:
            d[arr[i]].append(i+1)
    for i in d.keys():
        c+=d[i][-1]-d[i][0]
    print(c)
        
            


