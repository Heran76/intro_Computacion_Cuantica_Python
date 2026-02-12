
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
    <img src="https://img.shields.io/badge/Qiskit-1.x+- purple?style=for-the-badge&logo=qiskit&logoColor=white" alt="Qiskit"/>
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

## Descripción

Este repositorio recoge un recorrido estructurado y práctico por los fundamentos y aplicaciones de la **computación cuántica** utilizando **Python** como lenguaje principal.

Incluye explicaciones teóricas breves, implementaciones comentadas, visualizaciones y comparación entre las principales bibliotecas del ecosistema en 2026:

- Qiskit (IBM)
- Cirq (Google Quantum AI)
- PennyLane (diferenciación cuántica y QML)

### Temas principales cubiertos

- Fundamentos matemáticos (notación de Dirac, espacios de Hilbert, producto tensorial)
- Puertas cuánticas universales y circuitos básicos
- Representación y visualización en la esfera de Bloch
- Algoritmos cuánticos emblemáticos:
  - Deutsch–Jozsa
  - Grover (búsqueda no estructurada)
  - Shor (factorización) – en desarrollo
  - QAOA y VQE (optimización combinatoria y química cuántica)
  - Otros: Bernstein–Vazirani, Simon, HHL (resolución lineal)
- Simulación local de alta performance vs. ejecución en hardware real
- Programación híbrida cuántico-clásica

---

## Instalación recomendada (2026)

### Requisitos mínimos

- Python ≥ 3.11
- Gestor de entornos: conda (recomendado) o venv + pip

### Opción 1 – Miniconda (más ligera y recomendada)

```bash
# 1. Descargar Miniconda → https://docs.conda.io/en/latest/miniconda.html

# 2. Crear y activar entorno
conda create -n quantum python=3.11 -y
conda activate quantum

# 3. Instalar paquetes principales
conda install jupyter matplotlib numpy scipy -y
pip install --upgrade qiskit qiskit-aer qiskit[visualization] qiskit-ibm-runtime
pip install cirq-core cirq-google pennylane pennylane-lightning

### Opción 2 – 
python -m venv quantum-env
source quantum-env/bin/activate    # Linux/macOS
# quantum-env\Scripts\activate     # Windows

pip install --upgrade pip
pip install jupyter matplotlib numpy scipy
pip install qiskit[all] cirq pennylane
Recomendación de editores/entornos en 2026:

VS Code + extensiones: Jupyter, Python, Pylance, Qiskit
JupyterLab (ideal para notebooks interactivos)
PyCharm Professional (muy buen soporte científico) 