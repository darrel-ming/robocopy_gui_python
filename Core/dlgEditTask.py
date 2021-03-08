import os
import copy
from PySide2.QtWidgets import (
    QDialog, QMessageBox, QFileDialog, QCheckBox)
from PySide2.QtGui import (QIntValidator)
from UI.Ui_DlgEdit import Ui_EditTask
from Core.dlgExclude import DlgExclude
from Engine.Settings import Settings
from pathlib import Path


class DlgEditTask(QDialog):
    '''
    UI Class for 'Edit Task' Dialog
    Attributes:
    -----------
    ui : Ui_EditTask
        compiled by QtDesinger
    _task : MirrorTask
        temporary task for editing
    chks : list
        list of check boxes for custom switch options

    Methods:
    ----------
    GetOptions():
        get/sets custom switch check boxes
    UpdateCmd():
        makes the list of arguments from options
    Apply():
        apply the UI components to see it is valid or not
    UpdateCmd():
        builds the command argument from options
    GetFlagText(key):
        gets option name and value
    GetOptions(update):
        get/set UI values from/to task attributes

    Slots:
    ----------
    clicked():
        slot function for checkbox
    Btn_Clicked():
        slot function for UI components
    '''

    def __init__(self, parent, task):
        '''
        Paramters:
        -------------
        parent : FormMainWindow
        task : MirrorTask
            task to be edited
        '''
        super(DlgEditTask, self).__init__(parent)
        # copy the input task
        self._task = copy.deepcopy(task)
        # initialize UI
        self.ui = Ui_EditTask()
        self.ui.setupUi(self)

        # build the list of combo boxes
        self.chks = [
            self.ui.chk_s, self.ui.chk_v, self.ui.chk_m, self.ui.chk_xo,
            self.ui.chk_tbd, self.ui.chk_sec, self.ui.chk_mov, self.ui.chk_a,
            self.ui.chk_b, self.ui.chk_z, self.ui.chk_copyall,
            self.ui.chk_nocopy, self.ui.chk_mir, self.ui.chk_zb,
            self.ui.chk_np, self.ui.chk_create, self.ui.chk_purge,
            self.ui.chk_move, self.ui.chk_fat, self.ui.chk_copy,
            self.ui.chk_lev, self.ui.chk_r, self.ui.chk_w, self.ui.chk_e,
            self.ui.chk_fft, self.ui.chk_j, self.ui.chk_max, self.ui.chk_min,
            self.ui.chk_maxage, self.ui.chk_minage, self.ui.chk_maxlad,
            self.ui.chk_minlad
            ]
        # connect each checkbox to slots
        for chk in self.chks:
            chk.clicked.connect(self.clicked)
        # set the Source/Target input value
        self.ui.sourceFolderTextBox.setText(self._task.Source)
        self.ui.targetFolderTextBox.setText(self._task.Target)

        # if UserCustomOption is enabled
        if self._task.UseCustomOptions:
            self.ui.robocopySwitchesCheckBox.setChecked(True)
        self.ui.grpOptions.setEnabled(self._task.UseCustomOptions)
        # set the check boxes from task switch option
        self.GetOptions(False)

        # connect slots
        self.ui.btnBrowseSrc.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnBrowseSrc))
        self.ui.btnBrowseDst.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnBrowseDst))
        self.ui.btnExclude.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnExclude))
        self.ui.btnOK.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnCancel))
        self.ui.robocopySwitchesCheckBox.toggled.connect(
            lambda: self.Btn_Clicked(self.ui.robocopySwitchesCheckBox))
        self.ui.sourceFolderTextBox.textChanged.connect(
            lambda: self.Btn_Clicked(self.ui.sourceFolderTextBox))

        # txt boxes for custom check box
        self.ui.txt_lev.setValidator(QIntValidator(0, 100, self))
        self.ui.txt_lev.textChanged.connect(self.UpdateCmd)
        self.ui.txt_r.textChanged.connect(self.UpdateCmd)
        self.ui.txt_w.textChanged.connect(self.UpdateCmd)
        self.ui.txt_max.textChanged.connect(self.UpdateCmd)
        self.ui.txt_min.textChanged.connect(self.UpdateCmd)
        self.ui.txt_maxage.textChanged.connect(self.UpdateCmd)
        self.ui.txt_minage.textChanged.connect(self.UpdateCmd)
        self.ui.txt_maxlad.textChanged.connect(self.UpdateCmd)
        self.ui.txt_minlad.textChanged.connect(self.UpdateCmd)

    def clicked(self):
        '''
        slot fubction for UI components
        '''
        try:
            # get the signal sender
            button = self.sender()
            # if sender is not check box, return
            if not isinstance(button, QCheckBox):
                return
            # get the label of check box
            txt = button.text().lower()
            # get the state of the check box
            if txt == '/lev:':
                self.ui.txt_lev.setEnabled(button.isChecked())
            elif txt == '/r:':
                self.ui.txt_r.setEnabled(button.isChecked())
            elif txt == '/w:':
                self.ui.txt_w.setEnabled(button.isChecked())
            elif txt == '/max:':
                self.ui.txt_max.setEnabled(button.isChecked())
            elif txt == '/min:':
                self.ui.txt_min.setEnabled(button.isChecked())
            elif txt == '/maxage:':
                self.ui.txt_maxage.setEnabled(button.isChecked())
            elif txt == '/minage:':
                self.ui.txt_minage.setEnabled(button.isChecked())
            elif txt == '/maxlad:':
                self.ui.txt_maxlad.setEnabled(button.isChecked())
            elif txt == '/minlad:':
                self.ui.txt_minlad.setEnabled(button.isChecked())
            # updates the cmd from switches
            self.UpdateCmd()
        except Exception as e:
            print(f'Clicked err:{e}')

    def Apply(self):
        '''
        apply the UI components to see it is valid or not
        '''
        try:
            # get Source path
            srcTxt = self.ui.sourceFolderTextBox.text()
            # if not exist
            if not os.path.exists(srcTxt):
                QMessageBox.critical(
                    self,
                    Settings.EDIT_DLG_Invalid_Src_Caption,
                    Settings.EDIT_DLG_Invalid_Src_TEXT)
                self.ui.sourceFolderTextBox.setFocus()
                return False
            # get Target path
            dstTxt = self.ui.targetFolderTextBox.text()
            # if not exist
            if not os.path.exists(dstTxt):
                QMessageBox.critical(
                    self,
                    Settings.EDIT_DLG_Invalid_Tar_Caption,
                    Settings.EDIT_DLG_Invalid_Tar_TEXT)
                self.ui.targetFolderTextBox.setFocus()
                return False
            # Check if Target is child of Source
            if Path(srcTxt) in Path(dstTxt).parents:
                QMessageBox.critical(
                    self,
                    Settings.EDIT_DLG_Invalid_Tar_Caption,
                    Settings.EDIT_DLG_Invalid_Tar_TEXT2)
                self.ui.targetFolderTextBox.setFocus()
                return False
            # updates the Source and Target of the task
            self._task.Source = srcTxt
            self._task.Target = dstTxt
            # Update Custom Options
            self._task.UseCustomOptions = self.ui.robocopySwitchesCheckBox.isChecked()  # noqa
            self._task.CustomRobocopySwitches = ' '.join(self.GetOptions(True))
        except Exception as e:
            print(f'EditTaskDlg/Apply err:{e}')
        return True

    def Btn_Clicked(self, btn):
        '''
        slot function for UI components
        '''
        try:
            # custom switch check box
            if btn == self.ui.robocopySwitchesCheckBox:
                # get the default switches
                tmp = Settings.RobocopySwitches.split(' ')
                default_params = []
                for t in tmp:
                    a, _ = self.GetFlagText(t)
                    default_params.append(a)
                # enable/disable custom swtich group
                self.ui.grpOptions.setEnabled(btn.isChecked())
                if btn.isChecked():
                    # if enabled, apply txt box too
                    self.ui.txt_lev.setEnabled(self.ui.chk_lev.isChecked())
                    self.ui.txt_r.setEnabled(self.ui.chk_r.isChecked())
                    self.ui.txt_w.setEnabled(self.ui.chk_w.isChecked())
                    self.ui.txt_max.setEnabled(self.ui.chk_max.isChecked())
                    self.ui.txt_min.setEnabled(self.ui.chk_min.isChecked())
                    self.ui.txt_maxage.setEnabled(self.ui.chk_maxage.isChecked())   # noqa
                    self.ui.txt_minage.setEnabled(self.ui.chk_minage.isChecked())   # noqa
                    self.ui.txt_maxlad.setEnabled(self.ui.chk_maxlad.isChecked())   # noqa
                    self.ui.txt_minlad.setEnabled(self.ui.chk_minlad.isChecked())   # noqa
                else:
                    # if not, uncheck checkboxes
                    for sh in self.chks:
                        if sh.text().lower() in default_params:
                            sh.setChecked(True)
                        else:
                            sh.setChecked(False)
            # Source Folder cbhange
            elif btn == self.ui.sourceFolderTextBox:
                self.ui.btnExclude.setEnabled(os.path.exists(
                    self.ui.sourceFolderTextBox.text()))
            # OK button
            elif btn == self.ui.btnOK:
                # if can not apply, return
                if not self.Apply():
                    return
                self.accept()
            # Cancel Button
            elif btn == self.ui.btnCancel:
                self.reject()
            # Source Browser button
            elif btn == self.ui.btnBrowseSrc:
                # opens the file browser dialog
                path = QFileDialog(self).getExistingDirectory()
                path = path.replace('/', '\\')
                if len(path) > 0:
                    self.ui.sourceFolderTextBox.setText(path)
                    self._task.Source = path
            # Target Browser button
            elif btn == self.ui.btnBrowseDst:
                # opens the file browser dialog
                path = QFileDialog(self).getExistingDirectory()
                path = path.replace('/', '\\')
                if len(path) > 0:
                    self.ui.targetFolderTextBox.setText(path)
                    self._task.Target = path
            # Exclude Button
            elif btn == self.ui.btnExclude:
                # opens the Exclude Dialog
                dlg = DlgExclude(self, self._task)
                if dlg.exec_() != QDialog.Accepted:
                    return
                # update Exclude params
                self._task.ExcludedAttributes = dlg.ExcludedAttributes
                self._task.ExcludedFiles = dlg.ExcludedFiles
                self._task.ExcludedFolders = dlg.ExcludedFolders
            # update command arguments
            self.UpdateCmd()
        except Exception as e:
            print(f'Btn_Clicked err:{e}')

    def UpdateCmd(self):
        '''
        builds the command argument from options
        '''
        try:
            params = []
            # add robocopy exe
            params.append(Settings.RoboCopy_Exe)
            # get src from UI
            srcTxt = self.ui.sourceFolderTextBox.text()
            # get dst from UI
            dstTxt = self.ui.targetFolderTextBox.text()
            # add src
            params.append(f'\"{srcTxt}\"')
            # add dst
            params.append(f'\"{dstTxt}\"')
            # add Exclude options
            for p in self._task.GetExcludeOptions(True).split(';'):
                params.append(p)
            # add rest options
            for p in self.GetOptions(True):
                params.append(p)
            # make the list as a sting
            strCmd = ' '.join(params)
            # set the string to UI
            self.ui.txtCmd.setText(strCmd)
            self.ui.txtCmd.setEnabled(self.ui.robocopySwitchesCheckBox.isChecked()) # noqa
        except Exception as e:
            print(f'UpdateCmd err:{e}')

    def GetFlagText(self, key):
        '''
        parse the swtich option
        Parameters:
        ---------
            lev:30
        Returns:
        ---------
            lev, 30
        '''
        tmp = key.split(':')
        val = tmp[1] if len(tmp) > 1 else ''
        switch = tmp[0] if len(tmp) == 1 else tmp[0] + ':'
        return switch, val

    def GetOptions(self, update=False):
        '''
        get/set UI values from/to task attributes
        Parameters:
        -----------
        update: Bool
            False: Task to UI,
            True : UI to Task
        Return Values:
            if update is True, returns the list params
        '''
        try:
            # init params from default switch
            params = self._task.CustomRobocopySwitches.split(' ')
            for p in Settings.RobocopySwitches.split(' '):
                if p not in params:
                    params.append(p)
            # check boxes that checked
            ctrls = {}
            for ch in self.chks:
                ctrls[ch.text().lower()] = ch
            # sets check box from task value
            if not update:
                # uncheck all check boxes
                for ch in self.chks:
                    ch.setChecked(False)
                # disable all txt boxes
                self.ui.txt_lev.setEnabled(False)
                self.ui.txt_r.setEnabled(False)
                self.ui.txt_w.setEnabled(False)
                self.ui.txt_max.setEnabled(False)
                self.ui.txt_min.setEnabled(False)
                self.ui.txt_maxage.setEnabled(False)
                self.ui.txt_minage.setEnabled(False)
                self.ui.txt_maxlad.setEnabled(False)
                self.ui.txt_minlad.setEnabled(False)
                # iterate params
                for key in params:
                    if len(key) == 0:
                        continue
                    # parse switch
                    a, val = self.GetFlagText(key)
                    if a not in ctrls:
                        continue
                    # enables check box
                    ctrls[a].setChecked(True)
                    # enables txt box and set value
                    if a == '/lev:':
                        self.ui.txt_lev.setEnabled(True)
                        self.ui.txt_lev.setText(val)
                    elif a == '/r:':
                        self.ui.txt_r.setEnabled(True)
                        self.ui.txt_r.setText(val)
                    elif a == '/w:':
                        self.ui.txt_w.setEnabled(True)
                        self.ui.txt_w.setText(val)
                    elif a == '/max:':
                        self.ui.txt_max.setEnabled(True)
                        self.ui.txt_max.setText(val)
                    elif a == '/min:':
                        self.ui.txt_min.setEnabled(True)
                        self.ui.txt_min.setText(val)
                    elif a == '/maxage:':
                        self.ui.txt_maxage.setEnabled(True)
                        self.ui.txt_maxage.setText(val)
                    elif a == '/minage:':
                        self.ui.txt_minage.setEnabled(True)
                        self.ui.txt_minage.setText(val)
                    elif a == '/maxlad:':
                        self.ui.txt_maxlad.setEnabled(True)
                        self.ui.txt_maxlad.setText(val)
                    elif a == '/minlad:':
                        self.ui.txt_minlad.setEnabled(True)
                        self.ui.txt_minlad.setText(val)
                # updates cmd args
                self.UpdateCmd()
            else:
                # saves UI swtiches to task
                # clear param
                params.clear()
                # iterate all check boxes
                for ch in ctrls:
                    # if not unchecked, skip
                    if not ctrls[ch].isChecked():
                        continue
                    _str = ch
                    # if switch requires txt values
                    if ch == '/lev:':
                        _str += self.ui.txt_lev.text()
                    if ch == '/r:':
                        _str += self.ui.txt_r.text()
                    if ch == '/w:':
                        _str += self.ui.txt_w.text()
                    if ch == '/max:':
                        _str += self.ui.txt_max.text()
                    if ch == '/min:':
                        _str += self.ui.txt_min.text()
                    if ch == '/maxage:':
                        _str += self.ui.txt_maxage.text()
                    if ch == '/minage:':
                        _str += self.ui.txt_minage.text()
                    if ch == '/maxlad:':
                        _str += self.ui.txt_maxlad.text()
                    if ch == '/minlad:':
                        _str += self.ui.txt_minlad.text()
                    # add new switch
                    params.append(_str)
                return params
        except Exception as e:
            print(f'GetOptions err:{e}')
