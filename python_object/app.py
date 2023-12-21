from datetime import timedelta
from Money import Money
from Movie import Movie
from SequenceCondition import SequenceCondition
avatar = Movie(title='아바타',running_time=timedelta(minutes=120),fee=Money.wons(800),discount_policy=[SequenceCondition(1),SequenceCondition(10)])
print(avatar.running_time)