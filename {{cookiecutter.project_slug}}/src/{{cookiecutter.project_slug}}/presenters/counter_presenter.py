from {{ cookiecutter.project_slug }}.models.counter_model import CounterModel
from {{ cookiecutter.project_slug }}.utils.core import catch_except
from {{ cookiecutter.project_slug }}.views.counter_view import CounterView


class CounterPresenter:
    def __init__(self, view: CounterView, model: CounterModel):
        self._view = view
        self._model = model

        self._view.signal_add_pressed.connect(self.add)
        self._view.signal_sub_pressed.connect(self.sub)

        self._view.set_count(self._model.count)

    @catch_except
    def add(self):
        self._model.increment()
        self._view.set_count(self._model.count)

    @catch_except
    def sub(self):
        self._model.decrement()
        self._view.set_count(self._model.count)
