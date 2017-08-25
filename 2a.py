from math import *
xi=float(input("Limite superior: "))
xi_1=float (input("Limite inferior: "))
fx = input('f(x) = ')
fxi= eval(fx,{'x' : xi,'cos' : cos})
fxi_1 = eval(fx,{'x' : xi_1,'cos' : cos})
xnueva = xi-((f(xi)*(xi_1-xi))/(f(xi_1)-f(xi)))
error_a=100      
while fx(xnueva) !=0 and error_a > error_s:
      if fx (xnueva) > xi:
            xi = xnueva
            xi_1 = xi
      elif fx (xnueva) < xi_1:
            xi_1 = xnueva
            xi = xi_1
      elif xi_1 < xnueva < xi:
            xnueva = xi
      else:
            break
      xnueva = xi-((f(xi)*(xi_1-xi))/(f(xi_1)-f(xi)))
      error_a = abs ((xi-xnueva)/xnueva)*100

print(xnueva)