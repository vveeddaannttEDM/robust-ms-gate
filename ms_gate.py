from qiskit import QuantumCircuit
import numpy as np

def ms_gate(phi):
    """
    Creates a two-qubit Mølmer-Sørensen (MS) gate with phase phi.
    """
    qc = QuantumCircuit(2)
    # Apply Rx rotations to simulate the interaction
    qc.rxx(phi, 0, 1)
    return qc
