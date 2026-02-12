# Introducción a la Computación Cuántica con Python

<p align="center">
  <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&q=80&w=1200" alt="Fondo abstracto cuántico" width="800"/>
  <br><br>
  <em>Aprendizaje práctico de qubits, circuitos, algoritmos y visualización cuántica mediante Python</em>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://qiskit.org/">
    <img src="https://img.shields.io/badge/Qiskit-1.x+-purple?style=for-the-badge&logo=qiskit&logoColor=white" alt="Qiskit"/>
  </a>
  <a href="https://quantumai.google/cirq">
    <img src="https://img.shields.io/badge/Cirq-supported-blueviolet?style=for-the-badge" alt="Cirq"/>
  </a>
  <a href="https://pennylane.ai/">
    <img src="https://img.shields.io/badge/PennyLane-supported-9f00ff?style=for-the-badge" alt="PennyLane"/>
  </a>
  <br>
  <img src="https://img.shields.io/github/last-commit/TU_USUARIO/intro_Computacion_Cuantica_Python?style=for-the-badge&color=00C853&logo=github&logoColor=white" alt="Última actualización"/>
  <img src="https://img.shields.io/github/stars/TU_USUARIO/intro_Computacion_Cuantica_Python?style=for-the-badge&color=gold" alt="Estrellas"/>
</p>

---

## 📘 Descripción

Este repositorio recoge **mi recorrido personal de investigación y estudio** sobre los fundamentos y aplicaciones de la **computación cuántica**, utilizando **Python** como lenguaje principal.

Incluye explicaciones teóricas breves, implementaciones comentadas, visualizaciones y comparación entre las principales bibliotecas del ecosistema en 2026:

- Qiskit (IBM)
- Cirq (Google Quantum AI)
- PennyLane (diferenciación cuántica y QML)

<p align="center">
  <img src="https://img.freepik.com/foto-gratis/fondo-moderno-lineas-puntos-conexion_1048-7966.jpg" alt="Líneas de conexión cuántica" width="800"/>
  <br>
  <em>Este repositorio documenta mi investigación y estudios personales en computación cuántica</em>
</p>

### 🧠 Temas principales cubiertos

- Fundamentos matemáticos (notación de Dirac, espacios de Hilbert, producto tensorial)
- Puertas cuánticas universales y circuitos básicos
- Representación y visualización en la esfera de Bloch
- Algoritmos cuánticos emblemáticos:
  - Deutsch–Jozsa
  - Grover (búsqueda no estructurada)
  - Shor (factorización) – en desarrollo
  - QAOA y VQE (optimización combinatoria y química cuántica)
  - Bernstein–Vazirani, Simon, HHL (resolución lineal)
- Simulación local de alta performance vs. ejecución en hardware real
- Programación híbrida cuántico-clásica

---

## ⚙️ Instalación recomendada (2026)

### Requisitos mínimos

- Python ≥ 3.11
- Gestor de entornos: conda (recomendado) o venv + pip

---

### 🔹 Opción 1 – Miniconda (más ligera y recomendada)

```bash
# 1. Descargar Miniconda → https://docs.conda.io/en/latest/miniconda.html

# 2. Crear y activar entorno
conda create -n quantum python=3.11 -y
conda activate quantum

# 3. Instalar paquetes principales
conda install jupyter matplotlib numpy scipy -y
pip install --upgrade qiskit qiskit-aer qiskit[visualization] qiskit-ibm-runtime
pip install cirq-core cirq-google pennylane pennylane-lightning


```
---
### 🔸 Opción 2 – Entorno virtual con venv


bash
# Crear entorno
python -m venv quantum-env

# Activar (elige según tu sistema)
# Linux / macOS:
source quantum-env/bin/activate
# Windows:
# quantum-env\Scripts\activate

# Actualizar pip e instalar
pip install --upgrade pip
pip install jupyter matplotlib numpy scipy
pip install qiskit[all] cirq pennylane

## 📦 Bibliotecas del ecosistema
### Bibliotecas de computación convencional

pip install numpy==2.3.1  
*Librería fundamental para cálculo numérico y álgebra lineal*

pip install matplotlib==3.10.1  
*Visualización de datos y gráficos*

pip install gymnasium==1.2.0  
*Entornos para aprendizaje por refuerzo*

pip install gymnasium[classic-control]==1.2.0  
*Entornos clásicos de control para aprendizaje por refuerzo*

### Bibliotecas de desarrollo software cuántico

pip install qiskit==2.1.1  
*Framework principal de IBM para computación cuántica. Permite construir circuitos y puertas cuánticas*

pip install qiskit[visualizacion]==2.1.1  
*Utilidades de visualización: diagramas de circuitos, histogramas, esfera de Bloch*

pip install qiskit_aer==0.17.1  
*Simulador local de alto rendimiento. Necesario porque la mayoría no tenemos ordenador cuántico real*

pip install pyqubo==1.5.0  
*Para formular problemas de optimización combinatoria en formato QUBO. Útil para algoritmos como QAOA y VQE*

pip install qiskit-ibm-runtime==0.40.1  
*Para ejecutar algoritmos en simuladores reales y hardware cuántico de IBM vía cloud*

📌 Nota personal
Este repositorio es mi espacio de experimentación y documentación personal en computación cuántica.
No es un curso cerrado ni una guía estática: evoluciona conmigo a medida que avanzo en mi investigación y comprensión del campo.

“La mejor manera de aprender es construir y compartir.”

📄 Licencia
MIT © [Antonio Heredia Morante] – 2026