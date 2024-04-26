import json
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

import Panel.BlenderLauncher
import Operator.Path as Path
import Operator.File as File

class blenderLauncherWindow(QMainWindow,Panel.BlenderLauncher.Ui_BlenderLauncherWindow):
    def __init__(self):
        super(blenderLauncherWindow,self).__init__()
        self.setupUi(self)

        self.BlenderVersions = []
        self.WorkSpaces = []
        self.FilesInWorkSpace = []
        self.LoadConfig()

        self.FilesInWorkSpaceModel = QStandardItemModel()
        self.setupCustom()

        self.setupConnect()

    def LoadConfig(self):
        #get Blender Versions
        for dir in os.listdir(Path.BlenderFoundation()):
            if(dir.startswith('Blender ')):
                self.BlenderVersions.append(dir.replace('Blender ',''))
        #get WorkSpaces
        for workspace in Path.WorkSpaces():
            self.WorkSpaces.append(workspace)

    def setupCustom(self):
        self.comboBox_Version.addItems(self.BlenderVersions)
        self.comboBox_WorkSpace.addItems(self.WorkSpaces)
        self.listView_WorkSpaceFiles.setModel(self.FilesInWorkSpaceModel)
        self.Func_UpdateFilesInWorkSpace()


    def setupConnect(self):
        self.pushButton_Launch.clicked.connect(self.Action_pushButton_Launch_clicked)
        self.pushButton_BrowseWorkSpace.clicked.connect(self.Action_pushButton_BrowseWorkSpace_clicked)
        self.pushButton_Open.clicked.connect(self.Action_pushButton_Open_clicked)
        self.comboBox_WorkSpace.currentIndexChanged.connect(self.Action_comboBox_WorkSpace_currentIndexChanged)

    def Action_pushButton_Launch_clicked(self):
        version_string = 'Blender ' + self.comboBox_Version.currentText()
        cmdline = 'cd ' + Path.BlenderFoundation() + '\\' + version_string + ' && blender'
        os.system(cmdline)
        print('[CMD]: ' + cmdline)

    def Action_pushButton_BrowseWorkSpace_clicked(self):
        new_workspace = QFileDialog.getExistingDirectory()
        if(new_workspace!=""):
            self.WorkSpaces.append(new_workspace)
            self.comboBox_WorkSpace.addItem(new_workspace)
            self.comboBox_WorkSpace.setCurrentIndex(self.comboBox_WorkSpace.count()-1)
            Path.AddWorkSpace(new_workspace)
            self.Func_UpdateFilesInWorkSpace()

    def Action_pushButton_Open_clicked(self):
        version_string = 'Blender ' + self.comboBox_Version.currentText()
        open_path = self.listView_WorkSpaceFiles.selectionModel().selectedIndexes()[0].data()
        open_path = self.comboBox_WorkSpace.currentText() + "\\" + open_path
        cmdline = 'cd ' + Path.BlenderFoundation() + '\\' + version_string + ' && blender ' + open_path
        os.system(cmdline)
        print('[CMD]: ' + cmdline)

    def Action_comboBox_WorkSpace_currentIndexChanged(self):
        self.Func_UpdateFilesInWorkSpace()

    def Func_UpdateFilesInWorkSpace(self):
        workspace_path = self.comboBox_WorkSpace.currentText()
        files = File.get_filtered_files(workspace_path)
        self.FilesInWorkSpaceModel.clear()
        for file in files:
            self.FilesInWorkSpaceModel.appendRow(QStandardItem(file))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = blenderLauncherWindow()
    window.show()
    sys.exit(app.exec())