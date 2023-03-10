from sympy import limit, oo, Symbol
t = Symbol('t')  # variable de la función matemática en este caso es t
y = (t**2 - t + 1)/(t**2 + 1)  #y=f(t) expresión matemática a la cual quiero calcularle el límite 
print('El límite de la función  f(t)= (t^2 - t + 1) / (t^2 + 1)  es :', limit(y, t, oo)) # parámetro oo:  indica que estoy calculando el límite de la función para cuando t tiende al +inf
