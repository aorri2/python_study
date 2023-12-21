from datetime import date, time

class PeriodCondition:
    def __init__(self, day_of_week: int, start_time: time, end_time: time):
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    def is_satisfied_by(self, screening) -> bool:
        screening_start = screening.get_start_time()
        return (screening_start.weekday() == self.day_of_week and
                self.start_time <= screening_start.time() <= self.end_time)
