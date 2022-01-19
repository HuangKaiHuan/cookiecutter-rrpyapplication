from unittest import mock

from {{ cookiecutter.project_slug }}.presenters.calculator_presenter import (
    CalculatorModel,
    CalculatorPresenter,
    CalculatorView,
    Operation,
)


class TestCalculatorPresenter:
    def setup(self):
        self.view = mock.create_autospec(CalculatorView)
        self.view.signal_calc_pressed = mock.Mock()
        self.view.signal_sub_pressed = mock.Mock()
        self.view.get_value_1 = mock.Mock(return_value=2)
        self.view.get_value_2 = mock.Mock(return_value=1)
        self.view.get_operation = mock.Mock(return_value=Operation.ADD)

        self.model = CalculatorModel()
        self.presenter = CalculatorPresenter(self.view, self.model)

    def test_calc(self):
        self.presenter.calc()

        self.view.get_value_1.assert_called_once()
        self.view.get_value_2.assert_called_once()
        self.view.get_operation.assert_called_once()
        self.view.set_result.assert_called_once_with(3)
