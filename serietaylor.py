from sympy import *
import numpy as np

x = symbols('x')
pprint('Introduce la función para calcular su polinomio de Taylor: ')
expr = eval(input())
pprint('La función es: ')
pprint(expr)
pprint(r'Introduce el punto local x_0: ')
x0 = float(input())
pprint('Introduce el grado del polinomio: ')
n = int(input())
taylor = expr.series(x, x0, n).removeO()
pprint('El Polinomio de Taylor  de orden {0} centrado en {1} es:\n '.format(n, x0))
pprint(taylor)
