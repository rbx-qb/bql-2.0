from qiskit import QuantumCircuit, Aer, execute

class BQLHybridEngine:
    def run_script(self, commands):
        output = []
        for cmd in commands:
            if cmd.upper() == "RUN_QISKIT":
                output.append(self.run_qiskit())
            else:
                output.append({"info": f"Unknown command: {cmd}"})
        return output

    def run_qiskit(self):
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()
        backend = Aer.get_backend('qasm_simulator')
        result = execute(qc, backend, shots=1024).result()
        counts = result.get_counts()
        return {"QiskitResult": counts}
