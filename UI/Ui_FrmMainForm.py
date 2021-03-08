# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmMainForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 636)
        MainWindow.setMinimumSize(QSize(800, 500))
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/1 (2).png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, -1, 9)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnBackup = QPushButton(self.centralwidget)
        self.btnBackup.setObjectName(u"btnBackup")
        self.btnBackup.setEnabled(False)
        self.btnBackup.setMinimumSize(QSize(100, 48))
        icon1 = QIcon()
        icon1.addFile(u":/img/UI/rsc/backup.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnBackup.setIcon(icon1)
        self.btnBackup.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnBackup)

        self.btnRestore = QPushButton(self.centralwidget)
        self.btnRestore.setObjectName(u"btnRestore")
        self.btnRestore.setEnabled(False)
        self.btnRestore.setMinimumSize(QSize(100, 48))
        icon2 = QIcon()
        icon2.addFile(u":/img/UI/rsc/restore.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnRestore.setIcon(icon2)
        self.btnRestore.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnRestore)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnNew = QPushButton(self.centralwidget)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setEnabled(True)
        self.btnNew.setMinimumSize(QSize(0, 42))
        icon3 = QIcon()
        icon3.addFile(u":/img/UI/rsc/task_add.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnNew.setIcon(icon3)

        self.verticalLayout.addWidget(self.btnNew)

        self.btnEdit = QPushButton(self.centralwidget)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setEnabled(False)
        self.btnEdit.setMinimumSize(QSize(0, 42))
        icon4 = QIcon()
        icon4.addFile(u":/img/UI/rsc/task.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnEdit.setIcon(icon4)

        self.verticalLayout.addWidget(self.btnEdit)

        self.btnRemove = QPushButton(self.centralwidget)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setEnabled(False)
        self.btnRemove.setMinimumSize(QSize(0, 42))
        icon5 = QIcon()
        icon5.addFile(u":/img/UI/rsc/task_remove.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnRemove.setIcon(icon5)

        self.verticalLayout.addWidget(self.btnRemove)

        self.btnSchedule = QPushButton(self.centralwidget)
        self.btnSchedule.setObjectName(u"btnSchedule")
        self.btnSchedule.setEnabled(False)
        self.btnSchedule.setMinimumSize(QSize(0, 42))
        icon6 = QIcon()
        icon6.addFile(u":/img/UI/rsc/gnome-schedule-icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnSchedule.setIcon(icon6)

        self.verticalLayout.addWidget(self.btnSchedule)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txtLog = QTextEdit(self.centralwidget)
        self.txtLog.setObjectName(u"txtLog")
        self.txtLog.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtLog)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnHistory = QPushButton(self.centralwidget)
        self.btnHistory.setObjectName(u"btnHistory")
        self.btnHistory.setEnabled(False)
        self.btnHistory.setMinimumSize(QSize(0, 42))
        icon7 = QIcon()
        icon7.addFile(u":/img/UI/rsc/history-icon-png-4683.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnHistory.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.btnHistory)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet(u"QStatusBar{border-top: 1px outset grey;}")
        self.statusBar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RocketCopy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tasks:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Completed operations:", None))
        self.btnBackup.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.btnRestore.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"Edit        ", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"Remove ", None))
        self.btnSchedule.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.btnHistory.setText(QCoreApplication.translate("MainWindow", u"History  ", None))
    # retranslateUi

