from {{ cookiecutter.project_slug }}.models.calculator_model import CalculatorModel, Operation
from {{ cookiecutter.project_slug }}.utils.core import catch_except
from {{ cookiecutter.project_slug }}.views.calculator_view import CalculatorView


class CalculatorPresenter:
    def __init__(self, view: CalculatorView, model: CalculatorModel):
        self._view = view
        self._model = model

        self._view.set_optional_operation(Operation.member_values())

        self._view.signal_calc_pressed.connect(self.calc)

    @catch_except
    def calc(self):
        x1 = self._view.get_value_1()
        x2 = self._view.get_value_2()
        operation = self._view.get_operation()
        result = self._model.calc(float(x1), Operation(operation), float(x2))

        self._view.set_result(result)
