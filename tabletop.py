class TableTop:

    def __init__(self, lower_limit_coordinates, upper_limit_coordinates):
        self.lower_limit = lower_limit_coordinates
        self.upper_limit = upper_limit_coordinates

    def contains(self, point) -> bool:
        return self.lower_limit <= point <= self.upper_limit

