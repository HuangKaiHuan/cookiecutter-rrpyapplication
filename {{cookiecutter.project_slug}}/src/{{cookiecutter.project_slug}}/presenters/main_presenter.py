from {{ cookiecutter.project_slug }}.models.calculator_model import CalculatorModel
from {{ cookiecutter.project_slug }}.models.counter_model import CounterModel
from {{ cookiecutter.project_slug }}.views.main_view import MainView

from .calculator_presenter import CalculatorPresenter
from .counter_presenter import CounterPresenter


class MainPresenter:
    def __init__(
        self,
        view: MainView,
        calculator_model: CalculatorModel,
        counter_model: CounterModel,
    ):
        self._view = view
        self._calculator_model = calculator_model
        self._counter_model = counter_model

        self._calculator_presenter = CalculatorPresenter(
            self._view.calculator_view, self._calculator_model
        )
        self._counter_presenter = CounterPresenter(
            self._view.counter_view, self._counter_model
        )

        self._view.set_window_title("Passive View")
