"""
sample model file
"""

from {{cookiecutter.project_slug}} import setting


class SampleModel(object):
    def __init__(self):
        pass

    def get_change_log(self):
        with open(setting.CHANGE_LOG_PATH, encoding="utf-8") as f:
            change_log = f.readlines()
        return "".join(change_log)
