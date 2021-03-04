# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgLog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_DlgLog(object):
    def setupUi(self, DlgLog):
        if not DlgLog.objectName():
            DlgLog.setObjectName(u"DlgLog")
        DlgLog.resize(776, 357)
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/history-icon-png-4683.png", QSize(), QIcon.Normal, QIcon.On)
        DlgLog.setWindowIcon(icon)
        DlgLog.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.verticalLayout = QVBoxLayout(DlgLog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txtEdit = QTextEdit(DlgLog)
        self.txtEdit.setObjectName(u"txtEdit")
        self.txtEdit.setMinimumSize(QSize(520, 0))
        self.txtEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.txtEdit)


        self.retranslateUi(DlgLog)

        QMetaObject.connectSlotsByName(DlgLog)
    # setupUi

    def retranslateUi(self, DlgLog):
        DlgLog.setWindowTitle(QCoreApplication.translate("DlgLog", u"Rockeycopy log", None))
    # retranslateUi

