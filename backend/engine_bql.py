from qiskit import QuantumCircuit, Aer, execute
import strawberryfields as sf
from strawberryfields.ops import Dgate, BSgate, MeasureFock

class BQLHybridEngine:
    def __init__(self):
        self.sf_eng = sf.Engine('fock', backend_options={"cutoff_dim": 5})

    def run_script(self, commands):
        output = []
        for cmd in commands:
            if cmd.upper() == "RUN_QISKIT":
                output.append(self.run_qiskit())
            elif cmd.upper() == "RUN_STRAWBERRY":
                output.append(self.run_strawberry())
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

    def run_strawberry(self):
        prog = sf.Program(2)
        with prog.context as q:
            Dgate(1.0) | q[0]
            Dgate(1.0) | q[1]
            BSgate() | (q[0], q[1])
            MeasureFock() | q
        result = self.sf_eng.run(prog)
        return {"StrawberryResult": result.samples.tolist()}

