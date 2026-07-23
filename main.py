import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFT

def run_order_finding_subroutine_demo():
    print("--- [KAHANI SHURU]: Quantum Engine Start Ho Raha Hai ---")
    
    # Step 1: Memory Registers banana
    # m_qubits: Precision register (upar wala hissa) jo accuracy rakhega
    # l_qubits: Target register (neeche wala hissa) jo math ki values sambhalega
    m_qubits = 3
    l_qubits = 4 

    qr_control = QuantumRegister(m_qubits, 'precision-control')
    qr_target = QuantumRegister(l_qubits, 'target-state')
    cr_output = ClassicalRegister(m_qubits, 'measurement-result')

    circuit = QuantumCircuit(qr_control, qr_target, cr_output)

    # Step 2: Shuruat karna (Initialization)
    # Target register ko state |1> par set karte hain (X gate ka use karke)
    circuit.x(qr_target[0])
    print("[Step 1] Target register ko |1> par set kar diya gaya hai.")

    # Step 3: Superposition banana (Jaadu)
    # Control register ke sabhi qubits par Hadamard gate (H) lagate hain.
    # Isse computer ek hi waqt par saari possibilities (0 se 2^m - 1) mein ek sath aa jata hai.
    for q in qr_control:
        circuit.h(q)
    print("[Step 2] Hadamard gate lag gaya: Control register mein Superposition ban gaya.")

    # Step 4: Controlled-U Operations (Modular Exponentiation)
    # Yahan hum phase shifts (angles) add karte hain jo quantum rhythm ko represent karte hain.
    for i, control_qubit in enumerate(qr_control):
        power = 2 ** i
        circuit.cp(np.pi / power, control_qubit, qr_target[0])
    print("[Step 3] Controlled-U operations circuit mein jod diye gaye hain.")

    # Step 5: Inverse Quantum Fourier Transform (QFT dagger)
    # Inverse QFT lagate hain taaki galat raste cancel ho jayein aur sahi frequency (s/r) samne aa jaye.
    inv_qft = QFT(m_qubits, inverse=True, do_swaps=True).to_instruction()
    circuit.append(inv_qft, qr_control)
    print("[Step 4] Inverse QFT apply kar diya gaya hai.")

    # Step 6: Measurement (Nateeja dekhna)
    # Control register ko measure karte hain taaki binary fraction (s/r) bahar aa sake.
    circuit.measure(qr_control, cr_output)
    print("[Step 5] Measurement ready hai. Wave function ko collapse karne ke liye.\n")

    return circuit

if __name__ == "__main__":
    my_quantum_circuit = run_order_finding_subroutine_demo()
    print("--- [CIRCUIT KA NAKSHA (ASCII)] ---")
    print(my_quantum_circuit.draw(output='text'))
    