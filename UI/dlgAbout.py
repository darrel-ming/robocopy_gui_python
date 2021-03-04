import os, copy
from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel)
from UI.Ui_DlgAbout import Ui_DlgAbout

class DlgAbout(QDialog):
    def __init__(self, parent):
        super(DlgAbout, self).__init__(parent)
        
        self.ui = Ui_DlgAbout()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Dialog|Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        # connect slots
        self.ui.btnOK.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnOK))
        
    def Btn_Clicked(self, btn):
        if btn == self.ui.btnOK:
            self.accept()
