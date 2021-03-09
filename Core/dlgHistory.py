from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView)
from PySide2.QtGui import (QStandardItemModel, QStandardItem)
from PySide2.QtCore import (Qt)
from UI.Ui_DlgHistory import Ui_DlgHistory
from Core.dlgLog import DlgLog
from Engine.LogManager import LogManager
from Core.LabelItemDelegate import LabelItemDelegate
import os
from Engine.Settings import Settings


class DlgHistory(QDialog):
    '''
    Class for History Dialog
    Attributes:
    -----------
    _task : MirrorTask
        task to see history
    _logManager : LogManager
    taskViewMode : QStandardItemModel
    log_data : list
        the list of logs in the history

    Methods:
    -----------
    On_View(mi)
        opens the detail log window
    LoadTable():
        loads the history table

    Slots:
    -----------
    On_View():
        double-clicked slot for TableView
    '''

    def __init__(self, parent, task):
        '''
        Params:
        -------
        parent : FormMainWindow
        task : MirrorTask
        '''
        super(DlgHistory, self).__init__(parent)
        # initialize the UI
        self.ui = Ui_DlgHistory()
        self.ui.setupUi(self)

        try:
            # get the task from param
            self._task = task
            # initialize the logManager
            self.logManager = LogManager()
            # inits the selection model for TableView
            self.taskViewModel = QStandardItemModel(self)
            # sets the model to the TableView
            self.ui.tableView.setModel(self.taskViewModel)
            # connect double-clicked event to On_View
            self.ui.tableView.doubleClicked.connect(self.On_View)
            # set the cell delegate
            self.tableLabelDelegate = LabelItemDelegate(
                self.taskViewModel, self.ui.tableView)
            for i in range(2):
                self.ui.tableView.setItemDelegateForColumn(
                    i, self.tableLabelDelegate)
            # reset the history list
            self.log_data = []
            # loads the table
            self.LoadTable()
        except Exception as e:
            print(f'HistoryDlg Err:{e}')

    def On_View(self, mi):
        '''
        check if log file exist, and pop ups the DlgLog dialog
        Params :
        --------
        mi : ModelIndex
            selected TableView cell
        '''
        try:
            # get the log file name
            log_name = self.log_data[mi.row()]['dataRef']
            path = f'{os.getcwd()}\\{Settings.LOGS_DIR}\\{self._task.Guid}\\{log_name}' # noqa
            if not os.path.exists(path):
                QMessageBox.warning(
                    self,
                    Settings.HIST_DLG_ERR_Caption,
                    Settings.HIST_DLG_ERR_TEXT)
                return
            DlgLog(self, path).exec_()
        except Exception as e:
            print(f'On_View err:{e}')

    def LoadTable(self):
        '''
        Loads the history as the list
        '''
        try:
            # Clear the table rows
            self.taskViewModel.clear()
            # loads the log data
            self.log_data = self.logManager.LoadLogs(self._task.Guid)
            # prepare timestamp & msg
            for task in self.log_data:
                self.taskViewModel.appendRow([
                    QStandardItem(task['timeStamp']),
                    QStandardItem(task['message'])])
            # set the column header
            self.taskViewModel.setHorizontalHeaderLabels(
                Settings.HIST_TABLE_COLUMNS)
            # set the width of columns
            self.ui.tableView.setColumnWidth(0, 200)
            # set last column as stretchable
            self.ui.tableView.horizontalHeader().setSectionResizeMode(
                1, QHeaderView.Stretch)
            # set text align as left
            self.ui.tableView.horizontalHeader().setDefaultAlignment(
                Qt.AlignLeft)
        except Exception as e:
            print(f'HistryDlg/LoadTable Err:{e}')
