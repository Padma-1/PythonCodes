#input: abc
#output:[[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
"""s=input()#ab
lis=[]
def fun(s,i,l):
    global lis
    if i==-1:
        lis.append(l)
        return
    fun(s,i-1,l)
    fun(s,i-1,[s[i]]+l)

fun(s,len(s)-1,[])
print(lis)"""


##n=7
##arr=[1,2,3,4,5,6,7]
##d=2
##out:3 4 5 6 7 1 2
"""n=int(input())
arr=list(map(int,input().split()))
i=int(input())
print(arr[i:n+1]+arr[0:i])"""
