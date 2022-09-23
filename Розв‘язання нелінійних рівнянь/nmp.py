import math
import numpy as np
from scipy.misc import derivative
def f(x):
    return 3*pow(x, 4) - 2*pow(x,3) - pow(x, 2) + x - 4
a=-2
b=-1
eps=0.0001

def find_segments(): #відокремлюємо корені
    search_range = np.arange(-10, 10, 1)
    
    a = None

    previous_x = None
    current_x  = None

    segments = []

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x != None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    
    return segments

segments = find_segments()

for a, b in segments:
    print(f'Found segment:  [{a}, {b}]')

def rec(a, b, eps): 
    while (abs(a-b) > eps):
        if f(a)*f((a+b)/2)<0: 
            b = (a+b)/2 
        else: 
            a = (a+b)/2
        x = (a+b)/2
    
    print ('x= ', round(x,5), '  -   Method of halving')



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
    print('x= ', round (xi_1,5) , '  -   Chord method')


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
    return print('x= ', round(x,5) , "  -   Combination method")


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
    return print('x=', round(xi_1, 5) , "  -   Newton's method")
print (f'Solution of a nonlinear equation on a segment [{-2}, {-1}]')
rec(-2,-1,eps)
hord(-2,-1,eps)
nuton(-2,-1,eps)
komb(-2,-1,eps)
print (f'Solution of a nonlinear equation on a segment [{1}, {2}]')
rec(1,2,eps)
hord(1,2,eps)
nuton(1,2,eps)
komb(1,2,eps)
