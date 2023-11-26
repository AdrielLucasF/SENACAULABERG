import math

a = 2
b = 8
c = 3

delta = math.sqrt((b**2) - 4 * a *c)

xPositivo = ((-b)+delta) / (2*a)
xNegativo = ((-b)-delta) / (2*a)

print("X' = ",xPositivo,"\nX'' = ", xNegativo)

del(a,b,c,delta)
del(xNegativo,xPositivo)