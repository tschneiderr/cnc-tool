import os
import re


def find_files(path: str, extensions: list[str] = []) -> list[str]:
    """Find files in path, non-recursively"""
    files = []
    with os.scandir(path) as i:
        for entry in i:
            if entry.is_file():
                file_path = os.path.normpath(entry.path)
                if extensions:
                    file_ext = os.path.splitext(file_path)[1].lower()
                    if file_ext in extensions:
                        files.append(file_path)
                else:
                    files.append(file_path)
    return files


def number_lines(text: str, start_number: int, step: int) -> str:
    """Number CNC lines increasingly"""
    if not text:
        return ""
    pattern = r"^N\d+"
    current_number = start_number
    lines = text.splitlines()
    for i, line in enumerate(lines):
        repl = f"N{current_number}"
        lines[i], count = re.subn(pattern, repl, line)
        if count:
            current_number += step
    return "\n".join(lines) + "\n"


def number_ids(text: str, start_number: int, step: int, line_comment_char: str) -> str:
    """Number IDS increasingly, ignore commented lines"""
    if not text:
        return ""
    pattern = r"IDS=\d+"
    current_number = start_number
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.startswith(line_comment_char):
            repl = f"IDS={current_number}"
            lines[i], count = re.subn(pattern, repl, line)
            if count:
                current_number += step
    return "\n".join(lines) + "\n"


def convert_tabs_to_spaces(text: str, tab_width: int) -> str:
    if not text:
        return ""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace("\t", " " * tab_width)
    return "\n".join(lines) + "\n"


def remove_trailing_whitespace(text: str) -> str:
    if not text:
        return ""
    lines = text.rstrip().splitlines()
    for i, line in enumerate(lines):
        lines[i] = line.rstrip()
    return "\n".join(lines) + "\n"
