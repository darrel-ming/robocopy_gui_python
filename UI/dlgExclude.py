from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem)
from PySide2.QtCore import (QRect, QTimer, QItemSelectionModel)
from UI.Ui_DlgExclude import Ui_DlgExclude

from Engine.MirrorTask import MirrorTask

class DlgExclude(QDialog):
    def __init__(self, parent, task):
        super(DlgExclude, self).__init__(parent)
        self.ui = Ui_DlgExclude()
        self.ui.setupUi(self)
        
        self.ExcludedFiles = task.ExcludedFiles.copy()
        self.ExcludedFolders = task.ExcludedFolders.copy()
        self.ExcludedAttributes = task.ExcludedAttributes
        self.ui.excludedFilesControl.addItems(self.ExcludedFiles)
        self.ui.excludedFoldersControl.addItems(self.ExcludedFolders)
        self.ui.chkH.setChecked('H' in self.ExcludedAttributes)
        self.ui.chkS.setChecked('S' in self.ExcludedAttributes)
        self.ui.chkE.setChecked('E' in self.ExcludedAttributes)
        self.baseFolder = task.Source
        
            
        # connect slots
        self.ui.btnOK.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnCancel))
        self.ui.btnBrowseFile.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBrowseFile))
        self.ui.btnBrowseFolder.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBrowseFolder))
        self.ui.btnRemoveFile.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRemoveFile))
        self.ui.btnRemoveFolder.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRemoveFolder))
        self.ui.btnFileWild.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnFileWild))
        self.ui.btnFolderWild.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnFolderWild))
        
    def Apply(self):
        self.ExcludedFiles.clear()
        for i in range(self.ui.excludedFilesControl.count()):
            self.ExcludedFiles.append(self.ui.excludedFilesControl.item(i).text())
        self.ExcludedFolders.clear()
        for i in range(self.ui.excludedFoldersControl.count()):
            self.ExcludedFolders.append(self.ui.excludedFoldersControl.item(i).text())
        str_flag = ''
        if self.ui.chkH.isChecked():
            str_flag += 'H'
        if self.ui.chkS.isChecked():
            str_flag += 'S'
        if self.ui.chkE.isChecked():
            str_flag += 'E'
        self.ExcludedAttributes = str_flag
        
    def Btn_Clicked(self, btn):
        # OK button
        if btn == self.ui.btnOK:
            self.Apply()
            self.accept()
        # Cancel button
        elif btn == self.ui.btnCancel:
            self.reject()
        elif btn == self.ui.btnBrowseFile:
            
            while True:
                file, _ = QFileDialog(self, '', self.baseFolder).getOpenFileName()
                if len(file) == 0:
                    break
                if self.baseFolder in file:
                    sub_dir = file.replace(self.baseFolder, '').replace('/','\\')
                    if len(sub_dir) > 0:
                        self.ui.excludedFilesControl.addItem(sub_dir)
                        break
                QMessageBox.critical(self, 'Invalid file', 'The selected file is not contained in the source folder.')
        elif btn == self.ui.btnFileWild:
            self.ui.excludedFilesControl.addItem(self.ui.txtFile.text())
        elif btn == self.ui.btnFolderWild:
            self.ui.excludedFoldersControl.addItem(self.ui.txtFolder.text())
        elif btn == self.ui.btnBrowseFolder:
            while True:
                path = QFileDialog(self,"", self.baseFolder).getExistingDirectory()
                if len(path) == 0:
                    break
                if self.baseFolder in path:
                    sub_dir = path.replace(self.baseFolder, '')
                    if len(sub_dir) > 0:
                        self.ui.excludedFoldersControl.addItem(sub_dir)
                        break
                QMessageBox.critical(self, 'Invalid subfolder', 'The selected folder is not contained in the source folder.')
            
        elif btn == self.ui.btnRemoveFile:
            index = self.ui.excludedFilesControl.currentIndex().row()
            if index >= 0:
                self.ui.excludedFilesControl.takeItem(index)
        elif btn == self.ui.btnRemoveFolder:
            index = self.ui.excludedFoldersControl.currentIndex().row()
            if index >= 0:
                self.ui.excludedFoldersControl.takeItem(index)
            