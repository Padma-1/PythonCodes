##TO FIND WHETHER GIVEN NUMBER IS SEMI-PRIME OR NOT
#SEMI-PRIME-->NUMBER REPRESENTED IN PRODUCT OF TWO DISTINCT PRIMES

n=100
semi_seive=[i for i in range(n+1)]
def seivegen():
    i=2
    while(i<=n):
        if semi_seive[i]==i:
            for j in range(i*2,n+1,i):
                     semi_seive[j]=semi_seive[j]//i
        i+=1
    return semi_seive
seivegen()
t=int(input())
for i in range(t):
    m=int(input())
    semi_seive[m]
    if semi_seive[m]==1:
        print("yes")
    else:
        print("no")

            
            
            
