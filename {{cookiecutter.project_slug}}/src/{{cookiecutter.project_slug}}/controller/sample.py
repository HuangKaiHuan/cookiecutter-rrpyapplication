"""
sample controller file
"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from {{cookiecutter.project_slug}} import __version__, setting
from {{cookiecutter.project_slug}}.model.sample import SampleModel
from {{cookiecutter.project_slug}}.view.sample import Ui_SampleView


class SampleController(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SampleController, self).__init__(parent)
        self._ui = Ui_SampleView()
        self._ui.setupUi(self)

        self._model = SampleModel()

        self.setWindowIcon(QIcon(setting.INPUT_PATH.joinpath("sample.ico").as_posix()))
        self._ui.label_version.setText(__version__)

    def show_random(self):
        change_log = self._model.get_change_log()
        QtWidgets.QMessageBox.information(self, "修改日志", change_log)
