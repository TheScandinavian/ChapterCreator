import importlib.util
import subprocess
import sys


def function_install_simple_gui():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySimpleGUI"])


# Check if PySimpleGUI is installed
def function_gui_check():
    package_name = "PySimpleGUI"

    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(package_name + " will be installed.")
        function_install_simple_gui()
    else:
        print(package_name + " is installed.")


if __name__ == "__Chapter_Creator_Main__":
    function_gui_check()
