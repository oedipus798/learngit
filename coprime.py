from random import *
from math import *
def gcd(a,b):
    a=int(fabs(a))
    b=int(fabs(b))
    while(b!=0):
        r=a%b
        a=b
        b=r
    return a

def prob(N):
    total=0
    if N<0:
        print(' oh ,you don\'t like me')
        return -1
    else:
        for i in range(1,100000):
            a=randint(0,N)
            b=randint(0,N)
            s=gcd(a,b)
            if s==1:
                total+=1
            else:
                continue
#            print(s,a,b)
        return total/1e5

N=int(input('please input a non negative integer'))
for i in range(5):
    print(prob(N))
