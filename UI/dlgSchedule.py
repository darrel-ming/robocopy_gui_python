import os, copy, datetime
from PySide2.QtWidgets import (QDialog, QMessageBox, QHeaderView,
                            QFileDialog)
from PySide2.QtGui import (QPainter, QBrush, QColor, QPixmap, QStandardItemModel,
                        QStandardItem)
from PySide2.QtCore import (Qt, QRect, QTimer, QItemSelectionModel, QDate, QTime,
                            QDateTime)
from UI.Ui_DlgSchedule import Ui_DlgSchedule
from Engine.ScheduledTasksManager import ScheduledTasksManager

class DlgScedule(QDialog):
    def __init__(self, parent, mirror_task):
        super(DlgScedule, self).__init__(parent)
        
        self.ui = Ui_DlgSchedule()
        self.ui.setupUi(self)
        self._mirrorTask = mirror_task
        self._manager = ScheduledTasksManager()
        
        # connect slots
        self.ui.btnOK.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnOK))
        self.ui.btnCancel.clicked.connect(lambda: self.Btn_Clicked(self.ui.btnCancel))
        
        self.ui.comboBox.addItems(['Daily', 'Weekly', 'Monthly'])
        task = self._manager.Get(self._mirrorTask)
        
        
        if task is not None:
            time = task.NextRunTime
            dt = datetime.datetime.fromtimestamp(
            timestamp=time.timestamp(),
            tz=time.tzinfo
            )
            self.ui.checkBox.setChecked(task.Enabled)
            self.ui.dateEdit.setDate(QDate(dt.year, dt.month, dt.day))
            self.ui.timeEdit.setTime(QTime(dt.hour, dt.minute, dt.day))
        else:
            self.ui.dateEdit.setDate(QDate.currentDate())
            self.ui.timeEdit.setTime(QTime.currentTime())
        
    def Apply(self):
        sc_date = self.ui.dateEdit.date().toPython().strftime('%Y-%m-%d ')
        sc_time = self.ui.timeEdit.time().toString('hh:mm:ss')
        sc_datetime = datetime.datetime.strptime(sc_date+sc_time, "%Y-%m-%d %H:%M:%S")
        
        self._mirrorTask.Scheduled = self.ui.checkBox.isChecked()
        self._manager.Apply(self._mirrorTask, self.ui.comboBox.currentIndex(), sc_datetime)
        
        return True
    
    def Btn_Clicked(self, btn):
        if btn == self.ui.btnOK:
            if not self.Apply():
                return
            self.accept()
        # Cancel Button
        elif btn == self.ui.btnCancel:
            self.reject()
        