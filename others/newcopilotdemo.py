# n=int(input());
# i=0;
# finallist=[]
# for _ in range(n):
#     id=int(input());
#     name=input()
#     price=int(input());
#     finallist.append([id,name,price]);
        
# leftout=[list(i for i in range(n))]
# leftoutextras=[]
# for _ in range(3):
#     name=input().split();
#     discount=int(input());
#     for i in range(3):
#         if name==finallist[i][1]:
#             finallist[i][2]=finallist[i][2]*(100-discount)/100;    
#             leftoutextras.append(i)

# finalprint=[]
# for i in leftout:
#     if i in leftoutextras:
#         finalprint.append(i)
# finalprinter=leftoutextras+finalprint
# for i in range(n):
#     print(finallist[finalprinter[i]][0],finallist[finalprinter[i]][1],finallist[finalprinter[i]][2])

R = int(input(""))
C = int(input(""))
matrix = []
for i in range(R):          
    a =[]
    for j in range(C):      
         a.append(input())
    matrix.append(a)
  
# # For printing the matrix
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end = " ")
#     print()

for i in range(R):
    print(matrix[i][0])


