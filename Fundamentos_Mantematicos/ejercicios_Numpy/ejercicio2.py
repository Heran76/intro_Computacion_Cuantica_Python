'''
Dado el arraynp.array(25,30,22,35,28) que representa las edades de un grupo
 de personas, calcule la edad promedio, mínima y maxima. Imprima los resultados por
 consola. Nota: NumPy  ofrece funciones directas para cáculos, comonp.mean(), np.min()
 y np.max()
'''
import numpy as np

# Crear array
a= np.array([25, 30, 22, 35, 28])

# Calcular el promedio, el minimo y el maximo
avg_a, min_a, max_a= np.mean(a), np.min(a), np.max(a)

# Imprimir los resultados
print(f"El array de edades es: {a}")
print("La edad promedio es: {:.2f}".format(avg_a))
print("Las edades mínima y máxima son: {} y {}".format(min_a, max_a))

'''
El Valor de Este Código para la Computación Cuántica
Este ejercicio da un paso adelante con respecto al anterior. 
Ya no solo creamos un array y lo sumamos, sino que ahora realizamos análisis estadísticos sobre los datos. Esto es increíblemente relevante por las siguientes razones:

1. Comprensión de la Estadística Descriptiva (La Base de los Resultados Cuánticos)
La mecánica cuántica es, por naturaleza, probabilística. Cuando ejecutas un algoritmo cuántico, 
no obtienes una única respuesta determinista, sino una distribución de probabilidades sobre los posibles resultados.

Tu código toma un conjunto de datos (las edades) y calcula el promedio, el mínimo y el máximo.
 Esto es estadística descriptiva.

En computación cuántica, harás exactamente esto, pero con los resultados de tus experimentos. 
Por ejemplo:

Ejecutas un circuito cuántico 1024 veces (esto se llama "número de shots").

Obtienes un array de resultados: [000, 001, 000, 111, 001, ...].

Convertirías esos resultados en datos numéricos y luego usarías np.mean(), np.min(), np.max() para entender el comportamiento del algoritmo.

El valor esperado de un observable (como la posición o el spin de una partícula) no es más que un promedio ponderado, un concepto hermano de np.mean().

2. np.min() y np.max() en Algoritmos Cuánticos
Aunque pueda no parecerlo, encontrar mínimos y máximos es el corazón de algunos de los algoritmos cuánticos más prometedores.

Optimización: Algoritmos como el QAOA (Quantum Approximate Optimization Algorithm) o el recocido cuántico se utilizan para resolver problemas de optimización. El objetivo es encontrar el mínimo (o máximo) de una función compleja (por ejemplo, la ruta más corta para un viajante o la configuración de menor energía de un sistema).

En una simulación clásica de estos algoritmos, usarías np.min() y np.max() constantemente para ver si el algoritmo cuántico está convergiendo hacia la solución óptima.

3. Análisis de la Fiabilidad (Fidelidad)
Cuando construyes una computadora cuántica real, los resultados son ruidosos. Ejecutas el mismo circuito muchas veces y obtienes una nube de resultados.

np.mean() te da el valor central esperado.

np.min() y np.max() te dan los límites del ruido, ayudándote a entender la magnitud de los errores.

Esto es análogo a tu array de edades: las edades tienen una variabilidad, y nosotros queremos entender su rango (min y max) y su tendencia central (mean).

4. Transición a Conceptos más Avanzados
Las funciones que acabas de usar (mean, min, max) son la puerta de entrada a conceptos cuánticos más complejos:

Varianza y Desviación Estándar: En cuántica, el principio de incertidumbre de Heisenberg se expresa matemáticamente en términos de la desviación estándar de dos observables (como posición y momento). Para calcular una desviación estándar en Python, usarías np.std(), que es hermana de np.mean().

Estados propios: Encontrar el mínimo de un sistema (su estado fundamental) es el objetivo de la química cuántica y los algoritmos de optimización. Ese "mínimo" es, en realidad, el autovalor (eigenvalue) más bajo de una matriz enorme que representa la energía del sistema.

En resumen: Este ejercicio te enseña a extraer información significativa de un conjunto de datos. En computación cuántica, los datos son los estados cuánticos y las medidas, y la información que extraes (mean, min, max) son los resultados de tus experimentos, los valores esperados de tus observables y las soluciones a tus problemas de optimización. Estás aprendiendo a interpretar los resultados, que es tan importante como generar el código.
'''