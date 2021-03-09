import os
import datetime
from PySide2.QtWidgets import (QDialog, QMessageBox)
from PySide2.QtCore import (QDate, QTime)
from UI.Ui_DlgSchedule import Ui_DlgSchedule
from Engine.ScheduledTasksManager import ScheduledTasksManager
from Engine.Settings import Settings


class DlgScedule(QDialog):
    '''
    Class for task schedule dialog
    Attributes:
    ------------
    ui : Ui_DlgSchedule
        UI wrapper
    _mirrorTask : MirrorTask
        MirrorTask to register to 'Task Sceduler'
    _manager : SchedulerTasksManager()
        Manager to register/remove Task Schedules
    Methods:
    ----------
    EnableControls():
        Enable/disable controls according to the checkbox
    Apply():
        register/remove the mirrortask to system 'Task Scheduler'
    Slots:
    ----------
    Btn_Clicked():
        button click handler
    '''

    def __init__(self, parent, mirror_task):
        super(DlgScedule, self).__init__(parent)
        # setup UI
        self.ui = Ui_DlgSchedule()
        self.ui.setupUi(self)
        # selected task
        self._mirrorTask = mirror_task
        # schedule manager
        self._manager = ScheduledTasksManager()

        # connect slots
        self.ui.btnOK.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.btnCancel))
        self.ui.checkBox.clicked.connect(
            lambda: self.Btn_Clicked(self.ui.checkBox))
        # set checkbox
        self.ui.checkBox.setChecked(False)
        # make schedule types
        self.ui.comboBox.addItems(Settings.SCHEDULE_TYPES)
        # get task schedule task
        task = self._manager.Get(self._mirrorTask)
        try:
            if task is not None:
                # get next triger time
                time = task.LastRunTime
                # get time stamp
                dt = datetime.datetime.fromtimestamp(
                    timestamp=time.timestamp(),
                    tz=time.tzinfo)
                # set checkbox
                self.ui.checkBox.setChecked(task.Enabled)
                # set date & time
                self.ui.dateEdit.setDate(QDate(dt.year, dt.month, dt.day))
                self.ui.timeEdit.setTime(QTime(dt.hour, dt.minute, dt.day))
            else:
                self.ui.dateEdit.setDate(QDate.currentDate())
                self.ui.timeEdit.setTime(QTime.currentTime())
            # enable controls
            self.EnableControls()
        except Exception as e:
            print(f'Schedule Dlg Err:{e}')

    def Apply(self):
        '''
        register/remove the mirrortask to system 'Task Scheduler'
        '''
        # get date
        sc_date = self.ui.dateEdit.date().toPython().strftime('%Y-%m-%d ')
        # get time
        sc_time = self.ui.timeEdit.time().toString('hh:mm:ss')
        # merge date & time
        sc_datetime = datetime.datetime.strptime(
            sc_date+sc_time,
            "%Y-%m-%d %H:%M:%S")
        self._mirrorTask.Scheduled = self.ui.checkBox.isChecked()
        self._manager.Apply(
            self._mirrorTask,
            self.ui.comboBox.currentIndex(),
            sc_datetime)
        return True

    def Btn_Clicked(self, btn):
        '''
        button click handler
        '''
        # OK button is pressed
        if btn == self.ui.btnOK:
            # check if user wants to register
            if self.ui.checkBox.isChecked():
                # check if robocopy tool exists
                exe_path = os.getcwd() + Settings.RoboPath
                # if not shows error msg
                if not os.path.exists(exe_path):
                    QMessageBox.warning(
                        self,
                        "Error",
                        f'{exe_path} does not exist!')
                    return
            if not self.Apply():
                return
            self.accept()
        # Cancel Button
        elif btn == self.ui.btnCancel:
            self.reject()
        # Enable/disable checkbox is pressed
        elif btn == self.ui.checkBox:
            # Update UI components
            self.EnableControls()

    def EnableControls(self):
        '''
        Enable/disable controls according to the checkbox
        '''
        # get the state of the checkbox
        bEdit = self.ui.checkBox.isChecked()
        # update the state of the UI components
        # check box
        self.ui.comboBox.setEnabled(bEdit)
        # date edit control
        self.ui.dateEdit.setEnabled(bEdit)
        # time edit control
        self.ui.timeEdit.setEnabled(bEdit)
