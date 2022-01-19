from {{ cookiecutter.project_slug }}.models.counter_model import CounterModel


class TestCounterModel:
    def setup(self):
        self.counter = CounterModel()

    def test_increment(self):
        count = self.counter.count
        self.counter.increment()
        assert self.counter.count == count + 1

    def test_decrement(self):
        count = self.counter.count
        self.counter.decrement()
        assert self.counter.count == count - 1
