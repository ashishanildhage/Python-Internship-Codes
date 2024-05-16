import math,sys
from functools import reduce

def specialNumber(n):
    count=0
    for T in range(1,n+1):
        quartic,product=0,1
        quartic=reduce(lambda x, y: (x**4)+(y**4),list(map(int, str(T))))
        product=reduce(lambda x, y: x*y,list(map(int, str(T))))
        if math.gcd(quartic,product)>1:
            count+=1
    return count

print(*([specialNumber(n) for n in 
[int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]])
, sep = "\n")

#https://stackoverflow.com/questions/51772888/how-can-i-reduce-the-time-complexity-of-the-given-python-code#:~:text=You%20can%20easily%20omit%20declaration,readline'%2C%20and%20'stdout.

