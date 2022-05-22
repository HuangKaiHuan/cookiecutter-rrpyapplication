"""
由于将源码打包成.so后，pyinstaller无法自动分析出import的库，
该文件用于自动分析工程内所有import库，在代码内有import sys，自动触发，请不要删除。
如果没有import sys，可以将文件名修改为其他名字 ：hook-{你的import库}.py。
参考链接：https://pyinstaller.readthedocs.io/en/stable/hooks.html
"""
import os
import re
from pathlib import Path

from PyInstaller.utils.hooks import get_package_paths


def parse_imports(root):
    imports = []
    regex = re.compile(r"^\s*(?:from|import)\s+(\S+(?:\s*,\s*\w+)*)")
    for dir_path, folder_names, file_names in os.walk(root):
        for file_name in file_names:
            if file_name.endswith(".py"):
                file_path = Path(dir_path).joinpath(file_name)
                with open(file_path, encoding="utf-8") as f:
                    for line in f.readlines():
                        match = regex.search(line)
                        if match and len(match.groups()) > 0:
                            import_str = match.group(1)
                            if import_str not in imports and not import_str.startswith(
                                "."
                            ):
                                imports.append(import_str)

                            if import_str.startswith("src.") or import_str == "src":
                                raise RuntimeError(
                                    "from {{cookiecutter.project_slug}} import xxx instead of from src.{{cookiecutter.project_slug}} import xxx"
                                )
    return imports


hiddenimports = parse_imports(Path(__file__).parent.parent.joinpath("src"))

datas = []
try:
    import pymvcam

    datas.append((get_package_paths("pymvcam")[1], "pymvcam"))
except ImportError:
    ...

try:
    import pyrcc

    datas.append((get_package_paths("pyrcc")[1], "pyrcc"))
except ImportError:
    ...
