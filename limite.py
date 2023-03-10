from sympy import limit, oo, Symbol
t = Symbol('t')  # variable de la función matemática en este caso es t
y = (t**2 - t + 1)/(t**2 + 1)  # expresión matemática a la cual quiero calcularle el límite
print('El límite de la función  f(t)= (t^2 - t + 1) / (t^2 + 1)  es :', limit(y, t, oo))
