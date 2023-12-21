class SequenceCondition:
    def __init__(self, sequence: int):
        self.sequence = sequence

    def is_satisfied_by(self, screening) -> bool:
        return screening.is_sequence(self.sequence)
