class CounterModel:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count = self._count + 1

    def decrement(self):
        self._count = self._count - 1

    @property
    def count(self):
        return self._count
