# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPending.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_dlgPendng(object):
    def setupUi(self, dlgPendng):
        if not dlgPendng.objectName():
            dlgPendng.setObjectName(u"dlgPendng")
        dlgPendng.resize(700, 452)
        dlgPendng.setMinimumSize(QSize(700, 0))
        dlgPendng.setStyleSheet(u"QPushButton, Label{font: 10pt \"Segoe UI Symbol\";}")
        self.verticalLayout_2 = QVBoxLayout(dlgPendng)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(dlgPendng)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(32, 0))
        self.frame.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblTitle = QLabel(self.frame)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lblTitle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnInfo = QPushButton(self.frame)
        self.btnInfo.setObjectName(u"btnInfo")
        self.btnInfo.setMinimumSize(QSize(32, 32))
        self.btnInfo.setStyleSheet(u"border-image: url(:/img/UI/rsc/task.png);")

        self.horizontalLayout_2.addWidget(self.btnInfo)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(dlgPendng)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(490, 110))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 70, 31, 21))
        self.label_7.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 71, 41, 21))
        self.label_8.setStyleSheet(u"")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 50, 51, 21))
        self.label_6.setStyleSheet(u"")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 31, 31))
        self.label_3.setPixmap(QPixmap(u":/img/UI/rsc/target.png"))
        self.label_3.setScaledContents(True)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(380, 50, 51, 21))
        self.label_9.setStyleSheet(u"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 20, 271, 21))
        self.label_2.setStyleSheet(u"")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 20, 281, 21))
        self.label_5.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 10, 31, 31))
        self.label_4.setPixmap(QPixmap(u":/img/UI/rsc/task_remove.png"))
        self.label_4.setScaledContents(True)
        self.lbl_copyFolder = QLabel(self.frame_2)
        self.lbl_copyFolder.setObjectName(u"lbl_copyFolder")
        self.lbl_copyFolder.setGeometry(QRect(110, 50, 211, 21))
        self.lbl_copyFolder.setFont(font)
        self.lbl_copyFolder.setStyleSheet(u"")
        self.lbl_copyFile = QLabel(self.frame_2)
        self.lbl_copyFile.setObjectName(u"lbl_copyFile")
        self.lbl_copyFile.setGeometry(QRect(110, 70, 211, 16))
        self.lbl_copyFile.setFont(font)
        self.lbl_copyFile.setStyleSheet(u"")
        self.lbl_delFile = QLabel(self.frame_2)
        self.lbl_delFile.setObjectName(u"lbl_delFile")
        self.lbl_delFile.setGeometry(QRect(440, 70, 241, 21))
        self.lbl_delFile.setFont(font)
        self.lbl_delFile.setStyleSheet(u"")
        self.lbl_delFolders = QLabel(self.frame_2)
        self.lbl_delFolders.setObjectName(u"lbl_delFolders")
        self.lbl_delFolders.setGeometry(QRect(440, 50, 231, 21))
        self.lbl_delFolders.setFont(font)
        self.lbl_delFolders.setStyleSheet(u"")
        self.lbl_copyBytes = QLabel(self.frame_2)
        self.lbl_copyBytes.setObjectName(u"lbl_copyBytes")
        self.lbl_copyBytes.setGeometry(QRect(110, 90, 211, 16))
        self.lbl_copyBytes.setFont(font)
        self.lbl_copyBytes.setStyleSheet(u"")
        self.lbl_delBytes = QLabel(self.frame_2)
        self.lbl_delBytes.setObjectName(u"lbl_delBytes")
        self.lbl_delBytes.setGeometry(QRect(440, 90, 211, 16))
        self.lbl_delBytes.setFont(font)
        self.lbl_delBytes.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(dlgPendng)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.textEdit.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOK = QPushButton(dlgPendng)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 32))
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/okpng.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnOK.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnOK)

        self.btnCancel = QPushButton(dlgPendng)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 32))
        icon1 = QIcon()
        icon1.addFile(u":/img/UI/rsc/cancel.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnCancel.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(dlgPendng)

        QMetaObject.connectSlotsByName(dlgPendng)
    # setupUi

    def retranslateUi(self, dlgPendng):
        dlgPendng.setWindowTitle(QCoreApplication.translate("dlgPendng", u"Pending changes", None))
        self.lblTitle.setText(QCoreApplication.translate("dlgPendng", u"Theses are the pending changes to", None))
        self.btnInfo.setText("")
        self.label_7.setText(QCoreApplication.translate("dlgPendng", u"Files:", None))
        self.label_8.setText(QCoreApplication.translate("dlgPendng", u"Files:", None))
        self.label_6.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.label_3.setText("")
        self.label_9.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.label_2.setText(QCoreApplication.translate("dlgPendng", u"To be copied:", None))
        self.label_5.setText(QCoreApplication.translate("dlgPendng", u"To be deleted:", None))
        self.label_4.setText("")
        self.lbl_copyFolder.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.lbl_copyFile.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.lbl_delFile.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.lbl_delFolders.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.lbl_copyBytes.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.lbl_delBytes.setText(QCoreApplication.translate("dlgPendng", u"Folders:", None))
        self.label_10.setText(QCoreApplication.translate("dlgPendng", u"Details:", None))
        self.btnOK.setText(QCoreApplication.translate("dlgPendng", u"Proceed", None))
        self.btnCancel.setText(QCoreApplication.translate("dlgPendng", u"Abort", None))
    # retranslateUi

