#finding middle word in a string
"""s=input()
s=s.split()
n=len(s)
n1=n//2
print(s[n1])
#i/p:i am padma
#o/p:am"""

#reverse of a string
"""s=input()
print(s[::-1])
#padma
#amdap"""

#reverse of each word in a string
"""s=input()
s1=s.split()
res=""
for i in s1:
        res+=i[::-1]
        res+=" "
print(res)
##i am padma
##i ma amdap """

#max repeated character in a string
"""s=input()#padma
s=list(s)
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
res=max(d,key=d.get)
#d={'p': 1, 'a': 2, 'd': 1, 'm': 1}
print(res)#a
##for unique characters
for i in d:
    if d[i]==1:
        print(i)"""
      
####################################
"""s=input()#AAAABBBBCCCCCC
s1=list(set(s))
final=''
for i in s1:
    res=0
    res=s.count(i)
    final+=str(res)
    final+=str(i)
print(final)#4A4B8C"""
    
##ADDITION OF MATRICES
"""n=int(input())
mat1=[]
mat2=[]
res=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    mat1.append(list(map(int,input().split())))
for i in range(n):
    mat2.append(list(map(int,input().split())))
for j in range(n):
    for k in range(n):
        res[j][k]=mat1[j][k]+mat2[j][k]
print(res)"""

##TRANSPOSE OF A MATRIX
"""n=int(input())
mat=[]
res=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    mat.append(list(map(int,input().split())))
for j in range(n):
    for k in range(n):
        res[j][k]=mat[k][j]
print(res)
class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        res=[[0 for i in range(row)]for j in range(col)]##here row are converted to cols and viceversa
        for j in range(col):
            for k in range(row):
                res[j][k]=mat[k][j]
        return res
   """

