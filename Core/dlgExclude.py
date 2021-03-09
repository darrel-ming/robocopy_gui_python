from PySide2.QtWidgets import (QDialog, QMessageBox, QFileDialog)
from UI.Ui_DlgExclude import Ui_DlgExclude
from Engine.Settings import Settings


class DlgExclude(QDialog):
    '''
    class for DlgExclude Dialog box
    Attributes:
    ----------
    ui : Ui_DlgExclude
        UI wrapper instance
    baseFolder : Source folder

    Methods:
    ----------
    Apply():
        sets the UI values to task attributes

    Slots:
    Btn_Clicked()
        slot funtion for UI components
    '''

    def __init__(self, parent, task):
        '''
        Parameters:
        -----------
        parent : FrmMainWindow
            MainWindow to send singals
        task : MirrorTask
            task to be edited
        '''
        super(DlgExclude, self).__init__(parent)
        # intialize UI
        self.ui = Ui_DlgExclude()
        self.ui.setupUi(self)

        # get task attributes
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
        self.ui.btnOK.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnCancel))
        self.ui.btnBrowseFile.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnBrowseFile))
        self.ui.btnBrowseFolder.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnBrowseFolder))
        self.ui.btnRemoveFile.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnRemoveFile))
        self.ui.btnRemoveFolder.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnRemoveFolder))
        self.ui.btnFileWild.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnFileWild))
        self.ui.btnFolderWild.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnFolderWild))

    def Apply(self):
        '''
        sets the UI values to task attributes
        '''
        try:
            # make ExcludeFile list
            self.ExcludedFiles.clear()
            for i in range(self.ui.excludedFilesControl.count()):
                self.ExcludedFiles.append(
                    self.ui.excludedFilesControl.item(i).text())
            # make ExcludeFolder list
            self.ExcludedFolders.clear()
            for i in range(self.ui.excludedFoldersControl.count()):
                self.ExcludedFolders.append(
                    self.ui.excludedFoldersControl.item(i).text())
            # set the HSE flag
            str_flag = ''
            if self.ui.chkH.isChecked():
                str_flag += 'H'
            if self.ui.chkS.isChecked():
                str_flag += 'S'
            if self.ui.chkE.isChecked():
                str_flag += 'E'
            # set the exclude attributes
            self.ExcludedAttributes = str_flag
        except Exception as e:
            print(f'DlgExclude Apply Err:{e}')

    def Btn_Clicked(self, btn):
        '''
        slot funtion for UI components
        params:
        --------
        btn : QPushButton
            The button that sends signal
        '''
        try:
            # OK button
            if btn == self.ui.btnOK:
                self.Apply()
                self.accept()
            # Cancel button
            elif btn == self.ui.btnCancel:
                self.reject()
            # Brose File
            elif btn == self.ui.btnBrowseFile:
                # repeats until valid file is selcted
                while True:
                    file, _ = QFileDialog(
                        self,
                        '',
                        self.baseFolder).getOpenFileName()
                    if len(file) == 0:
                        break
                    if self.baseFolder in file:
                        sub_dir = file.replace(
                            self.baseFolder,
                            '').replace('/', '\\')
                        if len(sub_dir) > 0:
                            self.ui.excludedFilesControl.addItem(sub_dir)
                            break
                    QMessageBox.critical(
                        self,
                        Settings.EXCLUDE_DLG_INVALID_File_Caption,
                        Settings.EXCLUDE_DLG_INVALID_File_TEXT)
            elif btn == self.ui.btnFileWild:
                # removes the space
                txt = self.ui.txtFile.text().strip()
                if len(txt) == 0:
                    QMessageBox.information(
                        self,
                        Settings.EXCLUDE_DLG_INVALID_Wild_Caption,
                        Settings.EXCLUDE_DLG_INVALID_Wild_TEXT)
                    return
                self.ui.excludedFilesControl.addItem(txt)
            elif btn == self.ui.btnFolderWild:
                # removes the space
                txt = self.ui.txtFolder.text().strip()
                if len(txt) == 0:
                    QMessageBox.information(
                        self,
                        Settings.EXCLUDE_DLG_INVALID_Wild_Caption,
                        Settings.EXCLUDE_DLG_INVALID_Wild_TEXT)
                    return
                self.ui.excludedFoldersControl.addItem(txt)
            elif btn == self.ui.btnBrowseFolder:
                # repeats until valid file is selcted
                while True:
                    path = QFileDialog(self, "", self.baseFolder).getExistingDirectory()    # noqa
                    path = path.replace('/', '\\')
                    if len(path) == 0:
                        break
                    if self.baseFolder in path:
                        sub_dir = path.replace(self.baseFolder, '').replace('/', '\\')      # noqa
                        if len(sub_dir) > 0:
                            self.ui.excludedFoldersControl.addItem(sub_dir)
                            break
                    QMessageBox.critical(
                        self,
                        Settings.EXCLUDE_DLG_INVALID_SubDir_Caption,
                        Settings.EXCLUDE_DLG_INVALID_SubDir_TEXT)
            elif btn == self.ui.btnRemoveFile:
                index = self.ui.excludedFilesControl.currentIndex().row()
                # if selected index is valid
                if index >= 0:
                    self.ui.excludedFilesControl.takeItem(index)
            elif btn == self.ui.btnRemoveFolder:
                # if selected index is valid
                index = self.ui.excludedFoldersControl.currentIndex().row()
                if index >= 0:
                    self.ui.excludedFoldersControl.takeItem(index)
        except Exception as e:
            print(f'DlgExclude click err:{e}')
