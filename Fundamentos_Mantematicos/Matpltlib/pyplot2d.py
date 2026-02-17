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