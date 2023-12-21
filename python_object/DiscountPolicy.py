from abc import ABC, abstractmethod
from typing import List
from  .DiscountCondition import DiscountCondition

from  .Money import Money

class DiscountPolicy(ABC):
    def __init__(self, *conditions):
        self.conditions: List[DiscountCondition] = list(conditions)

    def calculate_discount_amount(self, screening) -> Money:
        for each in self.conditions:
            if each.is_satisfied_by(screening):
                return self.get_discount_amount(screening)
        return Money.ZERO

    @abstractmethod
    def get_discount_amount(self, screening) -> Money:
        pass
