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
