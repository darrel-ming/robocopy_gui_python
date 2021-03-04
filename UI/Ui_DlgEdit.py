# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgEdit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import rsc_rc

class Ui_EditTask(object):
    def setupUi(self, EditTask):
        if not EditTask.objectName():
            EditTask.setObjectName(u"EditTask")
        EditTask.resize(518, 615)
        EditTask.setStyleSheet(u"font: 10pt \"Segoe UI Symbol\";")
        self.verticalLayout = QVBoxLayout(EditTask)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(EditTask)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(24, 24))
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setStyleSheet(u"border-image: url(:/img/UI/rsc/task.png);")

        self.horizontalLayout.addWidget(self.label_4)

        self.label = QLabel(EditTask)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.sourceFolderTextBox = QLineEdit(EditTask)
        self.sourceFolderTextBox.setObjectName(u"sourceFolderTextBox")
        self.sourceFolderTextBox.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.sourceFolderTextBox)

        self.btnBrowseSrc = QPushButton(EditTask)
        self.btnBrowseSrc.setObjectName(u"btnBrowseSrc")
        self.btnBrowseSrc.setMinimumSize(QSize(0, 32))
        icon = QIcon()
        icon.addFile(u":/img/UI/rsc/browse.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnBrowseSrc.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnBrowseSrc)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.btnExclude = QPushButton(EditTask)
        self.btnExclude.setObjectName(u"btnExclude")
        self.btnExclude.setMinimumSize(QSize(0, 42))
        icon1 = QIcon()
        icon1.addFile(u":/img/UI/rsc/exclude.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnExclude.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btnExclude)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(EditTask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(24, 24))
        self.label_3.setMaximumSize(QSize(24, 24))
        self.label_3.setStyleSheet(u"border-image: url(:/img/UI/rsc/target.png);")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_2 = QLabel(EditTask)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.targetFolderTextBox = QLineEdit(EditTask)
        self.targetFolderTextBox.setObjectName(u"targetFolderTextBox")
        self.targetFolderTextBox.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_5.addWidget(self.targetFolderTextBox)

        self.btnBrowseDst = QPushButton(EditTask)
        self.btnBrowseDst.setObjectName(u"btnBrowseDst")
        self.btnBrowseDst.setMinimumSize(QSize(0, 32))
        self.btnBrowseDst.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btnBrowseDst)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.robocopySwitchesCheckBox = QCheckBox(EditTask)
        self.robocopySwitchesCheckBox.setObjectName(u"robocopySwitchesCheckBox")

        self.verticalLayout.addWidget(self.robocopySwitchesCheckBox)

        self.grpOptions = QGroupBox(EditTask)
        self.grpOptions.setObjectName(u"grpOptions")
        self.grpOptions.setEnabled(False)
        self.grpOptions.setMinimumSize(QSize(500, 160))
        self.chk_s = QCheckBox(self.grpOptions)
        self.chk_s.setObjectName(u"chk_s")
        self.chk_s.setGeometry(QRect(20, 20, 41, 17))
        self.chk_m = QCheckBox(self.grpOptions)
        self.chk_m.setObjectName(u"chk_m")
        self.chk_m.setGeometry(QRect(20, 60, 41, 17))
        self.chk_sec = QCheckBox(self.grpOptions)
        self.chk_sec.setObjectName(u"chk_sec")
        self.chk_sec.setGeometry(QRect(90, 20, 71, 17))
        self.chk_mov = QCheckBox(self.grpOptions)
        self.chk_mov.setObjectName(u"chk_mov")
        self.chk_mov.setGeometry(QRect(90, 40, 71, 17))
        self.chk_a = QCheckBox(self.grpOptions)
        self.chk_a.setObjectName(u"chk_a")
        self.chk_a.setGeometry(QRect(90, 60, 61, 17))
        self.chk_b = QCheckBox(self.grpOptions)
        self.chk_b.setObjectName(u"chk_b")
        self.chk_b.setGeometry(QRect(90, 80, 61, 17))
        self.chk_copyall = QCheckBox(self.grpOptions)
        self.chk_copyall.setObjectName(u"chk_copyall")
        self.chk_copyall.setGeometry(QRect(170, 20, 91, 17))
        self.chk_nocopy = QCheckBox(self.grpOptions)
        self.chk_nocopy.setObjectName(u"chk_nocopy")
        self.chk_nocopy.setGeometry(QRect(170, 40, 101, 17))
        self.chk_mir = QCheckBox(self.grpOptions)
        self.chk_mir.setObjectName(u"chk_mir")
        self.chk_mir.setGeometry(QRect(170, 60, 71, 17))
        self.chk_zb = QCheckBox(self.grpOptions)
        self.chk_zb.setObjectName(u"chk_zb")
        self.chk_zb.setGeometry(QRect(170, 80, 71, 17))
        self.chk_create = QCheckBox(self.grpOptions)
        self.chk_create.setObjectName(u"chk_create")
        self.chk_create.setGeometry(QRect(290, 20, 101, 17))
        self.chk_purge = QCheckBox(self.grpOptions)
        self.chk_purge.setObjectName(u"chk_purge")
        self.chk_purge.setGeometry(QRect(290, 40, 111, 17))
        self.chk_move = QCheckBox(self.grpOptions)
        self.chk_move.setObjectName(u"chk_move")
        self.chk_move.setGeometry(QRect(290, 60, 111, 17))
        self.chk_fat = QCheckBox(self.grpOptions)
        self.chk_fat.setObjectName(u"chk_fat")
        self.chk_fat.setGeometry(QRect(290, 80, 71, 17))
        self.chk_copy = QCheckBox(self.grpOptions)
        self.chk_copy.setObjectName(u"chk_copy")
        self.chk_copy.setGeometry(QRect(290, 100, 81, 17))
        self.chk_lev = QCheckBox(self.grpOptions)
        self.chk_lev.setObjectName(u"chk_lev")
        self.chk_lev.setGeometry(QRect(406, 20, 51, 17))
        self.txt_lev = QLineEdit(self.grpOptions)
        self.txt_lev.setObjectName(u"txt_lev")
        self.txt_lev.setGeometry(QRect(455, 18, 31, 20))
        self.chk_xo = QCheckBox(self.grpOptions)
        self.chk_xo.setObjectName(u"chk_xo")
        self.chk_xo.setGeometry(QRect(20, 80, 51, 20))
        self.chk_v = QCheckBox(self.grpOptions)
        self.chk_v.setObjectName(u"chk_v")
        self.chk_v.setGeometry(QRect(20, 40, 51, 20))
        self.chk_tbd = QCheckBox(self.grpOptions)
        self.chk_tbd.setObjectName(u"chk_tbd")
        self.chk_tbd.setGeometry(QRect(20, 100, 61, 17))
        self.chk_np = QCheckBox(self.grpOptions)
        self.chk_np.setObjectName(u"chk_np")
        self.chk_np.setGeometry(QRect(170, 100, 81, 17))
        self.chk_z = QCheckBox(self.grpOptions)
        self.chk_z.setObjectName(u"chk_z")
        self.chk_z.setGeometry(QRect(90, 100, 71, 17))
        self.chk_e = QCheckBox(self.grpOptions)
        self.chk_e.setObjectName(u"chk_e")
        self.chk_e.setGeometry(QRect(406, 80, 81, 17))
        self.txt_r = QLineEdit(self.grpOptions)
        self.txt_r.setObjectName(u"txt_r")
        self.txt_r.setGeometry(QRect(455, 40, 31, 20))
        self.chk_r = QCheckBox(self.grpOptions)
        self.chk_r.setObjectName(u"chk_r")
        self.chk_r.setGeometry(QRect(406, 40, 51, 17))
        self.txt_w = QLineEdit(self.grpOptions)
        self.txt_w.setObjectName(u"txt_w")
        self.txt_w.setGeometry(QRect(455, 62, 31, 20))
        self.chk_w = QCheckBox(self.grpOptions)
        self.chk_w.setObjectName(u"chk_w")
        self.chk_w.setGeometry(QRect(406, 62, 51, 17))
        self.chk_fft = QCheckBox(self.grpOptions)
        self.chk_fft.setObjectName(u"chk_fft")
        self.chk_fft.setGeometry(QRect(406, 100, 81, 17))

        self.verticalLayout.addWidget(self.grpOptions)

        self.label_5 = QLabel(EditTask)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.txtCmd = QTextEdit(EditTask)
        self.txtCmd.setObjectName(u"txtCmd")

        self.verticalLayout.addWidget(self.txtCmd)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.btnOK = QPushButton(EditTask)
        self.btnOK.setObjectName(u"btnOK")
        self.btnOK.setMinimumSize(QSize(0, 42))
        icon2 = QIcon()
        icon2.addFile(u":/img/UI/rsc/okpng.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnOK.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.btnOK)

        self.btnCancel = QPushButton(EditTask)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(0, 42))
        icon3 = QIcon()
        icon3.addFile(u":/img/UI/rsc/cancel.png", QSize(), QIcon.Normal, QIcon.On)
        self.btnCancel.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(EditTask)

        QMetaObject.connectSlotsByName(EditTask)
    # setupUi

    def retranslateUi(self, EditTask):
        EditTask.setWindowTitle(QCoreApplication.translate("EditTask", u"Edit task", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("EditTask", u"Source folder:", None))
        self.btnBrowseSrc.setText(QCoreApplication.translate("EditTask", u"Browse", None))
        self.btnExclude.setText(QCoreApplication.translate("EditTask", u"Excluded Items...", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("EditTask", u"Destination folder", None))
        self.btnBrowseDst.setText(QCoreApplication.translate("EditTask", u"Browse", None))
        self.robocopySwitchesCheckBox.setText(QCoreApplication.translate("EditTask", u"Custom copy options", None))
        self.grpOptions.setTitle(QCoreApplication.translate("EditTask", u"Copy options", None))
        self.chk_s.setText(QCoreApplication.translate("EditTask", u"/S", None))
        self.chk_m.setText(QCoreApplication.translate("EditTask", u"/M", None))
        self.chk_sec.setText(QCoreApplication.translate("EditTask", u"/SEC", None))
        self.chk_mov.setText(QCoreApplication.translate("EditTask", u"/MOV", None))
        self.chk_a.setText(QCoreApplication.translate("EditTask", u"/A", None))
        self.chk_b.setText(QCoreApplication.translate("EditTask", u"/B", None))
        self.chk_copyall.setText(QCoreApplication.translate("EditTask", u"/COPYALL", None))
        self.chk_nocopy.setText(QCoreApplication.translate("EditTask", u"/NOCOPY", None))
        self.chk_mir.setText(QCoreApplication.translate("EditTask", u"/MIR", None))
        self.chk_zb.setText(QCoreApplication.translate("EditTask", u"/ZB", None))
        self.chk_create.setText(QCoreApplication.translate("EditTask", u"/CREATE", None))
        self.chk_purge.setText(QCoreApplication.translate("EditTask", u"/PURGE", None))
        self.chk_move.setText(QCoreApplication.translate("EditTask", u"/MOVE", None))
        self.chk_fat.setText(QCoreApplication.translate("EditTask", u"/FAT", None))
        self.chk_copy.setText(QCoreApplication.translate("EditTask", u"/COPY:", None))
        self.chk_lev.setText(QCoreApplication.translate("EditTask", u"/LEV:", None))
        self.txt_lev.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_xo.setText(QCoreApplication.translate("EditTask", u"/XO", None))
        self.chk_v.setText(QCoreApplication.translate("EditTask", u"/V", None))
        self.chk_tbd.setText(QCoreApplication.translate("EditTask", u"/TBD", None))
        self.chk_np.setText(QCoreApplication.translate("EditTask", u"/NP", None))
        self.chk_z.setText(QCoreApplication.translate("EditTask", u"/Z", None))
        self.chk_e.setText(QCoreApplication.translate("EditTask", u"/E", None))
        self.txt_r.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_r.setText(QCoreApplication.translate("EditTask", u"/R:", None))
        self.txt_w.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_w.setText(QCoreApplication.translate("EditTask", u"/W:", None))
        self.chk_fft.setText(QCoreApplication.translate("EditTask", u"/FFT", None))
        self.label_5.setText(QCoreApplication.translate("EditTask", u"CopyCommand", None))
        self.btnOK.setText(QCoreApplication.translate("EditTask", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("EditTask", u"Cancel", None))
    # retranslateUi

