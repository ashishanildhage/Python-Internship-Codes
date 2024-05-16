n=int(input("Enter the number of nodes: "))
print("Enter the nodes: ")
nodes=[int(input()) for i in range(n)]
print("The nodes are: ",nodes)
maxormin=True
if nodes%2==1:
    nodes.append(nodes[-1]-1)
count=0
final_layer=[]
layer=[]
while len(nodes)!=1:
    for node in nodes:
        if count==0:
            layer.append(node)
            count+=1
        else:
            count=0
            layer.append(node)
            if maxormin:
                final_layer.append(max(layer))
            else:
                final_layer.append(min(layer))
            layer=[]
    maxormin=not maxormin
    nodes=final_layer        
    final_layer=[]

print(nodes)


 
    
