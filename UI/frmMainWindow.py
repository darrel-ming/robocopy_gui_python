import copy, datetime
from threading import Thread
from PySide2.QtWidgets import (QMainWindow, QMessageBox, QHeaderView,
                            QDialog, QLabel)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel)
from UI.Ui_FrmMainForm import Ui_MainWindow
from UI.dlgEditTask import DlgEditTask
from UI.dlgSchedule import DlgScedule
from UI.dlgAbout import DlgAbout
from UI.dlgHistory import DlgHistory
from UI.dlgPending import DlgPending

from Engine.MirrorTask import MirrorTask
from Engine.TaskManager import TaskManager
from Engine.LogManager import LogManager
from Engine.callback_decorator import decorate_callback
from PySide2.QtCore import (QTimer, Signal)

class MainWindow(QMainWindow):
    log = Signal(str)
    updateList = Signal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.log.connect(self.Log)
        self.updateList.connect(self.CopyCompleted)
        # connect signals
        self.ui.btnNew.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnNew))
        self.ui.btnEdit.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnEdit))
        self.ui.btnRemove.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRemove))
        self.ui.btnHistory.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnHistory))
        self.ui.btnSchedule.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnSchedule))

        self.ui.btnRestore.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRestore))
        self.ui.btnBackup.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBackup))
        
        self.ui.statusBar.addWidget(QLabel('RocketCopy   '))
        self.ui.statusBar.addWidget(QLabel('ver:1.0   '))
        self.linkLabel = QLabel('Help: <a href=\"https://www.lundgrensimon.com/rocketcopy/\">lundgrensimon.com/rocketcopy</a>   ')
        
        self.linkLabel.setOpenExternalLinks(True)
        self.ui.statusBar.addWidget(self.linkLabel)
        
        self._taskManager = TaskManager()
        self._logManager = LogManager()
        self.taskViewModel = QStandardItemModel(self)
        self.ui.tableView.setModel(self.taskViewModel)
        self.ui.tableView.doubleClicked.connect(self.On_Edit)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.On_Change)
        
        self.SelectedTask = None
        self.TaskList = []
        self.LoadTable()
        
    def EnableControls(self, flag):
        self.ui.btnNew.setEnabled(flag)
        self.ui.btnEdit.setEnabled(flag)
        self.ui.btnRemove.setEnabled(flag)
        self.ui.btnHistory.setEnabled(flag)
        self.ui.btnBackup.setEnabled(flag)
        self.ui.btnRestore.setEnabled(flag)
        self.ui.btnSchedule.setEnabled(flag)
        
        
    def On_Change(self,  selected, deselecte):
        flag = len(self.ui.tableView.selectionModel().selectedRows()) > 0
        current_index = self.ui.tableView.selectionModel().currentIndex().row()
        self.EnableControls(flag)
        self.SelectedTask = self.TaskList[current_index]
        
    def On_Edit(self, mi):
        self.SelectedTask = self.TaskList[mi.row()]
        self.EditTask()
        

    def LoadTable(self):
        self.taskViewModel.clear()
        self.TaskList = self._taskManager.LoadTasks()
        for task in self.TaskList:
            _str = 'Yes' if task.Scheduled else 'No'
            self.taskViewModel.appendRow([QStandardItem(task.Source), QStandardItem(task.Target), QStandardItem(_str), QStandardItem(task.LastOperation)])
        self.taskViewModel.setHorizontalHeaderLabels(['Source', 'Destination', 'Scheduled', 'Last successful operation'])
        if len(self.TaskList) > 0:
            self.ui.tableView.setCurrentIndex(self.ui.tableView.model().index(0,1))
            self.EnableControls(True)
            self.SelectedTask = self.TaskList[0]
            
        wth = [150, 150, 100, 200]
        for i in range(3):
            self.ui.tableView.setColumnWidth(i, wth[i])
        self.ui.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        
        
    def EditTask(self):
        if self.SelectedTask is None:
            return
        dlg = DlgEditTask(self, self.SelectedTask)
        if dlg.exec_() != QDialog.Accepted:
            return
        self.SelectedTask = copy.deepcopy(dlg._task)
        if self.TrySaveTask(self.SelectedTask):
            self.UpdateListItem(self.SelectedTask)
        
    def CopyCompleted(self, str_msg):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.SelectedTask.LastOperation = timestamp
        self.UpdateListItem(self.SelectedTask)
        self.TrySaveTask(self.SelectedTask)
        
        self._logManager.AddLog(self.SelectedTask, str_msg, timestamp)
        
        
    def UpdateListItem(self, task):
        index = -1
        for i in range(len(self.TaskList)):
            if self.TaskList[i].Guid == task.Guid:
                index = i
                break
        if index < 0:
            return
        self.TaskList[i] = self.SelectedTask
        self.taskViewModel.setItem(index, 0, QStandardItem(task.Source))
        self.taskViewModel.setItem(index, 1, QStandardItem(task.Target))
        self.taskViewModel.setItem(index, 2, QStandardItem('Yes' if task.Scheduled else 'No'))
        self.taskViewModel.setItem(index, 3, QStandardItem(task.LastOperation))
        
    def Btn_Clicked(self, btn):
        if btn == self.ui.btnNew:
            new_task = MirrorTask()
            dlg = DlgEditTask(self, new_task)
            if dlg.exec_() != QDialog.Accepted:
                return
            new_task = copy.deepcopy(dlg._task)
            if self.TrySaveTask(new_task):
                self.AddListItem(new_task)
                
        elif btn == self.ui.btnEdit:
            self.EditTask()
        elif btn == self.linkLabel:
            print('Label')
        elif btn == self.ui.btnRemove:
            indices = self.ui.tableView.selectionModel().selectedRows()
            if len(indices) == 0:
                return
            row = indices[0].row()
            res = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to remove the selected task?',
                                QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No))
            if res == QMessageBox.No:
                return
            try:
                self._taskManager.DeleteTask(self.SelectedTask)
                pass
            except Exception as e:
                QMessageBox.information(self, "I/O Error",  "The mirror task could not be deleted.\n\n" + e)
                return
            self.taskViewModel.removeRow(row)
        elif btn == self.ui.btnHistory:
            dlg = DlgHistory(self, self.SelectedTask)
            dlg.exec_()
        elif btn == self.ui.btnSchedule:
            dlg = DlgScedule(self, self.SelectedTask)
            if dlg.exec_() != QDialog.Accepted:
                return
            if self.TrySaveTask(self.SelectedTask):
                self.UpdateListItem(self.SelectedTask)
            
        elif btn == self.ui.btnRestore:
            self.StartOperation(False)
        elif btn == self.ui.btnBackup:
            self.StartOperation(True)
        
    def AddListItem(self, task):
        self.taskViewModel.appendRow([QStandardItem(task.Source), QStandardItem(task.Target), QStandardItem(task.LastOperation)])
        self.SelectedTask = task
        self.TaskList.append(task)
        self.ui.tableView.setCurrentIndex(self.ui.tableView.model().index(len(self.TaskList) - 1,1))
        
    def TrySaveTask(self, task):
        result = False
        try:
            result = True
            self._taskManager.SaveTask(task)

        except Exception as ex:
            QMessageBox.information(self, "Error", "The mirror task could not be saved.\n\n" + str(ex))
            result = False
            
        return result
    
    def StartOperation(self, reverse):
        selectedTask = copy.deepcopy(self.SelectedTask)
        selectedTask._direction = reverse
        if selectedTask is None:
            return
        if DlgPending(self, selectedTask).exec_() != QDialog.Accepted:
            return
        selectedTask.setParent(self)
        self.robocopy_thread = Thread(target=decorate_callback(
            selectedTask.run, self._enter_toggle, self._exit_toggle))
        self.robocopy_thread.start()
        
        
    def Log(self, msg):
        pre_txt = self.ui.txtLog.toPlainText()
        self.ui.txtLog.setPlainText(pre_txt + msg)
        
    def _enter_toggle(self):
        self.EnableControls(False)
    
    def _exit_toggle(self):
        self.EnableControls(True)
        # self.UpdateListItem(self.SelectedTask)