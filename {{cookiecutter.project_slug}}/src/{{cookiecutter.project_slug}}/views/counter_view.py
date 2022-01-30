from PyQt5 import QtCore, QtWidgets

from .ui import counter_ui


class CounterView(QtWidgets.QWidget):
    signal_add_pressed = QtCore.pyqtSignal()
    signal_sub_pressed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CounterView, self).__init__(parent)

        self._ui = counter_ui.Ui_Form()
        self._ui.setupUi(self)

        self._ui.pushButton_add.pressed.connect(lambda: self.signal_add_pressed.emit())
        self._ui.pushButton_sub.pressed.connect(lambda: self.signal_sub_pressed.emit())

    def set_count(self, value):
        self._ui.lineEdit_count.setText(str(value))
