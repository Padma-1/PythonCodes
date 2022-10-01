n1=[1,3]
n2=[2]
n=sorted(n1+n2)#[1,2,3]
y=len(n)#3
if y%2==0:#even
    mid=y//2
    median=(n[mid-1]+n[mid])/2
else:
    mid=y//2#1st position
    median=n[mid]
print('{0:0.5f}'.format(median))#2.00000
