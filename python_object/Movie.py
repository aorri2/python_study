from datetime import timedelta
from  Money import Money
class Movie:
    def __init__(self, title: str, running_time: timedelta, fee: Money, discount_policy):
        self.title = title
        self.running_time = running_time
        self.fee = fee
        self.discount_policy = discount_policy

    def get_fee(self) -> Money:
        return self.fee

    def calculate_movie_fee(self, screening) -> Money:
        return self.fee.minus(self.discount_policy.calculate_discount_amount(screening))
