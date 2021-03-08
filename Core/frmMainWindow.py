""" MainWindow

This script builds the main window of the tool.
    design file:        FrmMainForm.ui
    compiled py file:   Ui_FrmMainForm.py

"""

import copy
import datetime
import os
from threading import Thread
from PySide2.QtWidgets import (QMainWindow, QMessageBox, QHeaderView, QDialog, QLabel)  # noqa
from PySide2.QtGui import (QStandardItemModel, QStandardItem)
from PySide2.QtCore import (Qt)
from UI.Ui_FrmMainForm import Ui_MainWindow
from Core.dlgEditTask import DlgEditTask
from Core.dlgSchedule import DlgScedule
from Core.dlgHistory import DlgHistory
from Core.dlgPending import DlgPending
from Core.LabelItemDelegate import LabelItemDelegate

from Engine.MirrorTask import MirrorTask
from Engine.TaskManager import TaskManager
from Engine.LogManager import LogManager
from Engine.Settings import Settings
from Engine.callback_decorator import decorate_callback
from PySide2.QtCore import (Signal)


class MainWindow(QMainWindow):
    """
    A class used to represent an main window

    ...

    Attributes
    ----------
    ui: Ui_MainWindow
        UI wrapper instance
    _taskManager : TaskManager
        manage the tasks
    _logManager: LogManager:
        manage the log history for each task
    SelectedTask: MirrorTask
        points the current task selected on the TableView
    TaskList : List
        list of tasks
    Methods
    -------
    EnableControls(bEnable=True)
        Enables/disables UI controls with bEnable flag
    On_Change(selected, deselected)
        Tasks table view selection changed slot function
    On_Edit(index)
        TableView DoubleClicked slot function
    LoadTable()
        Makes the list of tasks
    EditTask()
        Opens the Task Edit Dialog box
    UpdateListItem(task)
        Updates the current selected item on TableView
    AddListItem(task):
        Adds the new task to the list
    TrySaveTask(task):
        Saves the task to XML file
    StartOperation(reverse):
        Perfomrs Backup/Restore operation
    _enter_toggle
        callback function before Robocopy thread begins
    _exit_toggle
        callback function before Robocopy thread finished

    Signals:
    --------
    log : (str)
        emited to print the log
    updateList: (str)
        emitted when the copy task has completed

    Slots:
    --------
    Log
        Logs the message
    Btn_Clicked(btn):
        Slot function to handle button clicks
    CopyCompleted(str_msg='')
        Slot for CopyCompleted signal comes from 'Backup/Restore' operation
    """
    # Signals
    log = Signal(str)
    updateList = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        # make UI from design UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connects slots to siganls
        self.log.connect(self.Log)
        self.updateList.connect(self.CopyCompleted)
        self.ui.btnNew.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnNew))            # noqa
        self.ui.btnEdit.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnEdit))          # noqa
        self.ui.btnRemove.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRemove))      # noqa
        self.ui.btnHistory.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnHistory))    # noqa
        self.ui.btnSchedule.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnSchedule))  # noqa
        self.ui.btnRestore.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnRestore))    # noqa
        self.ui.btnBackup.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnBackup))      # noqa

        # create the status bar
        self.ui.statusBar.addWidget(QLabel(f'{Settings.Product_Label}   '))
        self.ui.statusBar.addWidget(QLabel(f'ver:{Settings.Product_Version}   '))           # noqa
        self.linkLabel = QLabel(f'{Settings.Product_AboutLink}   ')
        self.linkLabel.setOpenExternalLinks(True)
        self.ui.statusBar.addWidget(self.linkLabel)

        # initiates the taskmanager and logmanager
        self._taskManager = TaskManager()
        self._logManager = LogManager()

        # create selectionmodel for tableview
        self.taskViewModel = QStandardItemModel(self)
        # set the model to tableview
        self.ui.tableView.setModel(self.taskViewModel)
        # connects double-clicked slot to the table
        self.ui.tableView.doubleClicked.connect(self.On_Edit)
        # connects table selct event
        self.ui.tableView.selectionModel().selectionChanged.connect(self.On_Change)         # noqa
        # overrides table cell delegate
        self.tableLabelDelegate = LabelItemDelegate(self.taskViewModel, self.ui.tableView)  # noqa
        # apply the delegate to every column
        for i in range(4):
            self.ui.tableView.setItemDelegateForColumn(i, self.tableLabelDelegate)          # noqa
        # set the Selected Task to None
        self.SelectedTask = None
        # create Task List
        self.TaskList = []
        # Loads the table
        self.LoadTable()

    def EnableControls(self, bEnable=True):
        """Enables/disables UI controls with bEnable flag.

        Parameters
        ----------
        bEnable : Bool, optional
            The flag to disable controls (default is True)
        """
        self.ui.btnNew.setEnabled(bEnable)
        self.ui.btnEdit.setEnabled(bEnable)
        self.ui.btnRemove.setEnabled(bEnable)
        self.ui.btnHistory.setEnabled(bEnable)
        self.ui.btnBackup.setEnabled(bEnable)
        self.ui.btnRestore.setEnabled(bEnable)
        self.ui.btnSchedule.setEnabled(bEnable)

    def On_Change(self,  selected, deselected):
        '''
        Tasks table view selection changed slot function
        This function switches the current task whenever user clicks
        an item on the TableView control
        Parameters:
        ----------
        selected: QModelIndex
            newly selected tableview cell
        deselected: QModelIndex
            previously selected tableview cell
        '''
        try:
            # check if there is at least one selected task
            flag = len(self.ui.tableView.selectionModel().selectedRows()) > 0
            # set the UI buttons enable/disable
            self.EnableControls(flag)
            # get the current selected index
            current_index = self.ui.tableView.selectionModel().currentIndex().row() # noqa
            # if selected index is valid
            if current_index >= 0:
                # update the current task
                self.SelectedTask = self.TaskList[current_index]
            else:
                # enables the 'New Task' button
                self.ui.btnNew.setEnabled(True)
        except Exception as e:
            print(f"On_Change Error:{e}")

    def On_Edit(self, index):
        '''
        TableView DoubleClicked slot function
        Parameters:
        -----------
        index: QModelIndex
            double-clicked Table view cell
        '''
        try:
            # updates the current task from the selected index
            self.SelectedTask = self.TaskList[index.row()]
            # Invokes the 'Edit Task' dialog
            self.EditTask()
        except Exception as e:
            print(f"On_Edit Error: {e}")

    def LoadTable(self):
        '''
            Makes the list of tasks
            This function loads the tasks in _taskManager and lists them
        '''
        try:
            # clear the table model
            self.taskViewModel.clear()
            # get the list of tasks
            self.TaskList = self._taskManager.LoadTasks()
            # for each task
            for task in self.TaskList:
                # get the scheduled state of the task
                _str = Settings.Schedule_String if task.Scheduled else Settings.UnScheduled_String      # noqa
                # inserts new Table row
                self.taskViewModel.appendRow([
                    QStandardItem(task.Source),
                    QStandardItem(task.Target),
                    QStandardItem(_str),
                    QStandardItem(task.LastOperation)])
            # names the each column label
            self.taskViewModel.setHorizontalHeaderLabels(Settings.Table_ColumnNames)                    # noqa
            # if there is at least on task, selects the first task and
            # updates the selected task
            if len(self.TaskList) > 0:
                # set the current cell
                self.ui.tableView.setCurrentIndex(
                    self.ui.tableView.model().index(0, 1))
                # updates the UI components
                self.EnableControls(True)
                # updates the selected task
                self.SelectedTask = self.TaskList[0]

            # resize column width
            wth = [200, 200, 100, 200]
            for i in range(4):
                self.ui.tableView.setColumnWidth(i, wth[i])
            # make the last column hit the end
            self.ui.tableView.horizontalHeader().setSectionResizeMode(
                3, QHeaderView.Stretch)
            # set the text align to left
            self.ui.tableView.horizontalHeader().setDefaultAlignment(
                Qt.AlignLeft)
        except Exception as e:
            print(f"Load Table Error:{e}")

    def EditTask(self):
        '''
        Opens the Task Edit Dialog box
        '''
        try:
            # if selected task is none return
            if self.SelectedTask is None:
                return
            # make new dialog instance
            dlg = DlgEditTask(self, self.SelectedTask)
            # returns if user hit the Cancel button
            if dlg.exec_() != QDialog.Accepted:
                return
            # updates the Selected Task
            self.SelectedTask = copy.deepcopy(dlg._task)
            # Saves the edited task
            if self.TrySaveTask(self.SelectedTask):
                # Updates task list
                self.UpdateListItem(self.SelectedTask)
        except Exception as e:
            print(f"Edit Task Error:{e}")

    def CopyCompleted(self, str_msg=''):
        '''
        Slot for CopyCompleted signal comes from 'Backup/Restore' operation
        '''
        try:
            # get the current timestamp
            timestamp = datetime.datetime.now().strftime(
                Settings.Log_DateFormat)
            # updates the LastOperation time
            self.SelectedTask.LastOperation = timestamp
            # updates the selected task on the TableView
            self.UpdateListItem(self.SelectedTask)
            # Save the task
            self.TrySaveTask(self.SelectedTask)
            # Puts the log
            self._logManager.AddLog(self.SelectedTask, str_msg, timestamp)
        except Exception as e:
            print(f"Copy Completed Error{e}")

    def UpdateListItem(self, task):
        '''
        Updates the current selected item on TableView
        Parameters:
        -----------
        task: MirrorTask
            currently selected task
        '''
        try:
            # if selected task is None, return
            if task is None:
                return
            # Checks if the selected task exist on task list
            index = -1
            for i in range(len(self.TaskList)):
                # compare GUIDs
                if self.TaskList[i].Guid == task.Guid:
                    index = i
                    break
            # if not EXIST, return
            if index < 0:
                return
            # updates the Task Manager
            self.TaskList[i] = self.SelectedTask
            # Rewrites the TableView item
            self.taskViewModel.setItem(
                index, 0, QStandardItem(task.Source))
            self.taskViewModel.setItem(
                index, 1, QStandardItem(task.Target))
            _str = Settings.Schedule_String if task.Scheduled else Settings.UnScheduled_String      # noqa
            self.taskViewModel.setItem(
                index, 2, QStandardItem(_str))
            self.taskViewModel.setItem(
                index, 3, QStandardItem(task.LastOperation))
        except Exception as e:
            print(f"UpdateListItem Error:{e}")

    def Btn_Clicked(self, btn):
        '''
        Slot function to handle button clicks
        Parameters:
        -----------
        btn : QPushButton
            sender that user hit the button
        '''
        try:
            # 'New Task' button
            if btn == self.ui.btnNew:
                # creates new task instance
                new_task = MirrorTask()
                # Opens the 'Edit Task' dialog with created task
                dlg = DlgEditTask(self, new_task)
                # if 'Cancel' was hit, return
                if dlg.exec_() != QDialog.Accepted:
                    return
                # updates the created task from dialog
                new_task = copy.deepcopy(dlg._task)
                # saves the new task
                if self.TrySaveTask(new_task):
                    # and adds to the list
                    self.AddListItem(new_task)
            # 'Edit' button
            elif btn == self.ui.btnEdit:
                # invokes EditTask()
                self.EditTask()
            # Remove button
            elif btn == self.ui.btnRemove:
                # check if there is anyone selected
                indices = self.ui.tableView.selectionModel().selectedRows()
                # if None of them is selected return
                if len(indices) == 0:
                    return
                # Confirms if user really wants to remove
                res = QMessageBox.question(
                    self,
                    'Confirmation',
                    Settings.Task_Remove_Msg,
                    QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No))  # noqa
                if res == QMessageBox.No:
                    return
                try:
                    # delete task from logManager
                    self._logManager.DeleteTask(self.SelectedTask)
                    # delete task from taskManager
                    self._taskManager.DeleteTask(self.SelectedTask)
                    # set the Selected task as None
                    self.SelectedTask = None
                except Exception:
                    QMessageBox.information(
                        self,
                        "I/O Error",
                        f"{Settings.Task_Remove_ErrMsg}")
                    return
                # if successfully removed, reload the list
                self.LoadTable()
            # History button
            elif btn == self.ui.btnHistory:
                # Opens the History Dialog with selected task
                dlg = DlgHistory(self, self.SelectedTask)
                dlg.exec_()
            # Schedule button
            elif btn == self.ui.btnSchedule:
                # Opens the Schedule Dialog with slected task
                dlg = DlgScedule(self, self.SelectedTask)
                if dlg.exec_() != QDialog.Accepted:
                    return
                # Save the selected task
                if self.TrySaveTask(self.SelectedTask):
                    # Update the Table list
                    self.UpdateListItem(self.SelectedTask)
            # Restore button
            elif btn == self.ui.btnRestore:
                self.StartOperation(False)
            # Backup button
            elif btn == self.ui.btnBackup:
                self.StartOperation(True)
        except Exception as e:
            print(f'Btn_Clicked Error:{e}')

    def AddListItem(self, task):
        '''
        Adds the new task to the list
        '''
        try:
            # inserts new row
            self.taskViewModel.appendRow([
                QStandardItem(task.Source),
                QStandardItem(task.Target),
                QStandardItem(task.LastOperation)])
            # updates the Selected Task
            self.SelectedTask = task
            # inserts new task to TaskList
            self.TaskList.append(task)
            # selects the newly added row
            self.ui.tableView.setCurrentIndex(
                self.ui.tableView.model().index(
                    len(self.TaskList) - 1, 1))
        except Exception as e:
            print(f"AddListItem Err:{e}")

    def TrySaveTask(self, task):
        '''
        Saves the task to XML file
        Return Value:
        ------------
            True:   Successfully Saved
            False:  An error was raised
        '''
        result = False
        try:
            result = True
            self._taskManager.SaveTask(task)
        except Exception as ex:
            QMessageBox.information(
                self,
                "Error",
                f"{Settings.Task_Save_ErrMsg}")
            print(f"TrySaveTask Error: {ex}")
            result = False
        return result

    def StartOperation(self, reverse):
        '''
        Perfomrs Backup/Restore operation
        Parameters:
        -----------
        reverse: Boolean
            True: Backup, False: Restore
        '''
        try:
            # backups the selected task
            selectedTask = copy.deepcopy(self.SelectedTask)
            # set the direction
            selectedTask._direction = reverse
            if selectedTask is None:
                return
            # check is robocopy file path is valid
            exe_path = os.getcwd() + Settings.RoboPath
            # if not shows error msg and return
            if not os.path.exists(exe_path):
                QMessageBox.warning(self, "Error", f"{exe_path} does not exist!")
                return
            # Pops up Pending Dialog
            if DlgPending(self, selectedTask).exec_() != QDialog.Accepted:
                return
            # set the parent of selected task of this
            selectedTask.setParent(self)
            try:
                # performs robo copy
                robocopy_thread = Thread(target=decorate_callback(
                    selectedTask.run, self._enter_toggle, self._exit_toggle))
                robocopy_thread.start()
            except Exception as e:
                print(f"RoboCopy Thread Error:{e}")
        except Exception as e:
            print(f"StartOperation Error:{e}")

    def Log(self, msg=''):
        '''
        Logs the message
        Parameters:
        -----------
        msg: string
            String to be added to log view
        '''
        try:
            pre_txt = self.ui.txtLog.toPlainText()
            self.ui.txtLog.setPlainText(pre_txt + msg)
        except Exception as e:
            print(f"Log Error:{e}")

    def _enter_toggle(self):
        '''
        callback function before Robocopy thread begins
        '''
        self.EnableControls(False)

    def _exit_toggle(self):
        '''
        callback function before Robocopy thread finished
        '''
        self.EnableControls(True)
