from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim).result()
counts = result.get_counts()

print(counts)
