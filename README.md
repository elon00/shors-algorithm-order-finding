
# Shor's Algorithm: Quantum Order-Finding Subroutine (QPE)

Welcome to my quantum computing repository! As a software engineering student exploring the next generation of computing, this project implements the core engine of **Shor's Factoring Algorithm**—specifically the **Quantum Order-Finding Subroutine** using **Quantum Phase Estimation (QPE)** in Python with Qiskit.

---

## 🚀 About the Project
Modern digital security (like RSA encryption) relies on the immense difficulty classical computers face when trying to factor large semi-prime numbers. This project simulates the quantum circuit logic that accelerates period/order-finding exponentially by leveraging:
1. **Superposition** (via Hadamard gates)
2. **Controlled-U Modular Arithmetic Operations**
3. **Inverse Quantum Fourier Transform ($QFT^\dagger$)**

---

## 🛠️ Project Structure

```text
shors-algorithm-order-finding/
│
├── venv/                   # Isolated Python virtual environment
├── main.py                 # Core Qiskit script simulating the QPE circuit
└── requirements.txt        # Project dependencies (Qiskit, NumPy)

```

---

## 💻 Getting Started Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/shors-algorithm-order-finding.git](https://github.com/YOUR_USERNAME/shors-algorithm-order-finding.git)
cd shors-algorithm-order-finding

```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv

```

* **Activate on Windows:**
```bash
venv\Scripts\activate

```


* **Activate on Mac/Linux:**
```bash
source venv/bin/activate

```



### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Quantum Circuit Simulation

```bash
python main.py

```

*(This will output the ASCII blueprint of the quantum phase estimation circuit directly to your terminal).*

---

## 📚 Technical Stack

* **Language:** Python
* **Quantum Framework:** Qiskit
* **Mathematical Library:** NumPy

---



```
