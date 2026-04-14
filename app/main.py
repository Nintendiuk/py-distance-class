class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def _get_km(self, other):
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other):
        return Distance(self.km + self._get_km(other))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.km += self._get_km(other)
        return self

    def __mul__(self, other):
        if isinstance(other, Distance):
            raise TypeError("Distance does not support multiplication")
        return Distance(self.km * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Distance):
            raise TypeError("Distance does not support division by Distance")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other):
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km < self._get_km(other)

    def __gt__(self, other):
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km > self._get_km(other)

    def __eq__(self, other):
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km == self._get_km(other)

    def __le__(self, other):
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km <= self._get_km(other)

    def __ge__(self, other):
        if not isinstance(other, (Distance, int, float)):
            return NotImplemented
        return self.km >= self._get_km(other)
