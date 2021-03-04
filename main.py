import os, sys
from PySide2.QtWidgets import (QApplication, QMessageBox)
from PySide2.QtCore import (Qt, QDir, QLockFile)
from UI.frmMainWindow import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())