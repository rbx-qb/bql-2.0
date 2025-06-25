# Arquivo: crispr_bql.py

"""
Módulo experimental que integra BQL com aplicações bioinformáticas,
permitindo simulações inspiradas em CRISPR sob ruído quântico.
"""

import numpy as np
from bql.state import BosonicRegister
from bql.ops import apply_noise, distill

class CrisprSimulation:
    def __init__(self, sequence_length, cutoff_dim=5):
        self.sequence_length = sequence_length
        self.cutoff_dim = cutoff_dim
        self.register = BosonicRegister("crispr_seq", cutoff_dim)
        self.base_map = {"A": 0, "T": 1, "C": 2, "G": 3}

    def encode_sequence(self, dna_sequence):
        """Mapeia uma sequência de DNA em estados Fock"""
        for base in dna_sequence[:self.cutoff_dim]:
            idx = self.base_map.get(base.upper(), 0)
            self.register.state[idx] += 0.25
        self.normalize()

    def normalize(self):
        total = sum(self.register.state)
        self.register.state = [x / total for x in self.register.state]

    def simulate_noise(self, noise_level=0.1):
        return apply_noise(self.register, noise_level)

    def simulate_distillation(self):
        return distill(self.register)

    def get_state(self):
        return self.register.as_dict()


# Exemplo de uso
if __name__ == "__main__":
    sim = CrisprSimulation(sequence_length=20, cutoff_dim=5)
    sim.encode_sequence("ACGTACGTACGT")
    print("Estado inicial:", sim.get_state())
    print(sim.simulate_noise(noise_level=0.15))
    print("Após ruído:", sim.get_state())
    print(sim.simulate_distillation())
    print("Após destilação:", sim.get_state())
