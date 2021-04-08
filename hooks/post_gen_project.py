#!/usr/bin/env python
import os
from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    os.remove(PROJECT_DIRECTORY.joinpath(filepath).as_posix())


def move_file(src, dst):
    shutil.move(PROJECT_DIRECTORY.joinpath(src), PROJECT_DIRECTORY.joinpath(dst))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")

    if "{{cookiecutter.gitlab_ci}}" != "y":
        remove_file(".gitlab-ci.yml")

    if "{{cookiecutter.pyinstaller_bundle_to}}" == "one-file":
        remove_file("one-folder.spec")
        move_file("one-file.spec", "{{ cookiecutter.project_slug }}.spec")
    else:
        remove_file("one-file.spec")
        move_file("one-folder.spec", "{{ cookiecutter.project_slug }}.spec")
