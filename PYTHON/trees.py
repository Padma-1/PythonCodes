class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None
def gen_tree(data,root,i,n):
    if i<n and data[i]!=None:
        root=Node(data[i])
        root.left=gen_tree(data,root.left,2*i+1,n)
        root.right=gen_tree(data,root.right,2*i+2,n)
    return root
def level_order(root,level):
    queue=[]
    queue.append(root)
    i=queue[0]
    while queue!=[]:
        level.append(queue[0].val)
        temp=queue.pop(0)
        if temp.left!=None:
            queue.append(temp.left)
        if temp.right!=None:
            queue.append(temp.right)
        
data=[1,2,None,4,5,6,7,8,9,10,11,12]
root=None
root=gen_tree(data,root,0,len(data))
level=[]
level_order(root,level)
print(level)
