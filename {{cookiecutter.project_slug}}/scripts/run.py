import sys

import PyQt5.QtWidgets

from {{cookiecutter.project_slug}}.main_window import MainWindow


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
