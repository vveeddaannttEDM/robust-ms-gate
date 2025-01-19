from qiskit.providers.aer import AerSimulator  
from qiskit.providers.aer.noise import NoiseModel, amplitude_damping_error, phase_damping_error, depolarizing_error  

def create_noise_model():  
    """  
    Create a noise model for symmetric and asymmetric errors compatible with Qiskit 1.3.1.  
    """  
    noise_model = NoiseModel()  
    
    # Symmetric error: Amplitude damping (represents motional mode noise)  
    symmetric_error = amplitude_damping_error(0.01)  # Damping probability  
    noise_model.add_all_qubit_quantum_error(symmetric_error, ['rxx'])  
    
    # Asymmetric error: Phase damping (represents qubit frequency drift)  
    asymmetric_error = phase_damping_error(0.01)  # Damping probability  
    noise_model.add_all_qubit_quantum_error(asymmetric_error, ['rxx'])  
    
    # Depolarizing error to represent general noise  
    depolarizing = depolarizing_error(0.01, 2)  # 2-qubit depolarizing error  
    noise_model.add_all_qubit_quantum_error(depolarizing, ['rxx'])  
    
    return noise_model