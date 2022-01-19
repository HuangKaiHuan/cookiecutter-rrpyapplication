from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

from .calculator_view import CalculatorView
from .counter_view import CounterView
from .ui import main_ui


class MainView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._calculator_view = CalculatorView(self)
        self._counter_view = CounterView(self)

        self._ui = main_ui.Ui_Form()
        self._ui.setupUi(self)

        self._ui.gridLayout_3.addWidget(self._calculator_view)
        self._ui.gridLayout_2.addWidget(self._counter_view)

    def set_tab_counter_content(self, view):
        self._ui.tab_counter.layout.addWidget(view)

    def set_tab_calculator_content(self, view):
        self._ui.tab_calculator.layout.addWidget(view)

    def set_window_title(self, title: str):
        self.setWindowTitle(title)

    @property
    def calculator_view(self):
        return self._calculator_view

    @property
    def counter_view(self):
        return self._counter_view

    def to_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            int(screen.width() - size.width()) // 2,
            int(screen.height() - size.height()) // 2,
        )
