numplayers=int(input())
score=[]
for i in range(0, numplayers):
 	score.append(int(input()))

health1=int(input())
health2=int(input())
count=0
for i in score:
    if health1%i==0 and health2%i==0:
        count+=1
        
print(count)

