# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAbout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        if not DlgAbout.objectName():
            DlgAbout.setObjectName(u"DlgAbout")
        DlgAbout.resize(400, 219)
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/RoboMirror.ico", QSize(), QIcon.Normal, QIcon.On)
        DlgAbout.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DlgAbout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(DlgAbout)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(DlgAbout)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOK = QPushButton(DlgAbout)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 32))

        self.horizontalLayout.addWidget(self.btnOK)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgAbout)

        QMetaObject.connectSlotsByName(DlgAbout)
    # setupUi

    def retranslateUi(self, DlgAbout):
        DlgAbout.setWindowTitle(QCoreApplication.translate("DlgAbout", u"About", None))
        self.label_2.setText(QCoreApplication.translate("DlgAbout", u"RoboCopy 1.0", None))
        self.label.setText(QCoreApplication.translate("DlgAbout", u"\u200b RocketCopy is a GUI (graphical user interface) for the built-in Windows command line tool RoboCopy which helps you mirroring local as well as network directories with ease. Please visit \u200b <a href=\"https://www.lundgrensimon.com/rocketcopy/\">https://www.lundgrensimon.com/rocketcopy/</a> \u200b for complete and updated information about the tool and for support.", None))
        self.btnOK.setText(QCoreApplication.translate("DlgAbout", u"&OK", None))
    # retranslateUi

