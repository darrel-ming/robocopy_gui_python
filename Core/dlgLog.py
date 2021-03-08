from PySide2.QtWidgets import (QDialog)
from PySide2.QtGui import (QFont)
from UI.Ui_DlgLog import Ui_DlgLog


class DlgLog(QDialog):
    '''
    Dialog box to see log in deatal.
    '''
    def __init__(self, parent, log_name):
        super(DlgLog, self).__init__(parent)
        self.ui = Ui_DlgLog()
        self.ui.setupUi(self)

        font = QFont()
        font.setFamily("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.ui.txtEdit.setCurrentFont(font)

        # opens the log file
        with open(log_name, 'r') as f:
            str_res = f.read()
            # puts the content to text box
            self.ui.txtEdit.setPlainText(str_res)
