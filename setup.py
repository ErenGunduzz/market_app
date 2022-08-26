from cx_Freeze import setup, Executable

setup(name = "market_app",
      version="0.1",
      description= "",
      executables = [Executable("main.py")])
