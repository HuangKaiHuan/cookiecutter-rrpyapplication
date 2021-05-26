"""
由于将源码打包成.so后，pyinstaller无法自动分析出import的库，
该文件用于自动分析工程内所有import库，在代码内有import sys，自动触发，请不要删除。
如果没有import sys，可以将文件名修改为其他名字 ：hook-{你的import库}.py。
参考链接：https://pyinstaller.readthedocs.io/en/stable/hooks.html
"""
import os
import re
from pathlib import Path


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
                            if not match.group(1) in imports and not match.group(
                                1
                            ).startswith("."):
                                imports.append(match.group(1))
    return imports


hiddenimports = parse_imports(Path(__file__).parent.parent.joinpath("src"))
