# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSchedule.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_DlgSchedule(object):
    def setupUi(self, DlgSchedule):
        if not DlgSchedule.objectName():
            DlgSchedule.setObjectName(u"DlgSchedule")
        DlgSchedule.resize(329, 228)
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/gnome-schedule-icon.png", QSize(), QIcon.Normal, QIcon.On)
        DlgSchedule.setWindowIcon(icon)
        DlgSchedule.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.verticalLayout = QVBoxLayout(DlgSchedule)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(DlgSchedule)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 32))

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox = QComboBox(DlgSchedule)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 32))

        self.verticalLayout.addWidget(self.comboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(DlgSchedule)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.dateEdit = QDateEdit(DlgSchedule)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 12))

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.timeEdit = QTimeEdit(DlgSchedule)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(0, 12))

        self.horizontalLayout_2.addWidget(self.timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnOK = QPushButton(DlgSchedule)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btnOK)

        self.btnCancel = QPushButton(DlgSchedule)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DlgSchedule)

        QMetaObject.connectSlotsByName(DlgSchedule)
    # setupUi

    def retranslateUi(self, DlgSchedule):
        DlgSchedule.setWindowTitle(QCoreApplication.translate("DlgSchedule", u"Schedule", None))
        self.checkBox.setText(QCoreApplication.translate("DlgSchedule", u"Perform automatic backups", None))
        self.label.setText(QCoreApplication.translate("DlgSchedule", u"Beginning:", None))
        self.btnOK.setText(QCoreApplication.translate("DlgSchedule", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgSchedule", u"Cancel", None))
    # retranslateUi

