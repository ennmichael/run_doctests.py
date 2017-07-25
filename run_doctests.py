#!/usr/bin/env python3


from typing import Iterator
import glob
import re
import sys
import os


def file_lines(filename: str) -> Iterator[str]:
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line


def whitespace_collapsed(s: str) -> str:
    """
    >>> whitespace_collapsed('Hello world')
    'Hello world'
    >>> whitespace_collapsed('Hello  world')
    'Hello world'
    >>> whitespace_collapsed('      Hello   world')
    'Hello world'
    >>> whitespace_collapsed('     Hello  world        ')
    'Hello world'
    >>> whitespace_collapsed('  \t   Hello  \t\t\t    world       \t ')
    'Hello world'
    """

    return re.sub(r'\s+', ' ', s).strip()


def string_imports_doctest(s: str) -> bool:
    """
    >>> string_imports_doctest('clearly not')
    False
    >>> string_imports_doctest("'import doctest'")
    False
    >>> string_imports_doctest('"import doctest"')
    False
    >>> string_imports_doctest("'from doctest import whatever'")
    False
    >>> string_imports_doctest('"from doctest import whatever"')
    False
    >>> string_imports_doctest('import doctest')
    True
    >>> string_imports_doctest('from doctest import testmod')
    True
    >>> string_imports_doctest('from doctest import whatever')
    True
    """

    collapsed_line = whitespace_collapsed(s)
    return collapsed_line == 'import doctest' or collapsed_line.startswith('from doctest import')


def file_imports_doctest(filename: str) -> bool:
    for line in file_lines(filename):
        if string_imports_doctest(line):
            return True

    return False


def source_files_using_doctest(directory: str) -> Iterator[str]:
    source_filenames = glob.glob(f'{directory}/*.py')
    return (filename for filename in source_filenames if file_imports_doctest(filename))


def run_source_files_using_doctest(directory: str) -> None:
    for filename in source_files_using_doctest(directory):
        os.system(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    help_text = "run_doctests.py - Run all files that use doctest.\n\n"\
                "Usage:\n" \
                "  run_doctests.py\n" \
                "    Run all files in current directory\n" \
                "  run_doctests.py dir1 dir2 dirN\n" \
                "    Run all files in given directories"

    if len(sys.argv) == 1:
        run_source_files_using_doctest(os.getcwd())
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print(help_text)
    else:
        for dirname in sys.argv[1:]:
            run_source_files_using_doctest(dirname)
