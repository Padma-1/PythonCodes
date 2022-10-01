##linear search-method1
arr=list(map(int,input()).split())
key= int(input())
if key in arr:
    print("yes")
else:
    print("no")

#linear search-method2
arr=list(map(int,input()).split())
key= int(input())
for i in range(len(arr)):
    if arr[i]==key:
        print("yes")
        break
else:
    print("no")

#Binary Search-method1
arr=sorted(list(map(int,input().split())))
key= int(input())
i=0
j=len(arr)-1
while i<=j:
    m=(i+j)//2
    if arr[m]==key:
        print("yes")
        break
    elif arr[m]<key:
        i=m+1
    else:
        j=m-1
else:
    print("no")"""
