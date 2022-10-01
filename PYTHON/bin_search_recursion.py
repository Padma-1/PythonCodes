def Bin_Search(l,h,arr,k):
    if l>h:
        return -1
    m=(l+h)>>1
    if arr[m]==k:
        return m
    elif arr[m]>k:
        return Bin_Search(0,m-1,arr,k)
    else:
        return Bin_Search(m+1,h,arr,k)
    
    
n=int(input())
arr=list(map(int,input().split()))#ARRAY IS IN SORTED ORDER
k=int(input())
print(Bin_Search(0,n-1,arr,k))


