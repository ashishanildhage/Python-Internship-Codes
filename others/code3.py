n=int(input())
a=[]
for i in range(0, n):
 	a=list(map(int,input()))[:n] 
max=max(a)
min=min(a)
sum=max+min
print(sum)


