<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Bloch_sphere.svg" alt="Bloch Sphere" width="380"/>
  &nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_circuit.jpg" alt="Quantum Circuit" width="380"/>
  <br>
  <small>Imágenes en CC0 – Wikimedia Commons (libre de derechos)</small>
</p>

<p align="center">
  <i>Explorando el fascinante mundo de los qubits, superposición, entrelazamiento y algoritmos cuánticos mediante código práctico en Python.</i>
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Quantum-Qiskit%20%7C%20Cirq%20%7C%20PennyLane-7C4DFF?style=for-the-badge" alt="Frameworks"/>
  <img src="https://img.shields.io/github/last-commit/TU_USUARIO/intro_Computacion_Cuantica_Python?style=for-the-badge&color=00C853" alt="Último commit"/>
</p>

---

### 🌌 ¿Qué encontrarás aquí?

Este repositorio documenta mi viaje personal de aprendizaje y experimentación en **computación cuántica** usando **Python**. Desde conceptos fundamentales hasta implementaciones prácticas de algoritmos cuánticos, todo explicado paso a paso con código ejecutable.

**Temas principales que estoy explorando:**

- Fundamentos: qubits, superposición, entrelazamiento, medición
- Puertas cuánticas y circuitos básicos
- La esfera de Bloch y visualización de estados
- Algoritmos clásicos cuánticos: Deutsch–Jozsa, Grover, Shor (en progreso), QAOA, VQE...
- Simuladores locales vs. ejecución en hardware real
- Bibliotecas modernas: Qiskit, Cirq, PennyLane, OpenQASM...

<p align="center">
  <img src="https://i.sstatic.net/nZWsR.png" alt="Bloch sphere entangled state" width="380"/>
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*dyiFT95MfMtkgdhddnPuSA.jpeg" alt="Bloch sphere visualization" width="380"/>
  <br>
  <small>Ejemplos de visualización en la esfera de Bloch</small>
</p>

### 🛠️ Tecnologías y herramientas que utilizo

| Biblioteca     | Uso principal                          | Estado en el repo     |
|----------------|----------------------------------------|------------------------|
| **Qiskit**     | Circuitos, simulación, hardware IBM    | ★★★ Muy activo        |
| **Cirq**       | Enfoque en NISQ, Google Quantum AI     | ★★ En exploración     |
| **PennyLane**  | Quantum Machine Learning, diferenciación | ★★ En progreso      |
| **matplotlib** / **plotly** | Visualizaciones (Bloch, histogramas) | ★★★ Siempre presente |
| **numpy**      | Álgebra lineal y estados cuánticos     | ★★★ Base             |

### 📂 Estructura del repositorio (actual → 2026)

```text
intro_Computacion_Cuantica_Python/
├── 01_Fundamentos/
│   ├── 01_Qué_es_un_qubit.ipynb
│   ├── 02_Superposición_y_Hadamard.ipynb
│   └── 03_Entrelazamiento_Bell.ipynb
├── 02_Puertas_y_Circuitos/
│   ├── 01_Puertas_básicas.ipynb
│   └── 02_Circuitos_multiples_qubits.ipynb
├── 03_Algoritmos/
│   ├── Deutsch-Jozsa/
│   ├── Grover/
│   └── Variacionales_(QAOA_VQE)/
├── 04_Visualización/
│   └── Esfera_de_Bloch_y_otros_plots/
├── experiments/          ← pruebas rápidas y locas
├── requirements.txt
├── .gitignore
└── README.md             ← tú estás aquí ✦