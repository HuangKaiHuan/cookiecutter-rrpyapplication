from PyQt5.QtWidgets import QMessageBox

__all__ = ["catch_except"]


# TODO: 可以抽象得更通用一些
def catch_except(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, "错误", str(e))
            msg_box.show()
            msg_box.exec_()

    return wrapper
