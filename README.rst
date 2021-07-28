============================
Cookiecutter RRPyApplication
============================

Cookiecutter_ template for a RR Python application.

- repo: https://github.com/HuangKaiHuan/cookiecutter-rrpyapplication.git

Notes:

- Support python3.6+ only
- If you have a library(not a application) you might want to take a look at RRPyLibrary_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _RRPyLibrary: https://github.com/HuangKaiHuan/cookiecutter-rrpylibrary.git

Features
========

- Formatting with black_
- Import sorting with isort_
- Static typing with mypy_
- Linting with flake8_
- Linting commit message with gitlint_
- Git hooks that run all the above with pre-commit_
- Managing a recorded version number with versioneer_
- Generate changelog from git commit message with gitchanglog_
- Managing dev task with invoke_
- Testing with pytest_
- Protect python codebase with Cython_
- Bundles application with Pyinstaller_
- Continuous Integration with gitlab-ci_ (optional)

.. _black: https://black.readthedocs.io/en/stable/index.html
.. _isort: https://pycqa.github.io/isort/
.. _mypy: https://mypy.readthedocs.io/en/stable/index.html
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _pre-commit: https://pre-commit.com/
.. _versioneer: https://github.com/python-versioneer/python-versioneer
.. _gitlint: https://jorisroovers.com/gitlint/
.. _gitchanglog: https://github.com/vaab/gitchangelog
.. _invoke: https://www.pyinvoke.org/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Cython: https://cython.readthedocs.io/en/latest/
.. _Pyinstaller: https://pyinstaller.readthedocs.io/en/stable/
.. _gitlab-ci: https://docs.gitlab.com/ee/ci/


Quickstart
==========

::

    # Install pipx if cookiecutter are not installed
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath

    # Use cookiecutter to create project from this template
    pipx run cookiecutter gh:HuangKaiHuan/cookiecutter-rrpyapplication

    # cd to the project root
    cd existing_folder

    # create virtualenv(recommend)
    python3 -m venv venv
    source venv/bin/activate

    # install dependencies
    pip install -U pip
    pip install -e .

    # auto init the repo by invoke command
    inv init-repo

    # or you can run command step by step
    git init
    git add .
    git commit -m "chore: First commit"
    git tag $your_version
    pre-commit install -t pre-commit
    pre-commit install -t pre-push
    pre-commit install -t commit-msg

    # Push to remote repo
    create a repo and put it there.
    git remote add origin git@$repo_hosting_domain:$repo_username/$project_name.git
    git push -u origin master

Developing the project
======================

You should read `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ before doing a commit.

To run the tests, just run::

    inv test

To run all check::

    pre-commit run -a

Version management
==================

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

* ``inv bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``inv bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``inv bumpversion major`` to increase version from `1.0.0` to `2.0.0`.
* ``inv bumpversion auto`` to auto increase version.

At the same time, it will auto update the changelog.

Building and Bundles
======================

    inv freeze

