from PyQt5 import QtCore, QtWidgets

from .ui import calculator_ui


class CalculatorView(QtWidgets.QWidget):
    signal_calc_pressed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CalculatorView, self).__init__(parent)

        self._ui = calculator_ui.Ui_Form()
        self._ui.setupUi(self)

        self._ui.pushButton_calc.pressed.connect(
            lambda: self.signal_calc_pressed.emit()
        )

    def set_optional_operation(self, operations: list):
        self._ui.comboBox_operator.clear()
        for i, operation in enumerate(operations):
            self._ui.comboBox_operator.addItem("")
            self._ui.comboBox_operator.setItemText(i, operation)

    def get_value_1(self):
        return self._ui.lineEdit_value_1.text()

    def get_value_2(self):
        return self._ui.lineEdit_value_2.text()

    def get_operation(self):
        return self._ui.comboBox_operator.currentText()

    def set_result(self, value):
        self._ui.lineEdit_result.setText(str(value))
