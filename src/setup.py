import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "S0006D Laboration 1",
        version = "1.1",
        author="Philip Lindh",
        description = "S0006D Assignment 1 - Philip Lindh",
        options = {"build_exe": build_exe_options},
        executables = [Executable(script="Main.py", targetName="S0006D Laboration 1.exe", base=base)])