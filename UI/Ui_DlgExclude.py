# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgExclude.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_DlgExclude(object):
    def setupUi(self, DlgExclude):
        if not DlgExclude.objectName():
            DlgExclude.setObjectName(u"DlgExclude")
        DlgExclude.resize(500, 600)
        DlgExclude.setMinimumSize(QSize(500, 600))
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/exclude.png", QSize(), QIcon.Normal, QIcon.On)
        DlgExclude.setWindowIcon(icon)
        DlgExclude.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.verticalLayout_3 = QVBoxLayout(DlgExclude)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, -1)
        self.groupBox = QGroupBox(DlgExclude)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.excludedFilesControl = QListWidget(self.groupBox)
        self.excludedFilesControl.setObjectName(u"excludedFilesControl")

        self.horizontalLayout.addWidget(self.excludedFilesControl)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnBrowseFile = QPushButton(self.groupBox)
        self.btnBrowseFile.setObjectName(u"btnBrowseFile")
        self.btnBrowseFile.setMinimumSize(QSize(90, 32))
        icon1 = QIcon()
        icon1.addFile(u":/img/UI/rsc/browse.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnBrowseFile.setIcon(icon1)

        self.verticalLayout.addWidget(self.btnBrowseFile)

        self.btnRemoveFile = QPushButton(self.groupBox)
        self.btnRemoveFile.setObjectName(u"btnRemoveFile")
        self.btnRemoveFile.setMinimumSize(QSize(0, 32))
        icon2 = QIcon()
        icon2.addFile(u":/img/UI/rsc/cancel.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnRemoveFile.setIcon(icon2)

        self.verticalLayout.addWidget(self.btnRemoveFile)

        self.txtFile = QLineEdit(self.groupBox)
        self.txtFile.setObjectName(u"txtFile")
        self.txtFile.setMinimumSize(QSize(0, 28))
        self.txtFile.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.txtFile)

        self.btnFileWild = QPushButton(self.groupBox)
        self.btnFileWild.setObjectName(u"btnFileWild")
        self.btnFileWild.setMinimumSize(QSize(0, 32))
        icon3 = QIcon()
        icon3.addFile(u":/img/UI/rsc/wildcard.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnFileWild.setIcon(icon3)

        self.verticalLayout.addWidget(self.btnFileWild)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(DlgExclude)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.chkH = QCheckBox(self.groupBox_2)
        self.chkH.setObjectName(u"chkH")

        self.horizontalLayout_4.addWidget(self.chkH)

        self.chkS = QCheckBox(self.groupBox_2)
        self.chkS.setObjectName(u"chkS")

        self.horizontalLayout_4.addWidget(self.chkS)

        self.chkE = QCheckBox(self.groupBox_2)
        self.chkE.setObjectName(u"chkE")

        self.horizontalLayout_4.addWidget(self.chkE)

        self.horizontalSpacer_2 = QSpacerItem(232, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(DlgExclude)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.excludedFoldersControl = QListWidget(self.groupBox_3)
        self.excludedFoldersControl.setObjectName(u"excludedFoldersControl")

        self.horizontalLayout_2.addWidget(self.excludedFoldersControl)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnBrowseFolder = QPushButton(self.groupBox_3)
        self.btnBrowseFolder.setObjectName(u"btnBrowseFolder")
        self.btnBrowseFolder.setMinimumSize(QSize(90, 32))
        self.btnBrowseFolder.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btnBrowseFolder)

        self.btnRemoveFolder = QPushButton(self.groupBox_3)
        self.btnRemoveFolder.setObjectName(u"btnRemoveFolder")
        self.btnRemoveFolder.setMinimumSize(QSize(0, 32))
        self.btnRemoveFolder.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btnRemoveFolder)

        self.txtFolder = QLineEdit(self.groupBox_3)
        self.txtFolder.setObjectName(u"txtFolder")
        self.txtFolder.setMinimumSize(QSize(0, 28))
        self.txtFolder.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.txtFolder)

        self.btnFolderWild = QPushButton(self.groupBox_3)
        self.btnFolderWild.setObjectName(u"btnFolderWild")
        self.btnFolderWild.setMinimumSize(QSize(0, 32))
        self.btnFolderWild.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btnFolderWild)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnOK = QPushButton(DlgExclude)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btnOK)

        self.btnCancel = QPushButton(DlgExclude)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btnCancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DlgExclude)

        QMetaObject.connectSlotsByName(DlgExclude)
    # setupUi

    def retranslateUi(self, DlgExclude):
        DlgExclude.setWindowTitle(QCoreApplication.translate("DlgExclude", u"Excluded items", None))
        self.groupBox.setTitle(QCoreApplication.translate("DlgExclude", u"Excluded files", None))
        self.btnBrowseFile.setText(QCoreApplication.translate("DlgExclude", u"Browse...   ", None))
        self.btnRemoveFile.setText(QCoreApplication.translate("DlgExclude", u"Remove       ", None))
        self.btnFileWild.setText(QCoreApplication.translate("DlgExclude", u"Add wildcard", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DlgExclude", u"Exclude files having any of thes attribues set:", None))
        self.chkH.setText(QCoreApplication.translate("DlgExclude", u"Hidden", None))
        self.chkS.setText(QCoreApplication.translate("DlgExclude", u"System", None))
        self.chkE.setText(QCoreApplication.translate("DlgExclude", u"Encrypted", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DlgExclude", u"Excluded folders", None))
        self.btnBrowseFolder.setText(QCoreApplication.translate("DlgExclude", u"Browse...   ", None))
        self.btnRemoveFolder.setText(QCoreApplication.translate("DlgExclude", u"Remove      ", None))
        self.btnFolderWild.setText(QCoreApplication.translate("DlgExclude", u"Add wildcard", None))
        self.btnOK.setText(QCoreApplication.translate("DlgExclude", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("DlgExclude", u"Cancel", None))
    # retranslateUi

