'''
Genera una array unidimensional de Numpyque tenga los enteros del 0 al 9 utilizando
np.arange(). A continuación, calcule la suma de elementos con np.sum() y muestre el resultado
por consola.
'''
# Importamos la librería NumPy, la herramienta fundamental para cálculo numérico en Python.
# En computación cuántica, la usaremos para representar vectores (estados) y matrices (operadores).
import numpy as np

# Creamos un array unidimensional (un vector) con los enteros del 0 al 9.
# np.arange(10) genera una secuencia: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# En computación cuántica, este array podría ser un paso inicial para crear un estado base |0>, |1>, etc.,
# aunque normalmente trabajaremos con números complejos.
a = np.arange(10)

# Calculamos la suma de todos los elementos del array 'a'.
# np.sum() es una función de agregación muy útil.
s = np.sum(a)

# Imprimimos el resultado de forma legible. La salida será:
# "La suma del array [0 1 2 3 4 5 6 7 8 9] es: 45"
print("La suma del array {} es: {}".format(a, s))

'''
El Valor de Este Código para la Computación Cuántica
A simple vista, este código parece de nivel muy básico, pero sus conceptos son los bloques de construcción
de casi todo lo que harás en simulaciones de computación cuántica con Python. 
Aquí te detallo por qué es importante:

1. Familiarización con NumPy
El estándar de la industria: Casi todas las librerías de computación cuántica en Python (como Qiskit, Cirq, PennyLane) están construidas sobre NumPy.
 Dominar np.array() es como aprender a sostener el bolígrafo antes de escribir.

Eficiencia: NumPy está escrito en C y Fortran por detrás, lo que lo hace extremadamente rápido para operaciones con vectores y matrices. Esto es crucial, 
ya que simular unos pocos qubits implica multiplicar matrices de 2ⁿ x 2ⁿ, que crecen exponencialmente.

2. Concepto de Vectores (Qubits)
En computación cuántica, el estado de un qubit se representa como un vector.

Un qubit en el estado |0> se representa como [1, 0].

Un qubit en el estado |1> se representa como [0, 1].

Una superposición, como |+>, se representa como [1/√2, 1/√2] (aproximadamente [0.707, 0.707]).

Tu array [0, 1, 2, ...] es un vector numérico. Aunque no es un estado cuántico válido
 (porque no está normalizado), te acostumbra a la idea de manipular colecciones de números como una sola entidad.

3. Concepto de Operaciones (Suma)
np.sum() es una operación que se aplica a todo el vector de una vez. En computación cuántica, harás esto constantemente.

Cálculo de probabilidades: Cuando tienes un vector de estado (por ejemplo, el resultado de una simulación),
 a menudo querrás sumar las probabilidades de ciertos resultados. Esto implicaría elevar al cuadrado los elementos y luego sumarlos (usando np.sum()).

Valores esperados: Para calcular el valor esperado de un operador (como una matriz de Pauli), realizarás operaciones que terminan en una suma.

4. Base para Operaciones más Complejas
Una vez que domines np.arange() y np.sum(), el siguiente paso natural para computación cuántica es:

Usar números complejos: estado = np.array([1+0j, 0+0j])

Calcular la norma de un vector (para verificar que está normalizado): norma = np.sqrt(np.sum(estado * np.conj(estado)))

Multiplicar matrices (puertas cuánticas) por vectores (estados): nuevo_estado = np.dot(puerta_Hadamard, estado_qubit)

En resumen: Este código es tu primer paso. Aunque no resuelve un problema cuántico directamente, establece las bases de la herramienta (NumPy) y el paradigma (operaciones vectoriales) que usarás para simular y entender el mundo cuántico.

'''
