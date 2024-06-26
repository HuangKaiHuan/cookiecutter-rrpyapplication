#!/usr/bin/env python
import os
from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path(os.path.realpath(os.path.curdir))


def remove_dir(dir_):
    shutil.rmtree(PROJECT_DIRECTORY.joinpath(dir_).as_posix())

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

    move_file("requirements/py{{ cookiecutter.python_version|replace('.', '') }}.txt", "requirements.txt")
    remove_dir("requirements")

    print("""
    ################################################################################
    ################################################################################
        You have successfully created `{{ cookiecutter.project_name }}`.
    ################################################################################
        You've used these cookiecutter parameters:
    {% for key, value in cookiecutter.items()|sort %}
            {{ "{0:30}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
    {%- endfor %}
    ################################################################################
        To get started run these:
            cd {{ cookiecutter.project_slug }}

            # create virtualenv(recommend)
            python{{ cookiecutter.python_version }} -m venv venv
            source venv/bin/activate # for linux
            venv/Scripts/activate # for windows

            # install dependencies
            python -m pip install -U pip
            python -m pip install -e .

            # auto init the repo by invoke command
            inv init-repo

            # Push to remote repo
            git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.git
            git push -u origin master --tags
    """)
