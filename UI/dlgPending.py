import os, copy
from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem, QFont)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel)
from UI.Ui_DlgPending import Ui_dlgPendng
import time, subprocess

class DlgPending(QDialog):
    def __init__(self, parent, task):
        super(DlgPending, self).__init__(parent)
        
        self.ui = Ui_dlgPendng()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Dialog|Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        
        # connect slots
        self.ui.btnOK.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnCancel))
        cmd, src, dst = task.GetParams()
        cmd.append('/l')
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout = proc.communicate()[0].decode('utf-8')
        str_msg = stdout
        
        font = QFont()
        font.setFamily("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.ui.textEdit.setCurrentFont(font)
        self.ui.textEdit.setText(str_msg)

        info = {'dirs':[], 'files':[], 'bytes':[]}
        for line in stdout.split('\r\n'):
            if 'Dirs :' in line:
                tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0]
                if len(tmp) == 6:
                    info['dirs'] = tmp
            elif 'Files :' in line:
                tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0]
                if len(tmp) == 6:
                    info['files'] = tmp
            elif 'Bytes :' in line:
                tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0]
                if len(tmp) == 6:
                    info['bytes'] = tmp
        self.ui.lbl_copyFolder.setText('%s out of %s' % (info['dirs'][1], info['dirs'][0]))
        self.ui.lbl_delFolders.setText('%s' % (info['dirs'][5]))
        self.ui.lbl_copyFile.setText('%s out of %s' % (info['files'][1], info['files'][0]))
        self.ui.lbl_delFile.setText('%s' % (info['files'][5]))
        self.ui.lbl_copyBytes.setText('%sbytes out of %sbytes' % (info['bytes'][1], info['bytes'][0]))
        self.ui.lbl_delBytes.setText('%sbytes' % (info['bytes'][5]))
        
        
    def Btn_Clicked(self, btn):
        if btn == self.ui.btnOK:
            self.accept()
        elif btn == self.ui.btnCancel:
            self.reject()
