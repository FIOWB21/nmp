
import math

def f(x):
    return 8*x**3-6*x**2-8*x+6
a=0
b=1
eps=0.0001

def rec(a,b,eps):
    if abs(f(b)-f(a))<=eps:
        print('Radical')
        return
    mid=(a+b)/2
    if f(mid)==0 or abs(f(mid))<=eps:
        print(f'Radical at x={mid}')
    elif f(a)*f(mid)<0:
        rec(a,mid,eps)
    else:
        rec(mid,b,eps)
rec(a,b,eps)
         

