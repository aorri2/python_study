from abc import ABC, abstractmethod

class DiscountCondition(ABC):
    @abstractmethod
    def is_satisfied_by(self, screening) -> bool:
        pass
