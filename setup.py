from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {"packages": ["src", "os", "pygame", "pytmx"], "include_files": ["resources"]}
bdist_options = {'add_to_path': False, 'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % ("LTU", "FSM Philip Lindh")}
exe_options = Executable(script="main.py", targetName="S0006D Finite State Machine", base="Win32GUI", icon="resources/icon/Game.ico")

setup(name = "S0006D Finite State Machine",
      version = "1.0",
      description = "Author: Philip Lindh",
      options = {"build_exe": build_options,
                 "bdist_msi": bdist_options},
      executables = [exe_options])