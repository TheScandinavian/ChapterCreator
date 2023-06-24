from Chapter_Creator_Package_Install import function_gui_check
function_gui_check()
import PySimpleGUI as Sg
import subprocess
from Chapter_Creator_New_Directory import function_check_chapter_directory
from Chapter_Creator_RNG import function_chapter_creation_table


def function_open_directory():
    subprocess.Popen(r'explorer /open, "C:\Chapter Creator"')


# Create layout
layout = [[Sg.Text("To generate a Space Marine Chapter, click GENERATE.")],
          [Sg.Button("GENERATE")], [Sg.Button("CANCEL")]]

# Create window
window = Sg.Window("CHAPTER CREATION SCRIPT", layout)

# Create event loop
while True:
    event, values = window.read()
    if event == "GENERATE":
        window.close()
        function_check_chapter_directory()
        function_chapter_creation_table()
        function_open_directory()
        break

    if event == Sg.WIN_CLOSED or "CANCEL":
        window.close()
        break
