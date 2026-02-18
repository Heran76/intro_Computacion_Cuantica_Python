import matplotlib.pyplot as plt
from IPython.display import display

#creamos la imagen 3D

f = plt.figure(figsize = (7,7))  # Corregido: agregué el segundo valor
ax = plt.axes(projection='3d') # Ejes de proyeccion en 3D

#dibujamos los ejes de coordenadas

ax.plot(xs=[-1,1], ys=[0,0], zs=[0,0], color='black', linewidth=1)
ax.plot(xs=[0,0], ys=[-1,1], zs=[0,0], color="black", linewidth=1)
ax.plot(xs=[0,0], ys=[0,0], zs=[-1,1], color='black', linewidth=1)
plt.show()
display(f)