from decimal import Decimal

class Money:
    ZERO = None  # 클래스 변수는 아래에서 정의됩니다.

    def __init__(self, amount: Decimal):
        self.amount = amount

    @classmethod
    def wons(cls, amount: float) -> 'Money':
        return cls(Decimal(str(amount)))

    def plus(self, other: 'Money') -> 'Money':
        return Money(self.amount + other.amount)

    def minus(self, other: 'Money') -> 'Money':
        return Money(self.amount - other.amount)

    def times(self, percent: float) -> 'Money':
        return Money(self.amount * Decimal(str(percent)))

    def is_less_than(self, other: 'Money') -> bool:
        return self.amount < other.amount

    def is_greater_than_or_equal(self, other: 'Money') -> bool:
        return self.amount >= other.amount

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __str__(self):
        return f"{str(self.amount)}원"

# 클래스 변수를 정의합니다.
Money.ZERO = Money.wons(0)