import sympy
from sympy import *

var('x y')

# equation

# example of a perfect square
eq1=  x**2 + 4*x + 4
#eq1=  x**2 - 4*x + 4

# example of difference of squares
eq2=  x**2 - 4


f = sympy.factor(eq1)
f1 = sympy.factor(eq2)
print("perfect square")
print(f,":::",eq1)
print("*"*20)
print("difference of squares")
print(f1,":::", eq2)