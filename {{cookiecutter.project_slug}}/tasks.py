import os
import shutil
import stat
import glob
from pathlib import Path

import requests
from gitchangelog import gitchangelog
from invoke import UnexpectedExit, task

import versioneer


def readonly_handler(func, path, execinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

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
        files = glob.glob(pattern, recursive=True)
        for file in files:
            shutil.rmtree(file, onerror=readonly_handler)


@task
def freeze(c, clean_=False):
    if clean_:
        clean(c)
    elif os.path.exists("dist"):
        shutil.rmtree("dist", onerror=readonly_handler)
    c.run("python setup.py build --build-lib build/lib")
    c.run("pyinstaller {{ cookiecutter.project_slug }}.spec --clean")


@task
def freeze_req(c):
    c.run("pip freeze > requirements.txt")
    requirement_lines = [
        i for i in open("requirements.txt").readlines() if not i.startswith("-e ") and not i.startswith("#")
    ]
    with open("requirements.txt", "w") as f:
        f.writelines(requirement_lines)


def _analysis_bump_part(c, tag):
    git_log_result = c.run(f"git log --pretty=format:%s --no-merges {tag}..HEAD")

    config = gitchangelog.load_config_file(
        ".gitchangelog.rc", fail_if_not_present=False
    )
    config = gitchangelog.Config(config)
    section_regexps = config["section_regexps"]

    part_dict = {"Bug Fixes": "patch", "Features": "minor", "BREAKING CHANGE": "major"}

    part_level_dict = {
        "auto": 0,
        "patch": 1,
        "minor": 2,
        "major": 3,
    }
    part = "auto"
    for commit in git_log_result.stdout.splitlines():
        part_key = gitchangelog.first_matching(section_regexps, commit)
        if part_key:
            part_type = part_dict[part_key]
            if part_level_dict[part_type] > part_level_dict[part]:
                part = part_type
    return part


@task(help={"part": "part of the version to be bumped"})
def bumpversion(c, part):
    if part not in ("auto", "major", "minor", "patch"):
        raise ValueError('part must be one of "auto", "major", "minor", or "patch"!')

    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout):
        raise RuntimeError(
            f"Git working directory is not clean:\n{git_status_result.stdout}"
        )

    full_version = versioneer.get_versions()["version"]
    major, minor, patch = [int(i) for i in full_version.split("+")[0].split(".")]
    now_version = f"{major}.{minor}.{patch}"

    if part == "auto":
        part = _analysis_bump_part(c, now_version)

    if part == "patch":
        patch += 1
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        raise RuntimeError(
            "Empty Change! you must have at least one commit type of fix, feat or breaking change"
        )

    new_version = f"{major}.{minor}.{patch}"
    c.run(f"git tag {new_version}")
    c.run("gitchangelog")
    git_status_result = c.run("git status --porcelain")
    if len(git_status_result.stdout) == 0:
        c.run(f"git tag -d {new_version}")
        raise RuntimeError(
            "Empty Change! you must have at least one commit type of fix, feat or breaking change"
        )
    c.run("git add CHANGELOG.rst")
    c.run(f'git commit -m "chore: bump version -> {new_version}"')
    c.run(f"git tag -f {new_version}")


@task
def init_repo(c):
    git_path = Path(".git")
    if git_path.exists():
        user_input = input(
            ".git repo already exists, do you want to delete it? yes/no : "
        ).lower()
        if user_input in ["y", "yes"]:
            shutil.rmtree(git_path.as_posix(), onerror=readonly_handler)
        else:
            return
    c.run("git init")
    c.run("pre-commit install -t pre-commit")
    c.run("pre-commit install -t pre-push")
    c.run("pre-commit install -t commit-msg")
    c.run("git add .")
    try:
        c.run('git commit -m "chore: First commit"')
    except UnexpectedExit:
        c.run("git add .")
        c.run('git commit -m "chore: First commit"')
    finally:
        c.run("git tag {{ cookiecutter.version }}")


@task
def upload(c, filename, url):
    full_version = versioneer.get_versions()["version"]
    zip_file_name = f"{Path(filename)}-{full_version}"
    zip_file_name_with_ext = zip_file_name + ".zip"
    if Path(filename).is_dir():
        shutil.make_archive(zip_file_name, "zip", filename)
        files = {"file": open(zip_file_name_with_ext, "rb")}
    else:
        shutil.move(filename, zip_file_name)
        files = {"file": open(zip_file_name, "rb")}

    requests.post(url, files=files)
