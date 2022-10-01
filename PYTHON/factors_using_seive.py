##To find number of prime factors and those factors
"""n=15
seive=[i for i in range(n+1)]
i=2
while(i*i<=n):
    if seive[i]==i:
       for j in range(i*i,n+1,i):
           if seive[j]==j:
                seive[j]=i
    i+=1
pf_list=[]
while n!=1:
    x=seive[n]
    n=n//x
    pf_list.append(x)
print(pf_list)#to print prime factors
print(len(set(pf_list)))#to print number of prime factors"""


##To find number of factors of given number
"""n=50
seive=[i for i in range(n+1)]
i=2
while(i*i<=n):
    if seive[i]==i:
       for j in range(i*i,n+1,i):
           if seive[j]==j:
                seive[j]=i
    i+=1
d={}
res=1
factors_list=[]
while n!=1:
    x=seive[n]
    n=n//x
    factors_list.append(x)
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
for i in d:
    res*=(d[i]+1)#(value1+1)*(value2+1)*......*(valuen+1)
print(res)#total 6 factors
print(factors_list)#[2, 5, 5]"""



#Almost Prime
##A number is called almost prime if it has exactly two distinct prime divisors.
##For example, numbers 6, 18, 24 are almost prime, while 4, 8, 9, 42 are not.
##Find the amount of almost prime numbers which are between 1 and n, inclusive.
"""n=21
c=0
seive=[i for i in range(n+1)]
i=2
while(i<=n):
    if seive[i]==i:
       for j in range(i,n+1,i):
           if seive[j]==j:
                seive[j]=i
           else:
               c+=1
               print(j)
    i+=1"""
    


    
    
