'''
Genera una array con los primeros 10 multiplos de 3, comenzando desde el 3(es decir, 3,6,9...)
Acontinuación, modifique el array reemplazando por -1 todos los elementos que se encuentren en posiciones impares
(indices 1,3,5,etc) imprima el array resultante.

'''
import numpy as np

# --- CONCEPTO CLAVE: arange() CON TRES PARÁMETROS ---
# np.arange(inicio, fin, paso)
# inicio = 3: empezamos en 3
# fin = 3 * 10 + 1 = 31: generamos hasta 30 (el fin es exclusivo, por eso sumamos 1)
# paso = 3: incrementos de 3 en 3
# Esto genera: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = np.arange(3, 3 * 10 + 1, 3)

print(f"Array original (múltiplos de 3): {A}")

# --- CONCEPTO CLAVE: SLICING CON PASO Y ASIGNACIÓN DIRECTA ---
# A[1::2] selecciona:
# - 1: empezamos desde el índice 1 (segundo elemento)
# - ::2: tomamos cada 2 elementos (paso 2)
# Esto selecciona los índices: 1, 3, 5, 7, 9 (posiciones pares del array)
# En el array original [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# Los elementos seleccionados son: [6, 12, 18, 24, 30]
# A todos estos elementos les asignamos el valor -1
A[1::2] = -1

# El array resultante será:
# Índice 0: 3 (no se modifica)
# Índice 1: -1 (se modifica)
# Índice 2: 9 (no se modifica)
# Índice 3: -1 (se modifica)
# Índice 4: 15 (no se modifica)
# Índice 5: -1 (se modifica)
# Índice 6: 21 (no se modifica)
# Índice 7: -1 (se modifica)
# Índice 8: 27 (no se modifica)
# Índice 9: -1 (se modifica)
# Resultado final: [3, -1, 9, -1, 15, -1, 21, -1, 27, -1]

print(f"Array modificado: {A}")

'''
El Valor de Este Código para la Computación Cuántica
Este ejercicio, aunque parece simple, introduce conceptos que son absolutamente esenciales para trabajar con simulaciones cuánticas eficientes.

1. Comprensión de la Indexación y el Slicing: La Base de la Manipulación de Estados
En computación cuántica, los estados de múltiples qubits son vectores enormes (de tamaño 2ⁿ). Poder acceder y modificar subconjuntos específicos de estos vectores es crucial.

Tu código: Usas A[1::2] = -1 para modificar selectivamente elementos en posiciones pares del array.

En computación cuántica: Esto es directamente análogo a aplicar operaciones a ciertos qubits o a preparar estados específicos.

Imagina que tienes un estado de 3 qubits (8 elementos) y quieres aplicar una puerta solo cuando el primer qubit sea |1⟩. Esto implica seleccionar y modificar un subconjunto específico de amplitudes (exactamente la mitad de ellas), muy similar a tu slicing.

La corrección de errores cuánticos a menudo requiere identificar y corregir errores que ocurren en posiciones específicas del vector de estado.

2. Patrones y Simetrías en Estados Cuánticos
Muchos estados cuánticos importantes tienen patrones regulares que pueden generarse eficientemente con slicing:

Tu código: Crea un patrón de valores -1 en posiciones pares.

En computación cuántica:

El estado GHZ (Greenberger-Horne-Zeilinger) para 3 qubits es (|000⟩ + |111⟩)/√2. En notación de índices, solo los índices 0 y 7 son no cero. Esto es un patrón de selección.

El estado W para 3 qubits es (|001⟩ + |010⟩ + |100⟩)/√3. Esto selecciona índices específicos (1, 2, 4 en little-endian).

La transformada de Fourier cuántica (QFT) genera patrones de fases que pueden implementarse eficientemente usando operaciones sobre subconjuntos de índices.

3. Comprensión de la Numeración de Índices (Endianness)
El slicing [1::2] te obliga a pensar en qué índices estás seleccionando. En computación cuántica, esto es crucial por el concepto de endianness:

Little-endian: El qubit 0 es el menos significativo (cambia más rápido). En un sistema de 3 qubits, los índices 0,1,2,3,4,5,6,7 corresponden a |000⟩, |001⟩, |010⟩, |011⟩, |100⟩, |101⟩, |110⟩, |111⟩.

Big-endian: El qubit 0 es el más significativo (cambia más lento).

Cuando seleccionas elementos como A[1::2], estás practicando la habilidad de pensar en patrones de bits y posiciones, exactamente lo que necesitas para entender qué significa aplicar una operación a un qubit específico.

4. Operaciones In-Place: Eficiencia en Simulaciones
Tu código modifica el array original con A[1::2] = -1 (operación in-place).

En computación cuántica: Cuando simulas un circuito cuántico con muchos qubits, los arrays son enormes. Crear copias constantemente sería prohibitivamente costoso en memoria y tiempo. Las simulaciones eficientes siempre modifican los arrays in-place siempre que es posible. Este hábito de pensar en modificación directa es esencial para escribir simuladores cuánticos eficientes.

5. Comprensión de la Paridad y la Simetría
El concepto de "posiciones pares" (índices 1,3,5,7,9) que usas está relacionado con la paridad de los índices.

En computación cuántica: La paridad es fundamental en códigos de corrección de errores (códigos de paridad) y en la detección de ciertos tipos de errores (como errores de bit-flip). Poder manipular estados basándose en la paridad de sus índices es una habilidad práctica importante.

6. Preparación Eficiente de Estados Iniciales
Para muchas simulaciones cuánticas, necesitas preparar estados iniciales específicos. El slicing con asignación es una forma extremadamente eficiente de hacerlo:

python
# Ejemplo: Crear un estado de 3 qubits con amplitudes en índices pares = 0.5, impares = 0
estado = np.zeros(8, dtype=complex)
estado[0::2] = 0.5  # Asigna 0.5 a índices 0,2,4,6
estado[1::2] = 0.0  # Asigna 0 a índices 1,3,5,7
En resumen: Este ejercicio te ha enseñado a generar secuencias con patrones (múltiplos de 3) y a modificar selectivamente subconjuntos de un array usando slicing con paso. Estas habilidades se traducen directamente en la capacidad de preparar estados cuánticos con simetrías específicas, aplicar operaciones a qubits particulares, y escribir simulaciones eficientes que modifiquen grandes vectores de estado sin crear copias innecesarias. Estás aprendiendo a "hablar" el lenguaje de los índices y patrones, que es el lenguaje de los estados cuánticos.





'''