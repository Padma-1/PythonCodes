#for a given array find the minimum elememt that is repaeated for k times
#input:[2,2,1,3,1] k=2
#output:1
#explanation: here 1 and 2 are repeated for 2 times. but the smallest number is 1
"""arr=list(map(int,input().split()))
key=int(input())
arr1=sorted(arr)
for i in range(len(arr1)):
    if arr1.count(arr1[i])==key:
        print(arr1[i])
        break
"""
#==========================================================================================================
#Given 2 names..convert the names into numbers
#eg: ANKUR:1*14*11*21*18=58212
#if the number for first name and second name %47 value is same-->print("CHOSEN")-->else print("NOT CHOSEN")
#INPUT:COMETQ and HVNGAT
#OUTPUT: CHOSEN
"""n1=input()
n2=input()
res1=1
res2=1
l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in n1:
    res1*=(l.index(i)+1)
for i in n2:
    res2*=(l.index(i)+1)
if (res1%47)==(res2%47):
    print("CHOSEN")
else:
    print("NOT CHOSEN")"""
#===========================================================================================================
#For a number coolness is defined as number of "101" occurring in its binary representation
#eg:21-->binary representation-->10101-->coolness is 2 as "101" occurring twice
#A number is defined as very cool if its coolness is greater than or equal to k.
#output the number of very cool integers between 1 and R inclusive.
#input is two space seperated integers R and K
##a='10101'
##c=0
##for i in range(2,len(a)):
##    if a[i:i+3]=='101':
##        c+=1
"""r,k=map(int,input().split())
count=0
for i in range(r+1):
    temp=bin(i)
    c=0
    for j in range(2,len(temp)):
        if temp[j:j+3]=='101':
            c+=1#to find how many 101's are present
        if c>=k:
            count+=1#if c>=k then count is to be incremented
            break
print(count) """
#============================================================================================================
#A robot in one step can move 1,2,3,4 or 5 positions forward.
#Determine min number of steps the robot need to make in order to get his destination.
#given an input integer X --> robots destination---->12
#print min steps robot needs to take to get from point 0 to print x.------->3
"""x=int(input())
c=x//5
if x%5!=0:
    print(c+1)
else:
    print(c)"""
#============================================================================================================
#find nth number in series
#series:1 5 13 25 41 61 85 112
#input:5 ---> output:41
##import sys
##i=sys.stdin.readline().strip().split()
"""arr=list(map(int,input().split()))
key=int(input())
print(arr[key-1])"""
#===============================================================================================================
#print pattern
#input:3
#output: 123*321
#        12***21
#        1*****1
"""n=int(input())
star=1
while n>0:
    temp=star
    for i in range(1,n+1):
        print(i,end="")
    while temp>0: 
        print("*",end="")
        temp-=1
    for j in range(n,0,-1):
        print(j,end="")
    print()
    n-=1
    star+=2"""
##5
##12345*54321
##1234***4321
##123*****321
##12*******21
##1*********1
#==========================================================================================
#prove a+b+c=d where a,b,c,d are integers
#remove all zeroes if present in a,b,c,d
#input:101 102 103 306
#output: valid
#11+12+13=36
"""arr=list(map(int,input().split()))
arr1=[]
for i in arr:
    s=0
    while i>0:
        rem=i%10
        if rem==0:
            i=i//10
            continue
        s=s*10+rem
        i=i//10
        s=str(s)[::-1]
        s=int(s)
    arr1.append(s)
if sum(arr1[0:3])==arr1[-1]:
    print("VALID")
else:
    print("INVALID")"""

    

    





































    
    
    
