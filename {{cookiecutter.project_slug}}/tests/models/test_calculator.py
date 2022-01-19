import pytest

from {{ cookiecutter.project_slug }}.models.calculator_model import CalculatorModel, Operation


class TestCalculatorModel:
    def setup(self):
        self.calculator = CalculatorModel()

    def test_calc(self):
        assert -1 == self.calculator.calc(1, Operation.SUB, 2)
        assert 3 == self.calculator.calc(2, Operation.ADD, 1)

        pytest.raises(ValueError, self.calculator.calc, 2, "__", 2)
