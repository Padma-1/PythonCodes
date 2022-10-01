##Input: 
##4
##Output: 
##2 + 2 = 4
##
##If there are more than one solution possible, return the lexicographically smaller solution.
##If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then [a, b] < [c, d]
##If a < c OR a==c AND b < d.


"""def create_sieve(n):
    res=[]
    sieve=[1]*(n+1)
    sieve[0]=sieve[1]=0
    i=2
    while (i*i<=n):
            if sieve[i]==1:
                for j in range(i*i,n+1,i):
                    sieve[j]=0
            i+=1
    for i in range(n+1):
        if sieve[i]==1:
            res.append(i)
    return res
    
n=int(input())
res=create_sieve(n)
for i in range(3):
    key=int(input())
    for i in range(len(res)):
            if res[i] and (key-res[i]) in res:
               print(res[i],key-res[i])
               break
"""
##2Q)
##Consecutive Prime Sum
##Some prime numbers can be expressed as Sum of other consecutive prime numbers.
##For example
##5 = 2 + 3
##17 = 2 + 3 + 5 + 7
##41 = 2 + 3 + 5 + 7 + 11 + 13
##Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
##
##Write code to find out number of prime numbers that satisfy the above-mentioned property in a given range.
##Input Format:
##First line of input contains k - the number of inputs
##The next k lines contains a number N.
##
##Output Format:
##Print the total number of all such prime numbers which are less than or equal to N.
##Example:
##Input:
##k = 2
##N = 20
## N = 15
##Output:
##2 (there are 2 such numbers: 5 and 17)
##1
def create_sieve(n):
    res=[0]*(n+1)
    sieve=[1]*(n+1)
    sieve[0]=sieve[1]=0
    i=2
    while (i*i<=n):
            if sieve[i]==1:
                for j in range(i*i,n+1,i):
                    sieve[j]=0
            i+=1
    res[0]=2
    for i in range(1,n+1):
        if sieve[i]==1 and sieve[i+res[i-1]]==1:
            res[i]=i+res[i-1]
        else:
            res[i]=res[i-1]
    print (res)
    
n=int(input())
create_sieve(n)

