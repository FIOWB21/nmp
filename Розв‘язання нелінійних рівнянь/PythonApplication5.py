import math
from scipy.misc import derivative
def f(x):
    return 8*pow(x,3)-6*pow(x,2)-8*pow(x,1)+6
a=-2
b=-1/2
eps=0.001
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
    print(f'Radical at x = ', round (xi_1,5))
hord(a,b,eps)