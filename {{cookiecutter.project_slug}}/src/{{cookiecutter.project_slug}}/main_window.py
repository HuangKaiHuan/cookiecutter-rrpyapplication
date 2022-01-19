from {{ cookiecutter.project_slug }}.models.calculator_model import CalculatorModel
from {{ cookiecutter.project_slug }}.models.counter_model import CounterModel
from {{ cookiecutter.project_slug }}.presenters.main_presenter import MainPresenter
from {{ cookiecutter.project_slug }}.views.main_view import MainView


class MainWindow:
    def __init__(self):
        calculator_model = CalculatorModel()
        counter_model = CounterModel()
        self.view = MainView()
        self.presenter = MainPresenter(self.view, calculator_model, counter_model)

    def show(self):
        self.view.to_center()
        self.view.show()
