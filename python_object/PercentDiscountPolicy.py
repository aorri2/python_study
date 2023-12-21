import DiscountPolicy,Money

class PercentDiscountPolicy(DiscountPolicy):
    def __init__(self, percent: float, *conditions):
        super().__init__(*conditions)
        self.percent = percent

    def get_discount_amount(self, screening) -> Money:
        return screening.get_movie_fee().times(self.percent)
