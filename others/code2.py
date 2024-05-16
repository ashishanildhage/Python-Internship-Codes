b=int(input())
if b>=0:
    sign=1
else:
    sign=-1
n = abs(b)
rev = 0

while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
    

print(b-(sign*rev))
