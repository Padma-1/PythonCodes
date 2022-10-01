#Alphabet rangoli
import string
n=int(input())
alph=string.ascii_lowercase
l=[]
for i in range(n):
        l.append('-'.join(alph[n-1:i:-1]+alph[i:n]).center(4*n-3,'-'))
for i in range(len(l)-1,0,-1):
        print(l[i])
for j in range(len(l)):
        print(l[j])
"""3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c---- """

#DOORMAT
n,m=map(int,input().split())
l=[]
for i in range(n//2):
        l.append(('.|.'*(2*i+1)).center(m,'-'))
l.append('WELCOME'.center(m,'-'))
for i in range(len(l)-1):
        print(l[i])
for j in range(len(l)-1,-1,-1):
        print(l[j])

"""
7 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------  """
