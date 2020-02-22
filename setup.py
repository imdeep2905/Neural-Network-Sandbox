import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["h5py"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Neural Network Sandbox",
        version = "1.0.0",
        description = "GUI based application to create and manipulate feed forward neural networks.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])