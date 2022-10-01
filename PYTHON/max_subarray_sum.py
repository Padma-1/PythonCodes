#sub array having maximum sum
"""l=list(map(int,input().split()))#-2 -2 4 -1 -2 1 5 -3
y=0                                 
for i in range(len(l)):
    for j in range(i,len(l)):
        x = sum(l[i:j+1])
        if x>y:
            y=x
print(y)"""
    
l=list(map(int,input().split()))#-2 -2 4 -1 -2 1 5 -3
max_end_here=0
max_so_far=0
for i in range(len(l)):#-2-->4
    max_end_here+=l[i]#--->-3
    if max_end_here<0:#-2<0#4<0
        max_end_here=0
    if max_so_far<max_end_here:#0<4
        max_so_far=max_end_here
print(max_so_far)
