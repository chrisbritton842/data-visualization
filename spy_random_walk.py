import numpy.random as r

class SpyRandomWalk:
    """A class to generate random walks for SPY."""

    def __init__(self, num_years=1):
        self.num_years = num_years
        self.num_days = 252 * num_years

        # All walks start at (0, 0).
        self.x_values = range(self.num_days)
        self.y_values = [100]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values) < self.num_days:

            # Decide which direction to go and how far to go in that direction.
            y_percent = r.normal(0, 0.014, 1)

            # Calculate the new price.
            last = self.y_values[-1]
            y = last + y_percent * last

            self.y_values.append(y)
