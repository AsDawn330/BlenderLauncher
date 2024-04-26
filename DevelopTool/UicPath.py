import sys
import os

path = 'D:\Project\BlenderLauncher\\UI\Panel'
uic = 'D:\Project\BlenderLauncher\\venv\Scripts\pyuic5.exe'
if(os.path.exists(path)):
    for file in os.listdir(path):
        if(file.endswith('.ui')):
            file = path + '\\' + file
            cmdline = uic + ' ' + file + ' -o ' + file.replace('.ui','.py')
            os.system(cmdline)
            print(cmdline)