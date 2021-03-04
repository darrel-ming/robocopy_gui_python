from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem, QFont)
from PySide2.QtCore import (QRect, QTimer, QItemSelectionModel)
from Engine.LogManager import LogManager
from Engine.MirrorTask import MirrorTask
from UI.Ui_DlgLog import Ui_DlgLog
import os

class DlgLog(QDialog):
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
        
        with open(log_name, 'r') as f:
            str_res = f.read()
            self.ui.txtEdit.setPlainText(str_res)