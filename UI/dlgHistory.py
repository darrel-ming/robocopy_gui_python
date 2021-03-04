from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel)
from UI.Ui_DlgHistory import Ui_DlgHistory
from UI.dlgLog import DlgLog
from Engine.LogManager import LogManager
from Engine.MirrorTask import MirrorTask
import os

class DlgHistory(QDialog):
    def __init__(self, parent, task):
        super(DlgHistory, self).__init__(parent)
        self.ui = Ui_DlgHistory()
        self.ui.setupUi(self)
        
        self._task = task
        self.logManager = LogManager()
        
        self.taskViewModel = QStandardItemModel(self)
        self.ui.tableView.setModel(self.taskViewModel)
        self.ui.tableView.doubleClicked.connect(self.On_View)
        self.log_data = []
        self.LoadTable()
        
    def On_View(self, mi):
        log_name = self.log_data[mi.row()]['dataRef']
        path = os.getcwd() + '\\Logs\\' + self._task.Guid + '\\' + log_name
        DlgLog(self, path).exec_()

    def LoadTable(self):
        self.taskViewModel.clear()
        self.log_data = self.logManager.LoadLogs(self._task.Guid)
        
        for task in self.log_data:
            self.taskViewModel.appendRow([QStandardItem(task['timeStamp']), QStandardItem(task['message'])])
        self.taskViewModel.setHorizontalHeaderLabels(['Timestamp', 'Task'])
        
        self.ui.tableView.setColumnWidth(0, 200)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        