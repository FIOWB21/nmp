import math
from scipy.misc import derivative
def f(x):
    return 8*pow(x,3)-6*pow(x,2)-8*pow(x,1)+6
a = -2
b = -1
eps = 0.001

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
    return print('x=', xi_1)
nuton (a,b,eps)