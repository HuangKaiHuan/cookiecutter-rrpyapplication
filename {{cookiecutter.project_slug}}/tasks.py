import shutil
from pathlib import Path

import requests
from invoke import task

import versioneer


@task
def clean(c, docs=False, bytecode=False, extra=""):
    patterns = ["build", "dist", "src/*.egg-info/"]
    if docs:
        patterns.append("docs/_build")
    if bytecode:
        patterns.append("**/*.pyc")
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))


@task
def freeze(c, clean_=False):
    if clean_:
        clean(c)

    c.run("rm -rf dist")
    c.run("python setup.py build --build-lib build/lib")
    c.run("pyinstaller {{ cookiecutter.project_slug }}.spec --clean")


@task(help={"part": "part of the version to be bumped"})
def bumpversion(c, part):
    if part not in ("major", "minor", "patch"):
        raise ValueError('part must be one of "major", "minor", or "patch"!')

    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout):
        raise RuntimeError(
            f"Git working directory is not clean:\n{git_status_result.stdout}"
        )

    c.run("gitchangelog")
    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout) == 0:
        raise RuntimeError(
            "Empty Change! you must have at least one commit type of fix, feat or breaking change"
        )

    full_version = versioneer.get_versions()["version"]
    major, minor, patch = [int(i) for i in full_version.split("+")[0].split(".")]
    if part == "patch":
        patch += 1
    elif part == "minor":
        minor += 1
        patch = 0
    else:
        major += 1
        minor = 0
        patch = 0
    new_version = f"{major}.{minor}.{patch}"
    c.run(f"git tag {new_version}")
    c.run("gitchangelog")
    c.run("git add CHANGELOG.rst")
    c.run(f"git commit -m 'chore: bump version -> {new_version}'")
    c.run(f"git tag -f {new_version}")


@task
def test(c):
    c.run("coverage erase")
    c.run("pytest --cov -sx")
    c.run("coverage html -d build/coverage/")


@task
def init_repo(c):
    git_path = Path(".git")
    if git_path.exists():
        user_input = input(
            ".git repo already exists, do you want to delete it? yes/no : "
        ).lower()
        if user_input in ["y", "yes"]:
            shutil.rmtree(git_path.as_posix())
        else:
            return
    c.run("git init")
    c.run("pre-commit install -t pre-commit")
    c.run("pre-commit install -t pre-push")
    c.run("pre-commit install -t commit-msg")
    c.run("git add .")
    c.run("git commit -m 'chore: First commit'")
    c.run("git tag 0.1.0")


@task
def upload(c, filename, url):
    full_version = versioneer.get_versions()["version"]
    zip_file_name = f"{filename}-{full_version}"
    zip_file_name_with_ext = zip_file_name + ".zip"
    if Path(filename).is_dir():
        shutil.make_archive(zip_file_name, "zip", filename)
    else:
        shutil.move(filename, zip_file_name_with_ext)

    files = {"file": open(zip_file_name_with_ext, "rb")}
    requests.post(url, files=files)
