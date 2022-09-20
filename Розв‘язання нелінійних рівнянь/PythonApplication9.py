import math
from scipy.misc import derivative
def f(x):
    return 8*x**3-6*x**2-8*x+6
a=-2
b=-1
eps=0.0001

def rec(a,b,eps):
    if abs(f(b)-f(a))<=eps:
        print('Radical')
        return
    mid=(a+b)/2
    if f(mid)==0 or abs(f(mid))<=eps:
        print(f'Radical at x={mid}', "  -   Method of halving")
    elif f(a)*f(mid)<0:
        rec(a,mid,eps)
    else:
        rec(mid,b,eps)


def hord (a,b,eps):
    if (f(a)*derivative(f,a,n=2)>0):
        x0=a
        xi=b
    else:
        x0=b
        xi=a
    xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))
    while (abs(xi_1-xi)>eps):
        xi=xi_1
        xi_1=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))
    print(f'Radical at x = ', xi_1 , "  -   Chord method")


def komb (a,b,eps):
    if (derivative(f,a,n=1)*derivative(f,a,n=2)>0):
        a0=a
        b0=b
    else:
        a0=a
        b0=b
    ai=a0
    bi=b0
    while abs(ai-bi)>eps:
        ai_1=ai-f(ai)*(bi-ai)/(f(bi)-f(ai))
        bi_1=bi-f(bi)/derivative(f,bi,n=1)
        ai=ai_1
        bi=bi_1
    x=(ai_1+bi_1)/2
    return print('x= ', x , "  -   Combination method")


def nuton(a,b,eps):
    df2=derivative (f,b,n=2)
    if (f(b)*df2>0):
        xi=b
    else:
        xi=a
    df=derivative(f,xi,n=1)
    xi_1=xi-f(xi)/df
    while (abs(xi_1-xi)>eps):
        xi=xi_1
        xi_1=xi-f(xi)/df
    return print('x=', xi_1 , "  -   Newton's method")
nuton(a,b,eps)
komb(a,b,eps)
hord(a,b,eps)
rec(a,b,eps)