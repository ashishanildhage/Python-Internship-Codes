n=int(input())
l=list(range(0,n))
s=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,n):
    l[i]=input()
    if l[i] == "9":
        s[9]+=1
    if l[i] == "8":
        s[8]+=1
    if l[i] == "7":
        s[7]+=1     
    if l[i] == "6":
        s[6]+=1
    if l[i] == "5":
        s[5]+=1
    if l[i] == "4":
        s[4]+=1
    if l[i] == "3":
        s[3]+=1       
    if l[i] == "2":
        s[2]+=1
    if l[i] == "1":
        s[1]+=1
    if l[i] == "0":
        s[0]+=1       
max=s.index(max(s))
min=s.index(1)
print(max-min)
