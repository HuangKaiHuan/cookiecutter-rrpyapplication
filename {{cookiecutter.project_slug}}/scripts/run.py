import sys

import PyQt5.QtWidgets

from {{ cookiecutter.project_slug }}.controller.sample import SampleController


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    controller = SampleController()
    controller.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
