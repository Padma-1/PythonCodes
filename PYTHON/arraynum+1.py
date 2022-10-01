#convert given list to a number and add one to that number..then again convert into list
l=list(map(int,input().split()))#2 4 3 6 6
x=0
for i in l:
   x=x*10+i
x+=1
print(x)#24367
x=list(map(int,str(x)))
print(x)#[2, 4, 3, 6, 7]
