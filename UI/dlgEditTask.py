import os, copy
from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog, QCheckBox)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem, QIntValidator)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel, )
from UI.Ui_DlgEdit import Ui_EditTask
from UI.dlgExclude import DlgExclude

from Engine.MirrorTask import MirrorTask
from Engine.Settings import Settings

class DlgEditTask(QDialog):
    def __init__(self, parent, task):
        super(DlgEditTask, self).__init__(parent)
        self._task = copy.deepcopy(task)
        self.ui = Ui_EditTask()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.Tool)
        self.chks = [self.ui.chk_s, self.ui.chk_v, self.ui.chk_m, self.ui.chk_xo, self.ui.chk_tbd,
                    self.ui.chk_sec, self.ui.chk_mov, self.ui.chk_a, self.ui.chk_b, self.ui.chk_z,
                    self.ui.chk_copyall, self.ui.chk_nocopy, self.ui.chk_mir, self.ui.chk_zb, self.ui.chk_np,
                    self.ui.chk_create, self.ui.chk_purge, self.ui.chk_move, self.ui.chk_fat, self.ui.chk_copy, 
                    self.ui.chk_lev, self.ui.chk_r, self.ui.chk_w, self.ui.chk_e, self.ui.chk_fft,
                    ]
        for chk in self.chks:
            chk.clicked.connect(self.clicked)
        
        self.ui.sourceFolderTextBox.setText(self._task.Source)
        self.ui.targetFolderTextBox.setText(self._task.Target)
        
        if self._task.UseCustomOptions:
            self.ui.robocopySwitchesCheckBox.setChecked(True)
        self.ui.grpOptions.setEnabled(self._task.UseCustomOptions)
        self.GetOptions(False)
        
            
        # connect slots
        self.ui.btnBrowseSrc.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBrowseSrc))
        self.ui.btnBrowseDst.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBrowseDst))
        self.ui.btnExclude.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnExclude))
        self.ui.btnOK.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnCancel))
        self.ui.robocopySwitchesCheckBox.toggled.connect(lambda: self.Btn_Clicked(self.ui.robocopySwitchesCheckBox))
        self.ui.sourceFolderTextBox.textChanged.connect(lambda: self.Btn_Clicked(self.ui.sourceFolderTextBox))
        
        self.ui.txt_lev.setValidator(QIntValidator(0, 100, self))
        self.ui.txt_lev.textChanged.connect(self.UpdateCmd)
        self.ui.txt_r.textChanged.connect(self.UpdateCmd)
        self.ui.txt_w.textChanged.connect(self.UpdateCmd)
        
        self.HasChanged = False
    
    def clicked(self):
        button = self.sender()
        if not isinstance(button, QCheckBox):
            return
        txt = button.text().lower()
        if txt == '/lev:':
            self.ui.txt_lev.setEnabled(button.isChecked())
        elif txt == '/r:':
            self.ui.txt_r.setEnabled(button.isChecked())
        elif txt == '/w:':
            self.ui.txt_w.setEnabled(button.isChecked())
        
        self.UpdateCmd()
                
    def Apply(self):
        srcTxt = self.ui.sourceFolderTextBox.text()
        if not os.path.exists(srcTxt):
            QMessageBox.critical(self, "Invalid source folder", "The source folder does not exist.")
            self.ui.sourceFolderTextBox.setFocus()
            return False
        dstTxt = self.ui.targetFolderTextBox.text()
        if not os.path.exists(dstTxt):
            QMessageBox.critical(self, "Invalid target folder", "The target folder does not exist.")
            self.ui.targetFolderTextBox.setFocus()
            return False
        if srcTxt in dstTxt:
            QMessageBox.critical(self, "Invalid target folder", "The target folder must not be in the source folder.")
            self.ui.targetFolderTextBox.setFocus()
            return False
        self._task.Source = srcTxt
        self._task.Target = dstTxt
        
        self._task.UseCustomOptions = self.ui.robocopySwitchesCheckBox.isChecked()
        self._task.CustomRobocopySwitches = self.GetOptions(True)
        return True
    
    def Btn_Clicked(self, btn):
        if btn == self.ui.robocopySwitchesCheckBox:
            tmp =  Settings.RobocopySwitches.replace('  ', ' ').split(' ')
            default_params = []
            for t in tmp:
                a, _ = self.GetFlagText(t)
                default_params.append(a)
            self.ui.grpOptions.setEnabled(btn.isChecked())
            if not btn.isChecked():
                for sh in self.chks:
                    if sh.text().lower() in default_params:
                        sh.setChecked(True)
                    else:
                        sh.setChecked(False)
            self.HasChanged = True
        # Source Folder cbhange
        elif btn == self.ui.sourceFolderTextBox:
            self.ui.btnExclude.setEnabled(os.path.exists(self.ui.sourceFolderTextBox.text()))
            self.HasChanged = True
        # OK button
        elif btn == self.ui.btnOK:
            if not self.Apply():
                return
            self.accept()
        # Cancel Button
        elif btn == self.ui.btnCancel:
            self.reject()
        # Source Browser button
        elif btn == self.ui.btnBrowseSrc:
            path = QFileDialog(self).getExistingDirectory()
            self.ui.sourceFolderTextBox.setText(path)
            self._task.Source = path
            self.HasChanged = True
        # Target Browser button
        elif btn == self.ui.btnBrowseDst:
            path = QFileDialog(self).getExistingDirectory()
            self.ui.targetFolderTextBox.setText(path)
            self._task.Target = path
            self.HasChanged = True
        # Exclude Button
        elif btn == self.ui.btnExclude:
            dlg = DlgExclude(self, self._task)
            if dlg.exec_() != QDialog.Accepted:
                pass
            self._task.ExcludedAttributes = dlg.ExcludedAttributes
            self._task.ExcludedFiles = dlg.ExcludedFiles
            self._task.ExcludedFolders = dlg.ExcludedFolders
            self.HasChanged = True
        self.UpdateCmd()
        
    def UpdateCmd(self):
        srcTxt = self.ui.sourceFolderTextBox.text()
        dstTxt = self.ui.targetFolderTextBox.text()

        strOptions = self._task.GetExcludeOptions()
        strOptions += self.GetOptions(True)
        
        strCmd = 'robocopy.exe ' + srcTxt + ' ' + dstTxt + ' ' + strOptions
        self.ui.txtCmd.setText(strCmd)
        self.ui.txtCmd.setEnabled(self.ui.robocopySwitchesCheckBox.isChecked())
        
    def GetFlagText(self, key):
        tmp = key.split(':')
        val = tmp[1] if len(tmp) > 1 else ''
        a = tmp[0] if len(tmp) == 1 else tmp[0] + ':'
        return a, val
                
    def GetOptions(self, update):
        params = self._task.CustomRobocopySwitches.replace('  ', ' ').split(' ')
        for p in Settings.RobocopySwitches.replace('  ', ' ').split(' '):
            if not p in params:
                params.append(p)
        ctrls = {}
        for ch in self.chks:
            ctrls[ch.text().lower()] = ch
        if not update:
            for ch in self.chks:
                ch.setChecked(False)
            self.ui.txt_lev.setEnabled(False)
            self.ui.txt_r.setEnabled(False)
            self.ui.txt_w.setEnabled(False)
            for key in params:
                if len(key) == 0:
                    continue
                a, val = self.GetFlagText(key)
                
                if a not in ctrls:
                    continue
                ctrls[a].setChecked(True)
                if a == '/lev:':
                    self.ui.txt_lev.setEnabled(True)
                    self.ui.txt_lev.setText(val)
                elif a == '/r:':
                    self.ui.txt_r.setEnabled(True)
                    self.ui.txt_r.setText(val)
                elif a == '/w:':
                    self.ui.txt_w.setEnabled(True)
                    self.ui.txt_w.setText(val)
                
                # opt = a.lo
            self.UpdateCmd()
            return
        params.clear()
        for ch in ctrls:
            if not ctrls[ch].isChecked():
                continue
            _str = ch
            
            if ch == '/lev:':
                _str += self.ui.txt_lev.text()
            if ch == '/r:':
                _str += self.ui.txt_r.text()
            if ch == '/w:':
                _str += self.ui.txt_w.text()
            params.append(_str)

        
        return ' '.join(params)