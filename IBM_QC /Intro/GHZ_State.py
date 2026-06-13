#Creación de un estado de Bell
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import EstimatorOptions
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from matplotlib import pyplot as plt
# Uncomment the next line if you want to use a simulator:
from qiskit_ibm_runtime.fake_provider import FakeBelemV2

# Crear un circuito cuántico de dos cúbits:
qc = QuantumCircuit(2)

# Aplicar una Hadamard al cúbit 0:
qc.h(0)

# Aplicar una CNOT en el cúbit 1 con el 0 como control:
qc.cx(0, 1)

# Devolver un dibujo del circuito usando MatPlotLib ("mpl")
qc.draw("mpl")
plt.show()

# Definición de observables:

observables_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
observables = [SparsePauliOp(label) for label in observables_labels]

# Optimización de circuitos y operadores (backend1 para simulación y backend2 para hardware real)
service = QiskitRuntimeService()
#Simulador
backend= FakeBelemV2()
#Real
backend2 = service.least_busy(simulator=False, operational=True)

    # Convertir a un circuito ISA
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

isa_circuit.draw("mpl", idle_wires=False)
plt.show()

# Construimos la instancia Estimator

estimator = Estimator(mode=backend)
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000

mapped_observables = [
    observable.apply_layout(isa_circuit.layout) for observable in observables
]

# Corremos el circuito midiendo los observables
job = estimator.run([(isa_circuit, mapped_observables)])

#Usamos el job ID para recuperar los datos más tarde
print(f">>> Job ID: {job.job_id()}")

#Este es el resultado del trabajo. Al subir un Pub, se da un único resultado acompañado de meta-datos propios.
job_result = job.result()

#Este es el resultado con la información de los seis observables
pub_result = job.result()[0]

# Analisis de resultados
# Ploteamos el resultado
values = pub_result.data.evs
errors = pub_result.data.stds

plt.plot(observables_labels, values, "-o")
plt.xlabel("Observables")
plt.ylabel("Valores")
plt.show()

# Escalar a un gran número de cúbits:
def get_qc_for_n_qubit_GHZ_state(n:int) -> QuantumCircuit:
    """Esta función crea un qiskit.QuantumCircuit (qc) para generar el estado GHZ de n cúbits, asumiendo que todos empiezan en el estado |0>.

    Args:
        n (int): Número de cúbits para el estado GHZ.

    Returns:
        QuantumCirquit: Circuito cuántico que genera el estado GHZ de n cúbits.
    """
    if isinstance(n, int) and n >= 2:
        qc = QuantumCircuit (n)
        qc.h(0)
        for i in range(n-1):
            qc.cx(i, i + 1)
    else:
        raise Exception("n no es un input válido.")
    return qc

# Creamos un circuito de 100 cúbits en el estado GHZ.
n = 100
qc = get_qc_for_n_qubit_GHZ_state(n)

# Definimos los observables

operator_strings = [
    "Z" + "I" * i + "Z" + "I" * (n - 2 -i) for i in range(n - 1)
]

operators = [SparsePauliOp(operator) for operator in operator_strings]

# Transformación a ISA

service = QiskitRuntimeService()

backend3 = service.least_busy(
    simulator=False, operational=True, min_num_qubits=100
)
pm = generate_preset_pass_manager(optimization_level=1, backend=backend3)
isa_circuit= pm.run(qc)
isa_operators_list = [op.apply_layout(isa_circuit.layout) for op in operators]

# Ejecución en hardware:

options = EstimatorOptions()
options.resilience_level = 1
options.dynamical_decoupling.enable = True
options.dynamical_decoupling.sequence_type = "XY4"

estimator = Estimator(backend3, options=options) # Creamos un objeto estimador
# Enviamos el circuito al estimador
job = estimator.run([(isa_circuit, isa_operators_list)])
job_id = job.job_id()
print(job_id)

# Resultados
data = list(range(1,len(operators) + 1))
result = job.result()[0]
values = result.data.evs
values = [
    v / values[0] for v in values
] # Normaliza el valor esperado para evaluar cómo decae con la distancia.
#Plot
plt.plot(data, values, marker= "o", label = "Estado GHZ de 100 cúbits")
plt.xlabel("Distancia entre cúbits $i$")
plt.ylabel(r"$\langle Z_i Z_0 \rangle / \langle Z_1 Z_0 \rangle $")
plt.legend()
plt.show()
