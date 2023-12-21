import DiscountPolicy, Money
class AmountDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_amount: Money, *conditions):
        super().__init__(*conditions)
        self.discount_amount = discount_amount

    def get_discount_amount(self, screening) -> Money:
        return self.discount_amount
