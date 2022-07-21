import re


def number_lines(text: str, start_number: int, step: int) -> str:
    if not text:
        return ""
    pattern = r"\bN\d+\b"
    current_number = start_number
    lines = text.splitlines()
    for i, line in enumerate(lines):
        repl = f"N{current_number}"
        lines[i], count = re.subn(pattern, repl, line)
        if count:
            current_number += step
    return "\n".join(lines) + "\n"


def number_lines_wo_comment(
    text: str, start_number: int, step: int, comment_symbol: str
) -> str:
    if not text:
        return ""
    pattern = r"\bN\d+\b"
    current_number = start_number

    lines = text.splitlines()
    for i, line in enumerate(lines):
        splitted_line = line.split(comment_symbol, 1)

        repl = f"N{current_number}"
        splitted_line[0], count = re.subn(pattern, repl, splitted_line[0])

        lines[i] = comment_symbol.join(splitted_line)

        if count:
            current_number += step

    return "\n".join(lines) + "\n"


def number_ids(text: str, start_number: int, step: int) -> str:
    if not text:
        return ""
    pattern = r"\bIDS=\d+\b"
    current_number = start_number
    lines = text.splitlines()
    for i, line in enumerate(lines):
        repl = f"IDS={current_number}"
        lines[i], count = re.subn(pattern, repl, line)
        if count:
            current_number += step
    return "\n".join(lines) + "\n"


def number_ids_wo_comment(
    text: str, start_number: int, step: int, comment_symbol: str
) -> str:
    if not text:
        return ""
    pattern = r"\bIDS=\d+\b"
    current_number = start_number

    lines = text.splitlines()
    for i, line in enumerate(lines):
        splitted_line = line.split(comment_symbol, 1)

        repl = f"IDS={current_number}"
        splitted_line[0], count = re.subn(pattern, repl, splitted_line[0])

        lines[i] = comment_symbol.join(splitted_line)

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
