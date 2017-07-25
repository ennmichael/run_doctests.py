# run_doctests.py

Run all files that use doctest.

## Usage

```
run_doctests.py                 # Run all files in current directory
run_doctests.py dir1 dir2 dirN  # Run all files in given directories
run_doctests.py --help          # Show a small help dialog, similar to this text
```

All files that `run_doctests.py` finds should have the hashbang at the beginning. Other than that, the script can run both Python 3 and Python 2 files.
`run_doctests.py` itself is written in Python 3.
