from  .Reservation import Reservation


class Screening:
    """
    A class representing a screening of a movie.
    """

    def __init__(self, movie, sequence, when_screened):
        """
        Initialize a new Screening instance.
        :param movie: The Movie object.
        :param sequence: The sequence number of the screening.
        :param when_screened: The datetime when the movie is screened.
        """
        self.movie = movie
        self.sequence = sequence
        self.when_screened = when_screened

    def get_start_time(self):
        """
        Return the start time of the screening.
        """
        return self.when_screened

    def is_sequence(self, sequence):
        """
        Check if the given sequence matches the screening's sequence.
        :param sequence: The sequence number to check.
        :return: True if matches, False otherwise.
        """
        return self.sequence == sequence

    def get_movie_fee(self):
        """
        Return the fee of the movie.
        """
        return self.movie.get_fee()

    def reserve(self, customer, audience_count):
        """
        Reserve a screening for a customer.
        :param customer: The Customer object.
        :param audience_count: The number of audiences.
        :return: A new Reservation object.
        """
        return Reservation(customer, self, self.calculate_fee(audience_count), audience_count)

    def _calculate_fee(self, audience_count):
        """
        Calculate the total fee for the given number of audiences.
        :param audience_count: The number of audiences.
        :return: The total fee.
        """
        return self.movie.calculate_movie_fee(self).times(audience_count)
        
    