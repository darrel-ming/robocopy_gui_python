"""RocketCopy

This script allows the user to copy batch of folder and files using
the robocopy based on UI interface.

This tool requires robocopy.exe in /Tool directory.

This script requires that `PySide2` be installed within the Python
environment you are running this script in.

"""

import sys
from PySide2.QtWidgets import QApplication
from Core.frmMainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

