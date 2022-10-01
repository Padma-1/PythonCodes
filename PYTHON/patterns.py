#pattern 1
"""A A A A 
   B B B B 
   C C C C 
   D D D D"""
n=int(input())
x=64
for i in range(1,n+1):
        for j in range(1,n+1):
                print(chr(i+x),end=" ")#print(chr(j+x),end=" ")
        print()

        
#pattern 2
"""5 5 5 5 5 
   4 4 4 4 4 
   3 3 3 3 3 
   2 2 2 2 2 
   1 1 1 1 1 """
n=int(input())
for i in range(n,0,-1):
        for j in range(1,n+1):
                print(i,end=" ")
        print()


#pattern 3
"""5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 """
n=int(input())
for i in range(1,n+1):
        for j in range(n,0,-1):
                print(j,end=" ")
        print()


#pattern 4
"""* * *
   * *
   *"""
n=int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end=" ")
    print()


#pattern5
"""
A A A 
B B 
C"""
n=int(input())
x=64
for i in range(1,n+1):
        for j in range(n,i-1,-1):
                print(chr(i+x),end=" ")
        print()

#pattern 6
""" *
   ***
  *****
 *******
********* """
n=int(input())
z=1
for i in range(1,n+1):
  for sp in range(n-1,i-1,-1):
    print(" ",end="")
  for j in range(1,z+1):
    print("*",end="")
  print()
  z+=2

#pattern 7
"""  3
    A 
  B B B 
C C C C C """
n=int(input())
z=65
k=1
for i in range(1,n+1):
  for sp in range(n-1,i-1,-1):
    print(" ",end=" ")
  for j in range(1,k+1):
    print(chr(z),end=" ")
  print()
  z+=1
  k+=2
  
#pattern 8
""" *****
   *****
  *****
 *****
***** """
n=int(input())
for i in range(1,n+1):
  for sp in range(n-1,i-1,-1):
    print(" ",end="")
  for j in range(1,n+1):
    print("*",end="")
  print()
     
 


