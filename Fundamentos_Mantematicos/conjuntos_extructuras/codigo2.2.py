import numpy as np
#Crea array x,y de 6 elementos y un valor escalar r
x = np.linspace(0,1,6) #Primer array
y = np.linspace(1, 2, 6)#segundo array
r = 2 #validar escalar
print(f'\n ******** Operaciones - funciones - con array ******************')
print(f'Array x {x}')
print(f'Array y {y}')
print(f'Escalar r : {r}')

#Operaciones aritméticas con array
print(f'\n ******** Operaciones aritméticas ******************')
print(f'x + y : {x+y}')
print(f'x-y: {x-y}')
print(f'x*y : {x*y}')
print(f'x/y : {x/y}')

#funciones sobre array
print(f'\n ******** funciones sobre array ******************')
print(f'sqrt(x): {np.sqrt(x)}')
print(f'-x: {-x}')
print(f'|-x|: {np.abs(-x)}')
print(f'x^r:{x**r}')

#Operaciones aritméticas con escalare
print(f'2r+x-3: {2*r+x+3}')
print(f'2*x/4:{2*4/4}')