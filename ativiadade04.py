import math

a = int(input("insira um numero para 'a': "))
b = int(input("insira um numero para 'b': "))
c = int(input("insira um numero para 'c': "))

delta =  (b**2) - (4 * a *c)

if (delta > 0):
    xPositivo = ((-b)+math.sqrt(delta)) / (2*a)
    xNegativo = ((-b)-math.sqrt(delta)) / (2*a)
    print("X' = ",xPositivo,"\nX'' = ", xNegativo)

elif (delta == 0):
    x = -b/(2*a)
    print("X: ",x)
else:
    print("Delta é negativo, portanto a raiz não é válida")


del(a,b,c,delta)