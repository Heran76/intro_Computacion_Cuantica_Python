'''
Considere los array [10,5,3,8]y [10,6,4,7] que representan las puntuaciones de cuatro estudiantes
den dos exámenes, respectivamente. Realice las siguientes operaciones:
1.- Calcule la media de la calificación de cada estudiante, asi como la meida global de la calificación
del grupo de estudiantes.
2.- Reste las calificaciones del segundo examen de calificicaciones del primero, para  halla la evaluación
indidivual de cada estudiante.
3.- Multiple la calificaciones del primer examen por 1.1 para simular un incrementoen la calificacióndel 10%,
sabiendo que ninguna calificación puede exceder de 10.
4.- Imprima el resultado de cada operación.
 

'''
# Importamos NumPy, esencial para computación cuántica y científica
import numpy as np

# Creamos dos arrays unidimensionales con las puntuaciones de 4 estudiantes
# A: puntuaciones del primer examen
# B: puntuaciones del segundo examen
A = np.array([10, 5, 3, 8])
B = np.array([10, 6, 4, 7])

# --- CONCEPTO CLAVE: CREACIÓN DE MATRICES 2D ---
# np.vstack() apila verticalmente los arrays A y B
# El resultado es una matriz de 2 filas (exámenes) y 4 columnas (estudiantes)
# All[0] = [10, 5, 3, 8]  (primer examen)
# All[1] = [10, 6, 4, 7]  (segundo examen)
All = np.vstack((A, B))

# --- CONCEPTO CLAVE: OPERACIONES POR EJES (AXIS) ---
# axis=0 opera a lo largo de las filas (para cada columna/estudiante)
# Calcula la media de cada estudiante (promedio entre sus dos exámenes)
# Resultado: [10.0, 5.5, 3.5, 7.5]
print("Calificaciones medias por estudiante: {}".format(np.mean(All, axis=0)))

# Sin especificar axis, opera sobre todos los elementos (media global)
# Resultado: 6.625
print("Calificacion promedio del grupo: {}".format(np.mean(All)))

# --- CONCEPTO CLAVE: DIFERENCIAS ENTRE FILAS ---
# np.diff() calcula la diferencia entre elementos consecutivos a lo largo de un eje
# axis=0: resta la fila 1 - fila 0 (segundo examen - primer examen)
# Resultado: [[0, 1, 1, -1]] (matriz 1x4)
diff = np.diff(All, axis=0)
print("Evolucion de cada estudiante: {}".format(diff))

# --- CONCEPTO CLAVE: OPERACIONES VECTORIZADAS Y FILTRADO ---
# Multiplicamos todo el array A por 1.1 (incremento del 10%)
# Esto se aplica elemento a elemento automáticamente (vectorización)
Ainc = 1.1 * A  # Resultado temporal: [11.0, 5.5, 3.3, 8.8]

# --- CONCEPTO CLAVE: INDEXADO BOOLEANO PARA LIMITAR VALORES ---
# Ainc > 10 crea una máscara booleana: [True, False, False, False]
# Asignamos 10 a todas las posiciones donde la máscara es True
# Esto asegura que ninguna calificación exceda 10
Ainc[Ainc > 10] = 10  # Resultado final: [10.0, 5.5, 3.3, 8.8]

print("Primer examen con incremento del 10%: {}".format(Ainc))
'''
El Valor de Este Código para la Computación Cuántica
Este ejercicio es excepcionalmente importante porque introduce conceptos que son directamente análogos a operaciones fundamentales en computación cuántica.

1. Matrices 2D: La Representación de Múltiples Qubits y Operadores
La creación de All como una matriz 2D usando np.vstack() es un paso crucial:

Tu código: Representas dos exámenes (filas) para cuatro estudiantes (columnas).

En computación cuántica:

Los estados de múltiples qubits se representan como vectores en un espacio de dimensión 2ⁿ. Por ejemplo, 2 qubits se representan como un vector de 4 elementos.

Las puertas cuánticas (operadores) que actúan sobre estos estados se representan como matrices de 2ⁿ × 2ⁿ.

Cuando aprendas a simular circuitos cuánticos, estarás multiplicando matrices (puertas) por vectores (estados) constantemente. La comprensión de estructuras 2D es fundamental.

2. El Parámetro axis: Trabajando con Subespacios Cuánticos
El concepto de axis en NumPy es una de las herramientas más poderosas y directamente aplicables:

Tu código: np.mean(All, axis=0) calcula el promedio a través de los exámenes para cada estudiante.

En computación cuántica: Este concepto es análogo a operar sobre qubits específicos en un sistema multi-qubit.

Imagina que tienes un estado de 3 qubits (8 dimensiones) y quieres aplicar una puerta solo al primer qubit.

En simulaciones, esto se implementa realizando operaciones que actúan sobre ciertos ejes (dimensiones) del tensor que representa el estado cuántico.

Calcular la probabilidad de medir un qubit en estado |0> implica "colapsar" o "trazar" sobre los otros qubits, una operación que conceptualmente es similar a especificar un axis para ignorar ciertas dimensiones.

3. np.diff(): Análogo a la Evolución Temporal y Derivadas
np.diff() calcula cambios entre estados:

Tu código: Muestra cómo cambió la calificación de cada estudiante entre exámenes.

En computación cuántica:

La evolución temporal de un sistema cuántico se describe por cambios infinitesimales (derivadas). La ecuación de Schrödinger iℏ ∂/∂t |ψ⟩ = H|ψ⟩ relaciona el cambio del estado con su energía.

En simulaciones numéricas, a menudo calculamos diferencias entre estados cuánticos en tiempos sucesivos para entender su dinámica.

En optimización cuántica, los algoritmos iterativos calculan la diferencia entre iteraciones para ver si convergen.

4. Operaciones Vectorizadas: El Rendimiento Necesario para la Cuántica
La multiplicación 1.1 * A es un ejemplo de vectorización:

Tu código: Una sola operación multiplica todos los elementos del array.

En computación cuántica: La simulación de sistemas cuánticos requiere una potencia de cálculo inmensa. Los estados de 30 qubits son vectores de más de mil millones de elementos. Sin vectorización (operaciones en C/Fortran como las de NumPy), sería imposible simular incluso sistemas pequeños. Este hábito de pensar en operaciones sobre arrays completos, no en bucles, es esencial.

5. Indexado Booleano con Condiciones: El Colapso de la Función de Onda
Ainc[Ainc > 10] = 10 es, de nuevo, indexado booleano, pero ahora con asignación:

Tu código: Limitas físicamente los valores que superan un umbral.

En computación cuántica: Aunque más complejo, esto recuerda al concepto de medición y proyección. Cuando mides un estado cuántico, las amplitudes de probabilidad que no corresponden al resultado medido "desaparecen" (colapsan a cero), y las que sí corresponden se "renormalizan". Es como un filtro drástico aplicado al vector de estado.

En resumen: Este ejercicio te ha enseñado a trabajar con matrices 2D (la base de sistemas multi-qubit), a realizar operaciones por ejes (manipular qubits específicos), a calcular diferencias (evolución temporal) y a aplicar operaciones vectorizadas (eficiencia computacional). Estás construyendo, pieza por pieza, el conjunto de habilidades necesario para simular y comprender sistemas cuánticos.

'''