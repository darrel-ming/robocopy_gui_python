# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgHistory.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_DlgHistory(object):
    def setupUi(self, DlgHistory):
        if not DlgHistory.objectName():
            DlgHistory.setObjectName(u"DlgHistory")
        DlgHistory.resize(547, 379)
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/history-icon-png-4683.png", QSize(), QIcon.Normal, QIcon.On)
        DlgHistory.setWindowIcon(icon)
        DlgHistory.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.verticalLayout = QVBoxLayout(DlgHistory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame = QFrame(DlgHistory)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(32, 60))
        self.frame.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnInfo = QPushButton(self.frame)
        self.btnInfo.setObjectName(u"btnInfo")
        self.btnInfo.setMinimumSize(QSize(32, 32))
        self.btnInfo.setStyleSheet(u"border-image: url(:/img/UI/rsc/history-icon-png-4683.png);")

        self.horizontalLayout_2.addWidget(self.btnInfo)


        self.verticalLayout.addWidget(self.frame)

        self.tableView = QTableView(DlgHistory)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(DlgHistory)

        QMetaObject.connectSlotsByName(DlgHistory)
    # setupUi

    def retranslateUi(self, DlgHistory):
        DlgHistory.setWindowTitle(QCoreApplication.translate("DlgHistory", u"RocketCopy task history", None))
        self.label.setText(QCoreApplication.translate("DlgHistory", u"This is the complete history of the selected task.\n"
" Double-click an entry to view the associated Rocketcopy log.", None))
        self.btnInfo.setText("")
    # retranslateUi

