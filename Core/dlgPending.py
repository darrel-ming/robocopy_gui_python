from PySide2.QtWidgets import (QDialog)
from PySide2.QtGui import (QFont)
from PySide2.QtCore import (Qt)
from UI.Ui_DlgPending import Ui_dlgPendng
import subprocess


class DlgPending(QDialog):
    '''
    Class for Pending Dialog
    Attributes:
    ------------
    Methods:
    ------------
    Slots:
    ------------
    Btn_Clicked():
        slot for button clicks
    '''

    def __init__(self, parent, task):
        '''
        Params:
        -------
        parent: FrmMainWindow
        task : MirrorTask
        '''
        super(DlgPending, self).__init__(parent)

        # init UI
        self.ui = Ui_dlgPendng()
        self.ui.setupUi(self)
        # removes the help button
        self.setWindowFlags(
            Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        # connect slots
        self.ui.btnOK.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnCancel))
        # get task params
        cmd, src, dst = task.GetParams()
        # append '/l' switch
        cmd.append('/l')
        # prepare subprocess
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # get output of result
        stdout = proc.communicate()[0].decode('utf-8')
        str_msg = stdout

        # make font so each character's width is same
        font = QFont()
        font.setFamily("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.ui.textEdit.setCurrentFont(font)
        self.ui.textEdit.setText(str_msg)

        # parse the pending result
        # ex: dirs[1,5,0] means 1 out of 5
        info = {'dirs': [], 'files': [], 'bytes': []}
        try:
            # split each line
            for line in stdout.split('\r\n'):
                # if current line is for directory
                if 'Dirs :' in line:
                    tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0] # noqa
                    if len(tmp) == 6:
                        info['dirs'] = tmp
                # if current line is for files
                elif 'Files :' in line:
                    tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0] # noqa
                    if len(tmp) == 6:
                        info['files'] = tmp
                # if current line is for bytes
                elif 'Bytes :' in line:
                    tmp = [a for a in line.split(':')[1].split('  ') if len(a) > 0] # noqa
                    if len(tmp) == 6:
                        info['bytes'] = tmp
            # check out pending result is valid
            if len(info['dirs']) == 0:
                self.ui.btnOK.setEnabled(False)
                return
            # sets the anaylsis numbers
            # dir copy
            self.ui.lbl_copyFolder.setText(
                f"{info['dirs'][1]} out of {info['dirs'][0]}")
            # dir del
            self.ui.lbl_delFolders.setText(
                f"{info['dirs'][5]}")
            # file copy
            self.ui.lbl_copyFile.setText(
                f"{info['files'][1]} out of {info['files'][0]}")
            # dir del
            self.ui.lbl_delFile.setText(
                f"{info['files'][5]}")
            # bytes copy
            self.ui.lbl_copyBytes.setText(
                f"{info['bytes'][1]}bytes out of {info['bytes'][0]}bytes")
            # bytes del
            self.ui.lbl_delBytes.setText(
                f"{info['bytes'][5]}bytes")
        except Exception as e:
            print(f'Pending dlg err:{e}')

    def Btn_Clicked(self, btn):
        '''
        slot for button click event
        params:
        -------
        btn: QPushButton
            Button that send click signal
        '''
        # OK button
        if btn == self.ui.btnOK:
            self.accept()
        # Cancel button
        elif btn == self.ui.btnCancel:
            self.reject()
