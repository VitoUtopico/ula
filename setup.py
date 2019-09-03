from cx_Freeze import setup, Executable
        
setup(
    name = "exec_ula",
    version = "1",
    descriptiom = "ula",
    executables = [Executable("C:/Users/Vito/Documents/Python Scripts/workspace_ula/ula/main_ula.py", base = None)])
                            


'''
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("your_program.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any program name>",
    options = options,
    version = "<any program version number>",
    description = '<any program description>',
    executables = executables
)'''