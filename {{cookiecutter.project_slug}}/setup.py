#!/usr/bin/env python

"""The setup script."""

import io
import os
import sys

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

from setuptools import find_packages, setup
from setuptools.extension import Extension

import versioneer

sources = ["src"]
exclude = ["__init__.py", "_version.py"]

extensions = []
py_modules = []
for source in sources:
    for dir_path, folder_names, file_names in os.walk(source):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            rel_path = os.path.relpath(file_path, "src")
            file_name_no_ext = os.path.splitext(rel_path.replace(os.sep, "."))[0]
            if file_name.endswith((".pyx", ".py")):
                if file_name not in exclude:
                    extension = Extension(
                        file_name_no_ext,
                        sources=[file_path],
                        extra_compile_args=["-Os", "-g0"],
                        extra_link_args=["-Wl,--strip-all"],
                    )
                    extensions.append(extension)
                else:
                    py_modules.append(file_name_no_ext)


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fh:
        return fh.read()


readme = read("README.rst")
changelog = read("CHANGELOG.rst")


def setup_package():
    metadata = dict(
        author="{{ cookiecutter.full_name.replace("\"", "\\\"") }}",
        author_email="{{ cookiecutter.email }}",
        python_requires=">=3.6",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        description="{{ cookiecutter.project_short_description }}",
        install_requires=open('requirements.txt').readlines(),
        long_description=readme + "\n\n" + changelog,
        include_package_data=True,
        keywords="{{ cookiecutter.project_slug }}",
        name="{{ cookiecutter.project_slug }}",
        url="{{ cookiecutter.repo_protocol }}://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}",
        version=versioneer.get_version(),
        package_dir={"": "src"},
        zip_safe=False,
    )

    args = sys.argv[1:]
    build_command = ["build", "build_ext", "build_py", "bdist_wheel"]
    run_build = False
    for command in build_command:
        if command in args:
            run_build = True

    if run_build:
        from Cython.Build import build_ext, cythonize
        from Cython.Compiler import Options

        Options.docstrings = False
        compiler_directives = {
            "optimize.unpack_method_calls": False,
            "always_allow_keywords": True,
        }
        metadata["ext_modules"] = cythonize(
            extensions,
            build_dir="build",
            language_level=3,
            compiler_directives=compiler_directives,
        )
        metadata["py_modules"] = py_modules
        metadata["packages"] = []
        cmdclass = versioneer.get_cmdclass({"build_ext": build_ext})
    else:
        cmdclass = versioneer.get_cmdclass()
        metadata["packages"] = find_packages("src")
    metadata["cmdclass"] = cmdclass

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
