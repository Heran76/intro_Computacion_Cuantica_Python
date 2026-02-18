import matplotlib.pyplot as plt
import numpy as np

#dibujo de los puntos(0.2), (1, 3), (2,4) unidos con lineas
plt.figure()
plt.plot([0, 1, 2], [2, 3, 4], color="blue")
plt.show()

#dibujo de los puntos (0.2),(1.3),(2.4) con las lineas negras y los puntos
#(0.3), (1.2); (1.4), (2.3) con cuadros en color gris claro

plt.figure()
plt.plot([0,1,2],[2,3,4], 's', color='black')
plt.plot([0,1,1,2],[3,2,4,3], 's', color='lightgray')
plt.show()

#Dibujar una circuferencia de radio r centrada en(0.0) con precisión de 
#p puntos en el eje x
r = 2
p = 100
x = np.linspace(-r, r, p)

y_pos = np.sqrt(r**2 - x **2)
y_neg = -np.sqrt(r**2 - x**2)  # Solo cambié esta línea (agregué el signo negativo)

plt.figure(figsize=(5.5, 5.5))
plt.plot(x, y_pos, color='black') #Puntos positivos
plt.plot(x, y_neg, color='black') #Puntos negativos
plt.axis('equal')  # Esta línea asegura que el círculo se vea redondo
plt.show()