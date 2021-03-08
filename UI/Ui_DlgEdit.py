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
        EditTask.resize(698, 594)
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
        self.grpOptions.setMinimumSize(QSize(680, 200))
        self.gridLayout = QGridLayout(self.grpOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chk_s = QCheckBox(self.grpOptions)
        self.chk_s.setObjectName(u"chk_s")

        self.gridLayout.addWidget(self.chk_s, 0, 0, 1, 1)

        self.chk_sec = QCheckBox(self.grpOptions)
        self.chk_sec.setObjectName(u"chk_sec")

        self.gridLayout.addWidget(self.chk_sec, 0, 1, 1, 1)

        self.chk_copyall = QCheckBox(self.grpOptions)
        self.chk_copyall.setObjectName(u"chk_copyall")

        self.gridLayout.addWidget(self.chk_copyall, 0, 2, 1, 1)

        self.chk_create = QCheckBox(self.grpOptions)
        self.chk_create.setObjectName(u"chk_create")

        self.gridLayout.addWidget(self.chk_create, 0, 3, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.chk_e = QCheckBox(self.grpOptions)
        self.chk_e.setObjectName(u"chk_e")

        self.horizontalLayout_18.addWidget(self.chk_e)

        self.horizontalSpacer_8 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_18, 0, 4, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.chk_max = QCheckBox(self.grpOptions)
        self.chk_max.setObjectName(u"chk_max")

        self.horizontalLayout_13.addWidget(self.chk_max)

        self.txt_max = QLineEdit(self.grpOptions)
        self.txt_max.setObjectName(u"txt_max")
        self.txt_max.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_13.addWidget(self.txt_max)


        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 5, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.chk_maxlad = QCheckBox(self.grpOptions)
        self.chk_maxlad.setObjectName(u"chk_maxlad")

        self.horizontalLayout_14.addWidget(self.chk_maxlad)

        self.txt_maxlad = QLineEdit(self.grpOptions)
        self.txt_maxlad.setObjectName(u"txt_maxlad")
        self.txt_maxlad.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_14.addWidget(self.txt_maxlad)


        self.gridLayout.addLayout(self.horizontalLayout_14, 0, 6, 1, 1)

        self.chk_v = QCheckBox(self.grpOptions)
        self.chk_v.setObjectName(u"chk_v")

        self.gridLayout.addWidget(self.chk_v, 1, 0, 1, 1)

        self.chk_mov = QCheckBox(self.grpOptions)
        self.chk_mov.setObjectName(u"chk_mov")

        self.gridLayout.addWidget(self.chk_mov, 1, 1, 1, 1)

        self.chk_nocopy = QCheckBox(self.grpOptions)
        self.chk_nocopy.setObjectName(u"chk_nocopy")

        self.gridLayout.addWidget(self.chk_nocopy, 1, 2, 1, 1)

        self.chk_purge = QCheckBox(self.grpOptions)
        self.chk_purge.setObjectName(u"chk_purge")

        self.gridLayout.addWidget(self.chk_purge, 1, 3, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.chk_fft = QCheckBox(self.grpOptions)
        self.chk_fft.setObjectName(u"chk_fft")

        self.horizontalLayout_17.addWidget(self.chk_fft)

        self.horizontalSpacer_9 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_17, 1, 4, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.chk_min = QCheckBox(self.grpOptions)
        self.chk_min.setObjectName(u"chk_min")

        self.horizontalLayout_12.addWidget(self.chk_min)

        self.txt_min = QLineEdit(self.grpOptions)
        self.txt_min.setObjectName(u"txt_min")
        self.txt_min.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_12.addWidget(self.txt_min)


        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 5, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.chk_lev = QCheckBox(self.grpOptions)
        self.chk_lev.setObjectName(u"chk_lev")

        self.horizontalLayout_15.addWidget(self.chk_lev)

        self.txt_lev = QLineEdit(self.grpOptions)
        self.txt_lev.setObjectName(u"txt_lev")
        self.txt_lev.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_15.addWidget(self.txt_lev)


        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 6, 1, 1)

        self.chk_m = QCheckBox(self.grpOptions)
        self.chk_m.setObjectName(u"chk_m")

        self.gridLayout.addWidget(self.chk_m, 2, 0, 1, 1)

        self.chk_a = QCheckBox(self.grpOptions)
        self.chk_a.setObjectName(u"chk_a")

        self.gridLayout.addWidget(self.chk_a, 2, 1, 1, 1)

        self.chk_mir = QCheckBox(self.grpOptions)
        self.chk_mir.setObjectName(u"chk_mir")

        self.gridLayout.addWidget(self.chk_mir, 2, 2, 1, 1)

        self.chk_move = QCheckBox(self.grpOptions)
        self.chk_move.setObjectName(u"chk_move")

        self.gridLayout.addWidget(self.chk_move, 2, 3, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.chk_j = QCheckBox(self.grpOptions)
        self.chk_j.setObjectName(u"chk_j")

        self.horizontalLayout_16.addWidget(self.chk_j)

        self.horizontalSpacer_10 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_16, 2, 4, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.chk_maxage = QCheckBox(self.grpOptions)
        self.chk_maxage.setObjectName(u"chk_maxage")

        self.horizontalLayout_11.addWidget(self.chk_maxage)

        self.txt_maxage = QLineEdit(self.grpOptions)
        self.txt_maxage.setObjectName(u"txt_maxage")
        self.txt_maxage.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_11.addWidget(self.txt_maxage)


        self.gridLayout.addLayout(self.horizontalLayout_11, 2, 5, 1, 1)

        self.chk_xo = QCheckBox(self.grpOptions)
        self.chk_xo.setObjectName(u"chk_xo")

        self.gridLayout.addWidget(self.chk_xo, 3, 0, 1, 1)

        self.chk_b = QCheckBox(self.grpOptions)
        self.chk_b.setObjectName(u"chk_b")

        self.gridLayout.addWidget(self.chk_b, 3, 1, 1, 1)

        self.chk_zb = QCheckBox(self.grpOptions)
        self.chk_zb.setObjectName(u"chk_zb")

        self.gridLayout.addWidget(self.chk_zb, 3, 2, 1, 1)

        self.chk_fat = QCheckBox(self.grpOptions)
        self.chk_fat.setObjectName(u"chk_fat")

        self.gridLayout.addWidget(self.chk_fat, 3, 3, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.chk_r = QCheckBox(self.grpOptions)
        self.chk_r.setObjectName(u"chk_r")

        self.horizontalLayout_6.addWidget(self.chk_r)

        self.txt_r = QLineEdit(self.grpOptions)
        self.txt_r.setObjectName(u"txt_r")
        self.txt_r.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.txt_r)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 4, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.chk_minage = QCheckBox(self.grpOptions)
        self.chk_minage.setObjectName(u"chk_minage")

        self.horizontalLayout_8.addWidget(self.chk_minage)

        self.txt_minage = QLineEdit(self.grpOptions)
        self.txt_minage.setObjectName(u"txt_minage")
        self.txt_minage.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_8.addWidget(self.txt_minage)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 5, 1, 1)

        self.chk_tbd = QCheckBox(self.grpOptions)
        self.chk_tbd.setObjectName(u"chk_tbd")

        self.gridLayout.addWidget(self.chk_tbd, 4, 0, 1, 1)

        self.chk_z = QCheckBox(self.grpOptions)
        self.chk_z.setObjectName(u"chk_z")

        self.gridLayout.addWidget(self.chk_z, 4, 1, 1, 1)

        self.chk_np = QCheckBox(self.grpOptions)
        self.chk_np.setObjectName(u"chk_np")

        self.gridLayout.addWidget(self.chk_np, 4, 2, 1, 1)

        self.chk_copy = QCheckBox(self.grpOptions)
        self.chk_copy.setObjectName(u"chk_copy")

        self.gridLayout.addWidget(self.chk_copy, 4, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.chk_w = QCheckBox(self.grpOptions)
        self.chk_w.setObjectName(u"chk_w")

        self.horizontalLayout_7.addWidget(self.chk_w)

        self.txt_w = QLineEdit(self.grpOptions)
        self.txt_w.setObjectName(u"txt_w")
        self.txt_w.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.txt_w)


        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 4, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.chk_minlad = QCheckBox(self.grpOptions)
        self.chk_minlad.setObjectName(u"chk_minlad")

        self.horizontalLayout_10.addWidget(self.chk_minlad)

        self.txt_minlad = QLineEdit(self.grpOptions)
        self.txt_minlad.setObjectName(u"txt_minlad")
        self.txt_minlad.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_10.addWidget(self.txt_minlad)


        self.gridLayout.addLayout(self.horizontalLayout_10, 4, 5, 1, 1)

        self.gridLayout.setColumnMinimumWidth(5, 20)
        self.gridLayout.setColumnMinimumWidth(6, 10)

        self.verticalLayout.addWidget(self.grpOptions)

        self.label_5 = QLabel(EditTask)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.txtCmd = QTextEdit(EditTask)
        self.txtCmd.setObjectName(u"txtCmd")
        self.txtCmd.setReadOnly(True)

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
        self.chk_sec.setText(QCoreApplication.translate("EditTask", u"/SEC", None))
        self.chk_copyall.setText(QCoreApplication.translate("EditTask", u"/COPYALL", None))
        self.chk_create.setText(QCoreApplication.translate("EditTask", u"/CREATE", None))
        self.chk_e.setText(QCoreApplication.translate("EditTask", u"/E", None))
        self.chk_max.setText(QCoreApplication.translate("EditTask", u"/MAX:", None))
        self.txt_max.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_maxlad.setText(QCoreApplication.translate("EditTask", u"/MAXLAD:", None))
        self.txt_maxlad.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_v.setText(QCoreApplication.translate("EditTask", u"/V", None))
        self.chk_mov.setText(QCoreApplication.translate("EditTask", u"/MOV", None))
        self.chk_nocopy.setText(QCoreApplication.translate("EditTask", u"/NOCOPY", None))
        self.chk_purge.setText(QCoreApplication.translate("EditTask", u"/PURGE", None))
        self.chk_fft.setText(QCoreApplication.translate("EditTask", u"/FFT", None))
        self.chk_min.setText(QCoreApplication.translate("EditTask", u"/MIN:", None))
        self.txt_min.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_lev.setText(QCoreApplication.translate("EditTask", u"/LEV:", None))
        self.txt_lev.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_m.setText(QCoreApplication.translate("EditTask", u"/M", None))
        self.chk_a.setText(QCoreApplication.translate("EditTask", u"/A", None))
        self.chk_mir.setText(QCoreApplication.translate("EditTask", u"/MIR", None))
        self.chk_move.setText(QCoreApplication.translate("EditTask", u"/MOVE", None))
        self.chk_j.setText(QCoreApplication.translate("EditTask", u"/J", None))
        self.chk_maxage.setText(QCoreApplication.translate("EditTask", u"/MAXAGE:", None))
        self.txt_maxage.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_xo.setText(QCoreApplication.translate("EditTask", u"/XO", None))
        self.chk_b.setText(QCoreApplication.translate("EditTask", u"/B", None))
        self.chk_zb.setText(QCoreApplication.translate("EditTask", u"/ZB", None))
        self.chk_fat.setText(QCoreApplication.translate("EditTask", u"/FAT", None))
        self.chk_r.setText(QCoreApplication.translate("EditTask", u"/R:", None))
        self.txt_r.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_minage.setText(QCoreApplication.translate("EditTask", u"/MINAGE:", None))
        self.txt_minage.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_tbd.setText(QCoreApplication.translate("EditTask", u"/TBD", None))
        self.chk_z.setText(QCoreApplication.translate("EditTask", u"/Z", None))
        self.chk_np.setText(QCoreApplication.translate("EditTask", u"/NP", None))
        self.chk_copy.setText(QCoreApplication.translate("EditTask", u"/COPY:", None))
        self.chk_w.setText(QCoreApplication.translate("EditTask", u"/W:", None))
        self.txt_w.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.chk_minlad.setText(QCoreApplication.translate("EditTask", u"/MINLAD:", None))
        self.txt_minlad.setText(QCoreApplication.translate("EditTask", u"1", None))
        self.label_5.setText(QCoreApplication.translate("EditTask", u"CopyCommand", None))
        self.btnOK.setText(QCoreApplication.translate("EditTask", u"OK", None))
        self.btnCancel.setText(QCoreApplication.translate("EditTask", u"Cancel", None))
    # retranslateUi

