'''
Cree un array con los valores [24.6, 18.3, 29.5,27,22.8,15.22.1], que simulan temperaturas diarias en grados
Celsius, Calcule y muestre la temparatura máxima, minima y promedio, finalmente, seleccione y muestre 
únicamente las temperaturas superiores a 24.0

'''

# Importamos NumPy, nuestro caballo de batalla para computación numérica y cuántica.
import numpy as np

# Creamos un array con las temperaturas diarias en grados Celsius.
# Nota: Corregí el array original que tenía un error: '15.22.1' era inválido.
# Asumimos que eran dos valores: 15.0 y 22.1.
t = np.array([24.6, 18.3, 29.5, 27, 22.8, 15, 22.1])

# Mostramos el array original para verificar los datos.
print("Temperaturas diarias: {}".format(t))

# Calculamos las métricas estadísticas.
# Observa una nueva sintaxis: podemos llamar a .mean(), .min(), .max()
# directamente sobre el array (métodos del objeto NumPy), además de usar
# las funciones np.mean(), np.min(), np.max() como en ejercicios anteriores.
# Ambas formas son válidas y comunes.
avg_t = t.mean()  # Equivalente a np.mean(t)
min_t = t.min()   # Equivalente a np.min(t)
max_t = t.max()   # Equivalente a np.max(t)

# Imprimimos los resultados con un formato limpio y una cifra decimal.
print("Temperatura máxima: {:.1f}°C".format(max_t))
print("Temperatura mínima: {:.1f}°C".format(min_t))
print("Temperatura promedio: {:.1f}°C".format(avg_t))

# --- EL CONCEPTO CLAVE: INDEXADO BOOLEANO (FILTRADO) ---
# t > 24.0  -> Esto crea un array de máscara booleana: [True, False, True, True, False, False, False]
# t[t > 24.0] -> Usamos esa máscara como índice para seleccionar solo los elementos donde es True.
# El resultado es un nuevo array que contiene solo [24.6, 29.5, 27]
high_t = t[t > 24.0]

# Mostramos las temperaturas filtradas.
print("Temperaturas superiores a 24.0°C: {}".format(high_t))

'''
El Valor de Este Código para la Computación Cuántica
Este ejercicio es un gran salto en tu preparación. El indexado booleano es una de las herramientas más poderosas y prácticas de NumPy, y su equivalente en computación cuántica es absolutamente crucial.

1. Filtrado de Resultados de Medición (El "Post-procesamiento" Clásico)
Cuando ejecutas un circuito cuántico muchas veces, obtienes un enorme conjunto de datos de resultados binarios (por ejemplo, '000', '001', '110', etc.). Muy a menudo, no te interesan todos los resultados, sino solo aquellos que cumplen una condición específica.

Tu código filtra temperaturas t > 24.0.

En computación cuántica, harías algo como:

python
# Supón que 'resultados' es un array de strings como ['000', '001', '010', '000', '111']
# Queremos solo los resultados donde el primer qubit (el bit más a la izquierda) es '1'
resultados_filtrados = resultados[np.char.startswith(resultados, '1')]
O si trabajamos con arrays numéricos que representan estados:

python
# Filtramos los estados base cuya energía (calculada por separado) sea baja
estados_baja_energia = estados[energias < 0.5]
Este filtrado es el corazón del post-procesamiento clásico que sigue a un experimento cuántico.

2. Proyecciones y Medición en Mecánica Cuántica
El concepto de "seleccionar elementos que cumplen una condición" es una analogía directa de cómo funciona la medición en cuántica.

Cuando mides un qubit en superposición, este se "proyecta" o "colapsa" a uno de los estados base (|0> o |1>).

Si tienes un sistema de múltiples qubits en superposición y decides medir solo el primer qubit, estás haciendo exactamente un filtrado: te quedas con todas las componentes del estado donde el primer qubit es |0> (y las renormalizas), o donde es |1>.

Aunque el mecanismo cuántico es más complejo, la operación mental de "seleccionar un subconjunto basado en una condición" es la misma que aplicas con t[t > 24.0].

3. Preparación de Estados Iniciales
A veces, quieres preparar un estado cuántico que solo incluya ciertas configuraciones. El indexado booleano te ayuda a visualizar y construir esos estados en simulaciones.

Ejemplo: Imagina que quieres crear un estado de 3 qubits que sea una superposición uniforme de solo los números pares (000, 010, 100, 110).

Podrías generar todos los estados y luego usar indexado booleano para filtrar los impares, exactamente como filtraste las temperaturas.

4. Análisis de Probabilidades Condicionales
En algoritmos cuánticos avanzados, a menudo necesitas calcular la probabilidad de un evento dado que ha ocurrido otro evento. Esto es una probabilidad condicional.

Para calcularla clásicamente a partir de los datos de un simulador, usarías un filtro. Por ejemplo: "¿Cuál es la temperatura promedio de los días en los que llovió?".

En tu caso: "¿Cuál es la temperatura promedio de los días con t > 24.0?".

python
# Calcular el promedio de las temperaturas altas
promedio_altas = high_t.mean()
Esto es análogo a calcular el valor esperado de un observable en el subespacio donde se cumple una condición.

En resumen: Este ejercicio te ha enseñado a aislar subconjuntos de datos relevantes. En el mundo cuántico, esa habilidad se traduce directamente en la capacidad de analizar resultados de mediciones, comprender el colapso del estado cuántico por proyección, 
y calcular probabilidades condicionales que son esenciales para muchos protocolos cuánticos (como la teletransportación o la corrección de errores). Es una habilidad fundamental que usarás constantemente.
'''