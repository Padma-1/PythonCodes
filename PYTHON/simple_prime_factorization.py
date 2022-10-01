##SAMPLE INPUT 
##3
##32
##100
##9085
##SAMPLE OUTPUT 
##2^5
##2^2*5^2
##2^0*5^1*23^1*79^1

x=100
seive=[i for i in range(x+1)]
i=2
while(i*i<=x):
    if seive[i]==i:
       for j in range(i*i,x+1,i):
           if seive[j]==j:
                seive[j]=i
    i+=1
t=int(input())
for i in range(t):
    d={2:0}
    n=int(input())
    if n==seive[n]:
        print("2^0")
    else:
        while n!=1:
            y=seive[n]
            n=n//y
            if y not in d:
                d[y]=1
            else:
                d[y]+=1
        print(d)#
            
        s=""
        for i in d:
            s+=(str(i)+"^"+str(d[i]))
            s+="*"
        print(s[0:len(s)-1])
        


