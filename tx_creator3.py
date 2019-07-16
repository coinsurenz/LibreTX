# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'txcreator4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from ecdsa_functions import *
from address_functions import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap



import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1618, 862)
        Dialog.setMinimumSize(QtCore.QSize(1618, 862))
        Dialog.setMaximumSize(QtCore.QSize(1618, 862))
        Dialog.setProperty("script_pubkey", "")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pubouts_label = QtWidgets.QLabel(Dialog)
        self.pubouts_label.setMinimumSize(QtCore.QSize(100, 0))
        self.pubouts_label.setObjectName("pubouts_label")
        self.gridLayout.addWidget(self.pubouts_label, 16, 3, 1, 1)
        self.scriptout4_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout4_box.setObjectName("scriptout4_box")
        self.gridLayout.addWidget(self.scriptout4_box, 24, 3, 1, 1)
        self.scriptout6_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout6_box.setObjectName("scriptout6_box")
        self.gridLayout.addWidget(self.scriptout6_box, 27, 3, 1, 1)
        self.signed_label = QtWidgets.QLabel(Dialog)
        self.signed_label.setObjectName("signed_label")
        self.gridLayout.addWidget(self.signed_label, 20, 6, 1, 1)
        self.signtx_label = QtWidgets.QLabel(Dialog)
        self.signtx_label.setObjectName("signtx_label")
        self.gridLayout.addWidget(self.signtx_label, 24, 6, 1, 1)
        self.txin5_box = QtWidgets.QLineEdit(Dialog)
        self.txin5_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin5_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin5_box.setObjectName("txin5_box")
        self.gridLayout.addWidget(self.txin5_box, 10, 3, 1, 1)
        self.sequence_label = QtWidgets.QLabel(Dialog)
        self.sequence_label.setObjectName("sequence_label")
        self.gridLayout.addWidget(self.sequence_label, 16, 0, 1, 1)
        self.sequence2_box = QtWidgets.QLineEdit(Dialog)
        self.sequence2_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence2_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence2_box.setObjectName("sequence2_box")
        self.gridLayout.addWidget(self.sequence2_box, 20, 0, 1, 1)
        self.privkey4_box = QtWidgets.QLineEdit(Dialog)
        self.privkey4_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey4_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey4_box.setObjectName("privkey4_box")
        self.gridLayout.addWidget(self.privkey4_box, 24, 4, 1, 1)
        self.txinamount_box1 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box1.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box1.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box1.setObjectName("txinamount_box1")
        self.gridLayout.addWidget(self.txinamount_box1, 6, 0, 1, 1)
        self.txinamount_box2 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box2.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box2.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box2.setObjectName("txinamount_box2")
        self.gridLayout.addWidget(self.txinamount_box2, 7, 0, 1, 1)
        self.txinamount_box5 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box5.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box5.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box5.setObjectName("txinamount_box5")
        self.gridLayout.addWidget(self.txinamount_box5, 10, 0, 1, 1)

        # LEAVE THIS- REINSTATE LATER
        # self.walletstyle_combobox = QtWidgets.QComboBox(Dialog)
        # self.walletstyle_combobox.setObjectName("walletstyle_combobox")
        # self.gridLayout.addWidget(self.walletstyle_combobox, 8, 5, 1, 1)
        self.privkey_comboBox = QtWidgets.QComboBox(Dialog)
        self.privkey_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.privkey_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.privkey_comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.privkey_comboBox, 16, 5, 1, 1)
        self.txtype_combobox_1 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_1.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_1.setObjectName("txtype_combobox_1")
        self.gridLayout.addWidget(self.txtype_combobox_1, 6, 1, 1, 1)
        self.privkey_label = QtWidgets.QLabel(Dialog)
        self.privkey_label.setObjectName("privkey_label")
        self.gridLayout.addWidget(self.privkey_label, 16, 4, 1, 1)
        self.txinamount_box4 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box4.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box4.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box4.setObjectName("txinamount_box4")
        self.gridLayout.addWidget(self.txinamount_box4, 9, 0, 1, 1)
        self.sequence1_box = QtWidgets.QLineEdit(Dialog)
        self.sequence1_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence1_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence1_box.setObjectName("sequence1_box")
        self.gridLayout.addWidget(self.sequence1_box, 17, 0, 1, 1)
        self.txin2_box = QtWidgets.QLineEdit(Dialog)
        self.txin2_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin2_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin2_box.setObjectName("txin2_box")
        self.gridLayout.addWidget(self.txin2_box, 7, 3, 1, 1)
        self.privkey3_box = QtWidgets.QLineEdit(Dialog)
        self.privkey3_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey3_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey3_box.setObjectName("privkey3_box")
        self.gridLayout.addWidget(self.privkey3_box, 22, 4, 1, 1)
        self.inputindex_label = QtWidgets.QLabel(Dialog)
        self.inputindex_label.setMinimumSize(QtCore.QSize(0, 20))
        self.inputindex_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.inputindex_label.setObjectName("inputindex_label")
        self.gridLayout.addWidget(self.inputindex_label, 5, 2, 1, 1)
        self.inputindex3_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex3_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex3_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex3_box.setObjectName("inputindex3_box")
        self.gridLayout.addWidget(self.inputindex3_box, 8, 2, 1, 1)
        self.nlocktime_box = QtWidgets.QLineEdit(Dialog)
        self.nlocktime_box.setMinimumSize(QtCore.QSize(100, 0))
        self.nlocktime_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.nlocktime_box.setObjectName("nlocktime_box")
        self.gridLayout.addWidget(self.nlocktime_box, 20, 5, 1, 1)
        self.privkey1_box = QtWidgets.QLineEdit(Dialog)
        self.privkey1_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey1_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey1_box.setObjectName("privkey1_box")
        self.gridLayout.addWidget(self.privkey1_box, 17, 4, 1, 1)
        self.txtype_combobox_2 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_2.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_2.setObjectName("txtype_combobox_2")
        self.gridLayout.addWidget(self.txtype_combobox_2, 7, 1, 1, 1)
        self.Title_label = QtWidgets.QLabel(Dialog)
        self.Title_label.setMinimumSize(QtCore.QSize(20, 0))
        self.Title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        self.gridLayout.addWidget(self.Title_label, 0, 4, 1, 1)
        self.hashtype_box = QtWidgets.QLineEdit(Dialog)
        self.hashtype_box.setMinimumSize(QtCore.QSize(100, 0))
        self.hashtype_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hashtype_box.setObjectName("hashtype_box")
        self.gridLayout.addWidget(self.hashtype_box, 24, 5, 1, 1)
        self.hashtype_label = QtWidgets.QLabel(Dialog)
        self.hashtype_label.setObjectName("hashtype_label")
        self.gridLayout.addWidget(self.hashtype_label, 22, 5, 1, 1)
        self.scriptpub5_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub5_box.setObjectName("scriptpub5_box")
        self.gridLayout.addWidget(self.scriptpub5_box, 10, 4, 1, 1)
## LEAVE THIS- WILL BE IMPLIMENTED
        # self.emulatewallet_label = QtWidgets.QLabel(Dialog)
        # self.emulatewallet_label.setObjectName("emulatewallet_label")
        # self.gridLayout.addWidget(self.emulatewallet_label, 7, 5, 1, 1)
        
        # self.txtype_comboBox = QtWidgets.QComboBox(Dialog)
        # self.txtype_comboBox.setMinimumSize(QtCore.QSize(90, 0))
        # self.txtype_comboBox.setMaximumSize(QtCore.QSize(90, 16777215))
        # self.txtype_comboBox.setObjectName("txtype_comboBox")
        # self.gridLayout.addWidget(self.txtype_comboBox, 27, 1, 1, 1)

        self.multisig_spinbox = QtWidgets.QSpinBox(Dialog)
        # self.multisig_spinbox.setMaximumSize(QtCore.QSize(90, 16777215))
        # self.multisig_spinbox.setMinimum(1)
        self.multisig_spinbox.setMinimumSize(QtCore.QSize(90, 0))
        self.multisig_spinbox.setMaximumSize(QtCore.QSize(90, 16777215))
        self.multisig_spinbox.setProperty("total_multig_str", "")
        self.multisig_spinbox.setObjectName("multisig_spinbox")
        self.gridLayout.addWidget(self.multisig_spinbox, 27, 1, 1, 1)


        self.education_checkbox = QtWidgets.QCheckBox(Dialog)
        self.education_checkbox.setObjectName("education_checkbox")
        self.gridLayout.addWidget(self.education_checkbox, 24, 1, 1, 1)
        self.numins_label = QtWidgets.QLabel(Dialog)
        self.numins_label.setObjectName("numins_label")
        self.gridLayout.addWidget(self.numins_label, 16, 1, 1, 1)
        self.privkey6_box = QtWidgets.QLineEdit(Dialog)
        self.privkey6_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey6_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey6_box.setObjectName("privkey6_box")
        self.gridLayout.addWidget(self.privkey6_box, 27, 4, 1, 1)
        self.txinamount_box6 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box6.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box6.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box6.setObjectName("txinamount_box6")
        self.gridLayout.addWidget(self.txinamount_box6, 11, 0, 1, 1)
        self.numouts_label = QtWidgets.QLabel(Dialog)
        self.numouts_label.setObjectName("numouts_label")
        self.gridLayout.addWidget(self.numouts_label, 20, 1, 1, 1)
        self.privkey5_box = QtWidgets.QLineEdit(Dialog)
        self.privkey5_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey5_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey5_box.setObjectName("privkey5_box")
        self.gridLayout.addWidget(self.privkey5_box, 25, 4, 1, 1)
        self.inputindex1_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex1_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex1_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex1_box.setObjectName("inputindex1_box")
        self.gridLayout.addWidget(self.inputindex1_box, 6, 2, 1, 1)
        self.scriptpub2_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub2_box.setObjectName("scriptpub3_box")
        self.gridLayout.addWidget(self.scriptpub2_box, 7, 4, 1, 1)
        self.currentblock_label = QtWidgets.QLabel(Dialog)
        self.currentblock_label.setObjectName("currentblock_label")
        self.gridLayout.addWidget(self.currentblock_label, 9, 5, 1, 1)
        self.scriptpub1_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub1_box.setObjectName("scriptpub2_box")
        self.gridLayout.addWidget(self.scriptpub1_box, 6, 4, 1, 1)
        self.privkey2_box = QtWidgets.QLineEdit(Dialog)
        self.privkey2_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey2_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey2_box.setObjectName("privkey2_box")
        self.gridLayout.addWidget(self.privkey2_box, 20, 4, 1, 1)
        self.txtype_combobox_6 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_6.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_6.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_6.setObjectName("txtype_combobox_6")
        self.gridLayout.addWidget(self.txtype_combobox_6, 11, 1, 1, 1)
        self.scriptpub6_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub6_box.setObjectName("scriptpub6_box")
        self.gridLayout.addWidget(self.scriptpub6_box, 11, 4, 1, 1)
        self.inputindex2_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex2_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex2_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex2_box.setObjectName("inputindex2_box")
        self.gridLayout.addWidget(self.inputindex2_box, 7, 2, 1, 1)
        self.sequence3_box = QtWidgets.QLineEdit(Dialog)
        self.sequence3_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence3_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence3_box.setObjectName("sequence3_box")
        self.gridLayout.addWidget(self.sequence3_box, 22, 0, 1, 1)
        self.txtype_combobox_4 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_4.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_4.setObjectName("txtype_combobox_4")
        self.gridLayout.addWidget(self.txtype_combobox_4, 9, 1, 1, 1)
        self.txtype_combobox_5 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_5.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_5.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_5.setObjectName("txtype_combobox_5")
        self.gridLayout.addWidget(self.txtype_combobox_5, 10, 1, 1, 1)
        self.scriptpub3_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub3_box.setObjectName("scriptpub1_box")
        self.gridLayout.addWidget(self.scriptpub3_box, 8, 4, 1, 1)
        self.tx_type1_label = QtWidgets.QLabel(Dialog)
        self.tx_type1_label.setMinimumSize(QtCore.QSize(0, 20))
        self.tx_type1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.tx_type1_label.setObjectName("tx_type1_label")
        self.gridLayout.addWidget(self.tx_type1_label, 5, 1, 1, 1)
        self.txin3_box = QtWidgets.QLineEdit(Dialog)
        self.txin3_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin3_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin3_box.setObjectName("txin3_box")
        self.gridLayout.addWidget(self.txin3_box, 8, 3, 1, 1)
        self.txin6_box = QtWidgets.QLineEdit(Dialog)
        self.txin6_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin6_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin6_box.setObjectName("txin6_box")
        self.gridLayout.addWidget(self.txin6_box, 11, 3, 1, 1)
        self.output_box = QtWidgets.QTextBrowser(Dialog)
        self.output_box.setMinimumSize(QtCore.QSize(1600, 300))
        self.output_box.setMaximumSize(QtCore.QSize(1600, 300))
        self.output_box.setObjectName("output_box")

        out_font = QtGui.QFont()
        out_font.setPointSize(15)
        # out_font.setBold(True)
        # out_font.setWeight(75)
        out_font.setWeight(35)
        self.output_box.setFont(out_font)

        self.gridLayout.addWidget(self.output_box, 33, 0, 4, 13)
        self.scriptout5_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout5_box.setObjectName("scriptout5_box")
        self.gridLayout.addWidget(self.scriptout5_box, 25, 3, 1, 1)
        self.scriptout2_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout2_box.setObjectName("scriptout2_box")
        self.gridLayout.addWidget(self.scriptout2_box, 20, 3, 1, 1)
        self.scriptout3_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout3_box.setObjectName("scriptout3_box")
        self.gridLayout.addWidget(self.scriptout3_box, 22, 3, 1, 1)
        self.sequence5_box = QtWidgets.QLineEdit(Dialog)
        self.sequence5_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence5_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence5_box.setObjectName("sequence5_box")
        self.gridLayout.addWidget(self.sequence5_box, 25, 0, 1, 1)
        self.txinamount_box3 = QtWidgets.QLineEdit(Dialog)
        self.txinamount_box3.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box3.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box3.setObjectName("txinamount_box3")
        self.gridLayout.addWidget(self.txinamount_box3, 8, 0, 1, 1)
        self.txinamounts_label = QtWidgets.QLabel(Dialog)
        self.txinamounts_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txinamounts_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txinamounts_label.setObjectName("txinamounts_label")
        self.gridLayout.addWidget(self.txinamounts_label, 5, 0, 1, 1)
        self.version_box = QtWidgets.QLineEdit(Dialog)
        self.version_box.setMinimumSize(QtCore.QSize(100, 0))
        self.version_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.version_box.setObjectName("version_box")
        self.gridLayout.addWidget(self.version_box, 27, 5, 1, 1)
# LEAVE THIS WILL RE INSTATE
        # self.un_signed_button = QtWidgets.QPushButton(Dialog)
        # self.un_signed_button.setObjectName("pushButton")
        # self.gridLayout.addWidget(self.un_signed_button, 22, 6, 1, 1)
        
        self.txin4_box = QtWidgets.QLineEdit(Dialog)
        self.txin4_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin4_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin4_box.setObjectName("txin4_box")
        self.gridLayout.addWidget(self.txin4_box, 9, 3, 1, 1)
        self.multisig_spin_label = QtWidgets.QLabel(Dialog)
        self.multisig_spin_label.setObjectName("multisig_spin_label")
        self.gridLayout.addWidget(self.multisig_spin_label, 25, 1, 1, 1)
        self.inputindex4_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex4_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex4_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex4_box.setObjectName("inputindex4_box")
        self.gridLayout.addWidget(self.inputindex4_box, 9, 2, 1, 1)
        self.amount4_box = QtWidgets.QLineEdit(Dialog)
        self.amount4_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount4_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount4_box.setObjectName("amount4_box")
        self.gridLayout.addWidget(self.amount4_box, 24, 2, 1, 1)
        self.scriptout1_box = QtWidgets.QLineEdit(Dialog)
        self.scriptout1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout1_box.setObjectName("scriptout1_box")
        self.gridLayout.addWidget(self.scriptout1_box, 17, 3, 1, 1)
        self.outputformat_label = QtWidgets.QLabel(Dialog)
        self.outputformat_label.setMinimumSize(QtCore.QSize(0, 20))
        self.outputformat_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.outputformat_label.setObjectName("outputformat_label")
        self.gridLayout.addWidget(self.outputformat_label, 5, 5, 1, 1)
        self.txins_label = QtWidgets.QLabel(Dialog)
        self.txins_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txins_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txins_label.setObjectName("txins_label")
        self.gridLayout.addWidget(self.txins_label, 5, 3, 1, 1)
        self.currentblock_box = QtWidgets.QLineEdit(Dialog)
        self.currentblock_box.setMinimumSize(QtCore.QSize(100, 0))
        self.currentblock_box.setMaximumSize(QtCore.QSize(100, 20))
        self.currentblock_box.setObjectName("currentblock_box")
        self.gridLayout.addWidget(self.currentblock_box, 10, 5, 1, 1)
        self.inputindex6_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex6_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex6_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex6_box.setObjectName("inputindex6_box")
        self.gridLayout.addWidget(self.inputindex6_box, 11, 2, 1, 1)
        self.privkeyformat_label = QtWidgets.QLabel(Dialog)
        self.privkeyformat_label.setObjectName("privkeyformat_label")
        self.gridLayout.addWidget(self.privkeyformat_label, 16, 6, 1, 1)
        self.nlocktime_label = QtWidgets.QLabel(Dialog)
        self.nlocktime_label.setObjectName("nlocktime_label")
        self.gridLayout.addWidget(self.nlocktime_label, 17, 5, 1, 1)
        self.scriptpubkey_label = QtWidgets.QLabel(Dialog)
        self.scriptpubkey_label.setMinimumSize(QtCore.QSize(0, 20))
        self.scriptpubkey_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.scriptpubkey_label.setObjectName("scriptpubkey_label")
        self.gridLayout.addWidget(self.scriptpubkey_label, 5, 4, 1, 1)
        self.sequence4_box = QtWidgets.QLineEdit(Dialog)
        self.sequence4_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence4_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence4_box.setObjectName("sequence4_box")
        self.gridLayout.addWidget(self.sequence4_box, 24, 0, 1, 1)
        self.sequence6_box = QtWidgets.QLineEdit(Dialog)
        self.sequence6_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence6_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence6_box.setObjectName("sequence6_box")
        self.gridLayout.addWidget(self.sequence6_box, 27, 0, 1, 1)
        self.inputindex5_box = QtWidgets.QLineEdit(Dialog)
        self.inputindex5_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex5_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex5_box.setObjectName("inputindex5_box")
        self.gridLayout.addWidget(self.inputindex5_box, 10, 2, 1, 1)
        self.txtype_combobox_3 = QtWidgets.QComboBox(Dialog)
        self.txtype_combobox_3.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_3.setObjectName("txtype_combobox_3")
        self.gridLayout.addWidget(self.txtype_combobox_3, 8, 1, 1, 1)
        self.amount1_box = QtWidgets.QLineEdit(Dialog)
        self.amount1_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount1_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount1_box.setObjectName("amount1_box")
        self.gridLayout.addWidget(self.amount1_box, 17, 2, 1, 1)
        self.amount6_box = QtWidgets.QLineEdit(Dialog)
        self.amount6_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount6_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount6_box.setObjectName("amount6_box")
        self.gridLayout.addWidget(self.amount6_box, 27, 2, 1, 1)
        self.amounts_label = QtWidgets.QLabel(Dialog)
        self.amounts_label.setObjectName("amounts_label")
        self.gridLayout.addWidget(self.amounts_label, 16, 2, 1, 1)
        self.txin1_box = QtWidgets.QLineEdit(Dialog)
        self.txin1_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin1_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin1_box.setObjectName("txin1_box")
        self.gridLayout.addWidget(self.txin1_box, 6, 3, 1, 1)

        self.signed_button = QtWidgets.QPushButton(Dialog)
        self.signed_button.setObjectName("unsigned_button")
        self.signed_button.setMinimumSize(QtCore.QSize(85, 0))
        self.signed_button.setMaximumSize(QtCore.QSize(85, 16777215))
        self.gridLayout.addWidget(self.signed_button, 25, 6, 1, 1)

        

        self.version_label = QtWidgets.QLabel(Dialog)
        self.version_label.setObjectName("version_label")
        self.gridLayout.addWidget(self.version_label, 25, 5, 1, 1)
        self.scriptpub4_box = QtWidgets.QLineEdit(Dialog)
        self.scriptpub4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub4_box.setObjectName("scriptpub4_box")
        self.gridLayout.addWidget(self.scriptpub4_box, 9, 4, 1, 1)
        self.numins_combo = QtWidgets.QComboBox(Dialog)
        self.numins_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numins_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numins_combo.setObjectName("numins_combo")
        self.gridLayout.addWidget(self.numins_combo, 17, 1, 1, 1)
        self.numouts_combo = QtWidgets.QComboBox(Dialog)
        self.numouts_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numouts_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numouts_combo.setObjectName("numouts_combo")
        self.gridLayout.addWidget(self.numouts_combo, 22, 1, 1, 1)
        self.amount3_box = QtWidgets.QLineEdit(Dialog)
        self.amount3_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount3_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount3_box.setObjectName("amount3_box")
        self.gridLayout.addWidget(self.amount3_box, 22, 2, 1, 1)
        self.amount5_box = QtWidgets.QLineEdit(Dialog)
        self.amount5_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount5_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount5_box.setObjectName("amount5_box")
        self.gridLayout.addWidget(self.amount5_box, 25, 2, 1, 1)
        self.amount2_box = QtWidgets.QLineEdit(Dialog)
        self.amount2_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount2_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount2_box.setObjectName("amount2_box")
        self.gridLayout.addWidget(self.amount2_box, 20, 2, 1, 1)
        self.outputformat_combobox = QtWidgets.QComboBox(Dialog)
        self.outputformat_combobox.setMinimumSize(QtCore.QSize(0, 20))
        self.outputformat_combobox.setMaximumSize(QtCore.QSize(100, 20))
        self.outputformat_combobox.setProperty("bitcoin_address", "")
        self.outputformat_combobox.setObjectName("outputformat_combobox")
        self.gridLayout.addWidget(self.outputformat_combobox, 6, 5, 1, 1)
        # self.locktime_checkBox = QtWidgets.QCheckBox(Dialog)
        # self.locktime_checkBox.setObjectName("checkBox")
        # self.gridLayout.addWidget(self.locktime_checkBox, 11, 5, 1, 1)

        # self.txtype_comboBox = QtWidgets.QComboBox(Dialog)
        # self.txtype_comboBox.setMinimumSize(QtCore.QSize(90, 0))
        # self.txtype_comboBox.setMaximumSize(QtCore.QSize(90, 16777215))
        # self.txtype_comboBox.setObjectName("txtype_comboBox")
        # self.gridLayout.addWidget(self.txtype_comboBox, 27, 1, 1, 1)


        self.locktime_button = QtWidgets.QPushButton(Dialog)
        self.locktime_button.setMinimumSize(QtCore.QSize(0, 20))
        self.locktime_button.setMaximumSize(QtCore.QSize(100, 20))

        self.locktime_button.setObjectName("Convert Locktime")
        self.gridLayout.addWidget(self.locktime_button, 11, 5, 1, 1)

# delete threse?
        self.txtype_combobox_1.activated.connect(lambda: tx_select_func(1))
        self.txtype_combobox_2.activated.connect(lambda: tx_select_func(2))
        self.txtype_combobox_3.activated.connect(lambda: tx_select_func(3))
        self.txtype_combobox_4.activated.connect(lambda: tx_select_func(4))
        self.txtype_combobox_5.activated.connect(lambda: tx_select_func(5))
        self.txtype_combobox_6.activated.connect(lambda: tx_select_func(6))

        self.numins_combo.activated.connect(lambda: ins_activate(self.numins_combo.currentIndex()+1))
        self.numouts_combo.activated.connect(lambda: outs_activate(self.numouts_combo.currentIndex()+1))

        # slotLambda = lambda: self.indexChanged_lambda(self.myObject)
        # self.comboBox.currentIndexChanged.connect(slotLambda)

        self.outputformat_combobox.addItems(['0','1'])


        self.sequence1_box.setText('fdffffff')
        self.inputindex1_box.setDisabled(True)
        # self.inputindex1_box.setText('01000000')
        # self.scriptpub1_box.setText('1976a9142c8facb21175f940311a5192c44d2ea070d07d4288ac')
        # self.scriptout1_box.setText('34GwNmcLrMsR5CCdgmte8Jm2SzAcc2yJY4')
        # self.txin1_box.setText('df85b199e88aa4681932ab88bbfa52059a8b7ad46fdfa75ce8b03b7e859f94ab')
        # self.privkey1_box.setText('cRpPQiEio6aB65UZN3rXCwvxq9tFuEHHDUwEmyJb6arke5CNQyh3')
        # self.amount1_box.setText('0.0009')

        self.txinamount_box2.setDisabled(True)
        self.inputindex2_box.setDisabled(True)
        self.scriptpub2_box.setDisabled(True)
        self.scriptout2_box.setDisabled(True)
        self.txin2_box.setDisabled(True)
        self.privkey2_box.setDisabled(True)
        self.amount2_box.setDisabled(True)
        self.sequence2_box.setDisabled(True)

        self.txinamount_box3.setDisabled(True)
        self.inputindex3_box.setDisabled(True)
        self.scriptpub3_box.setDisabled(True)
        self.scriptout3_box.setDisabled(True)
        self.txin3_box.setDisabled(True)
        self.privkey3_box.setDisabled(True)
        self.amount3_box.setDisabled(True)
        self.sequence3_box.setDisabled(True)

        self.txinamount_box3.setDisabled(True)
        self.inputindex3_box.setDisabled(True)
        self.scriptpub3_box.setDisabled(True)
        self.scriptout3_box.setDisabled(True)
        self.txin3_box.setDisabled(True)
        self.privkey3_box.setDisabled(True)
        self.amount3_box.setDisabled(True)
        self.sequence3_box.setDisabled(True)

        self.txinamount_box4.setDisabled(True)
        self.inputindex4_box.setDisabled(True)
        self.scriptpub4_box.setDisabled(True)
        self.scriptout4_box.setDisabled(True)
        self.txin4_box.setDisabled(True)
        self.privkey4_box.setDisabled(True)
        self.amount4_box.setDisabled(True)
        self.sequence4_box.setDisabled(True)

        self.txinamount_box5.setDisabled(True)
        self.inputindex5_box.setDisabled(True)
        self.scriptpub5_box.setDisabled(True)
        self.scriptout5_box.setDisabled(True)
        self.txin5_box.setDisabled(True)
        self.privkey5_box.setDisabled(True)
        self.amount5_box.setDisabled(True)
        self.sequence5_box.setDisabled(True)

        self.txinamount_box6.setDisabled(True)
        self.inputindex6_box.setDisabled(True)
        self.scriptpub6_box.setDisabled(True)
        self.scriptout6_box.setDisabled(True)
        self.txin6_box.setDisabled(True)
        self.privkey6_box.setDisabled(True)
        self.amount6_box.setDisabled(True)
        self.sequence6_box.setDisabled(True)


        self.nlocktime_box.setText('28f11700')
        self.numins_combo.addItems(['1','2','3','4','5','6'])
        self.numouts_combo.addItems(['1','2','3','4','5','6'])
        # self.signed_button.clicked.connect(join_segwit)
        self.signed_button.clicked.connect(ok_button)
        self.hashtype_box.setText('01000000')
        # self.txtype_comboBox.addItems(['0','1','2','3'])
        self.txtype_combobox_1.addItems(['0','1','2','3','4','5','6','7'])
        self.txtype_combobox_2.addItems(['0','1','2','3','4','5','6','7'])
        self.txtype_combobox_3.addItems(['0','1','2','3','4','5','6','7'])
        self.txtype_combobox_4.addItems(['0','1','2','3','4','5','6','7'])
        self.txtype_combobox_5.addItems(['0','1','2','3','4','5','6','7'])
        self.txtype_combobox_6.addItems(['0','1','2','3','4','5','6','7'])

        self.locktime_button.clicked.connect(int_to_nlocktime)

        

        self.inputindex1_box.setText('00000000')
        self.scriptpub1_box.setText('1976a9141e496e03f7c17ac4177bff2125e2a199f4b5018688ac')
        self.scriptout1_box.setText('n2ZzdQWjqP8tFizWG7vn8uja6bf2BkhZkn')
        self.txin1_box.setText('235ddc5a16629c3c7c26be35bb4f5eeba600b4d9680f5825c997e32766ee0b52')
        self.privkey1_box.setText('cUhdxeW6Fd9dNYNWGeisBo1qvmeZi4Cg8cRzN937QmHC8Zsay9or')
        # self.privkey2_box.setText('cTwV7qAiUNuPc5eACrtoeBHEvEdKzCm2Fa83vnEjoGhogbAp2Q2e')
        # self.privkey3_box.setText('cW78VE4LWsXLM39qcMjNqwu5f1omKambLizQr3ivMtLR9ai9TH2E')
        self.amount1_box.setText('0.000007')
        self.version_box.setText('02000000')

        # self.inputindex2_box.setText('01000000')
        # self.scriptpub2_box.setText('1976a9143742b596c54cef6a80b5b2da26352f7ffd2766db88ac')
        # self.scriptout2_box.setText('1976a91468725f2a7f81b435e40359e73e1b59f1ab86002188ac')
        # self.txin2_box.setText('049dc7cc904fdc231c413832357b185fd9329c807dd1209174ce01d752015c84')
        # self.privkey2_box.setText('cV64LmYBcfFvQ7JL4NvHfarDrUYv1Xmd4fFKT9zMNNfpFpytv8bA')
        # self.amount2_box.setText('0.0009')
        # self.sequence2_box.setText('ffffffff')

        self.privkey_comboBox.addItems(['0','1','2'])



        # locktime_checkBox
        # nlocktime_box
        # currentblock_box

        # self.inputindex3_box.setText('01000000')
        # self.scriptpub3_box.setText('1976a914e09cc5a1e04d644866588bc40b5b9c4343bfe2f488ac')
        # self.scriptout3_box.setText('1976a91487864ec3cf617d290867e4263e706f6d58179f0688ac')
        # self.txin3_box.setText('52d9b2266093ea87cc8353f7c472e0ae40a748eb649f511c0854da2a1df1afdf')
        # self.privkey3_box.setText('cN1ydyzThBLuREaK1wF56XkHrAE4yQ3TAvgSc2TyExJiN5RWHcuZ')
        # self.amount3_box.setText('0.0009')
        # self.sequence3_box.setText('feffffff')


        # self.inputindex4_box.setText('01000000')
        # self.scriptpub4_box.setText('1976a9147d9003d8d2062f357c9edf785b27133a333c5b8d88ac')
        # self.txin4_box.setText('2a383f365f5f01b23894e2cde0546e322f1313666a329e6408a06e8a4fc85743')
        # self.privkey4_box.setText('cUVJbdCRQJbPrDDxtGw1AgFj9wx9Y496e2pNUyGsFXKJe2qJmCyr')
        # self.amount4_box.setText('0.0009')
        # self.sequence4_box.setText('feffffff')

        # self.inputindex5_box.setText('01000000')
        # self.scriptpub5_box.setText('1976a914c277d4d48190cbadd612d8ec2748a1b1e76a24e388ac')
        # self.txin5_box.setText('d937e6015733e099a1608f9c484dfbb2375e93f6a9030ace75943e32e04a4c02')
        # self.privkey5_box.setText('cPvBSC4m83rSXjKNBai2KLuGJ8CEbhRkyctFdwccj5cEVV5Y5Re6')
        # self.amount5_box.setText('0.0009')
        # self.sequence5_box.setText('feffffff')


        # self.inputindex6_box.setText('01000000')
        # self.scriptpub6_box.setText('1976a914175e2a476add9cf2da213ec5dbf137da8f636ebc88ac')
        # self.txin6_box.setText('04f2937f3f127686bad5327b4ec8bd6165b1c0ba1ac6bcb04ca1c815558251db')
        # self.privkey6_box.setText('cPUvx5vt86Egp6gCFm4k52GBWNZ6nmC8yN3CVvTPdadSbyaDA6BN')
        # self.amount6_box.setText('0.0007')
        # self.sequence6_box.setText('feffffff')

        
        
        # self.version_box.setText('02000000')
        
        
        
        # self.scriptout4_box.setText('1976a9144263f9e8b970d5ef7ff914b119f13bb55e8c0cfc88ac')

        # self.scriptout5_box.setText('1976a9146417a04bffd27e19b7dd0d6a349599bbfd46e57f88ac')

        # self.scriptout6_box.setText('1976a914d848cfe3f6a7db4f3e14f97ef2d0519029f801da88ac')


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tx Creator Tool"))
        self.pubouts_label.setText(_translate("Dialog", "Script pub outs"))
        self.signed_button.setText(_translate("Dialog", "Create TX"))
        self.signtx_label.setText(_translate("Dialog", "Sign Tx"))
        self.sequence_label.setText(_translate("Dialog", "Sequence"))
        self.privkey_label.setText(_translate("Dialog", "Priv Keys"))
        self.inputindex_label.setText(_translate("Dialog", "Input Index"))
        self.Title_label.setText(_translate("Dialog", "Transaction Creator Tool"))
        self.hashtype_label.setText(_translate("Dialog", "Hash type"))
## LEAVE THIS- WILL BE IMPLIMENTED
        # self.emulatewallet_label.setText(_translate("Dialog", "Emulate Wallet"))
        self.education_checkbox.setText(_translate("Dialog", "Education Mode"))
        self.numins_label.setText(_translate("Dialog", "Num Ins"))
        self.numouts_label.setText(_translate("Dialog", "Num Outs"))
        self.currentblock_label.setText(_translate("Dialog", "Current Block Height"))
        self.tx_type1_label.setText(_translate("Dialog", "Tx Type"))
        self.txinamounts_label.setText(_translate("Dialog", "Txin Amounts"))
        
        # self.un_signed_button.setText(_translate("Dialog", "impliment"))  #unsigned button

        self.multisig_spin_label.setText(_translate("Dialog", "Multisig Total"))
        self.outputformat_label.setText(_translate("Dialog", "Output Address Format"))
        self.txins_label.setText(_translate("Dialog", "Txins TXID\'s"))
        self.privkeyformat_label.setText(_translate("Dialog", "Priv Key Format"))
        self.nlocktime_label.setText(_translate("Dialog", "N-locktime"))
        self.scriptpubkey_label.setText(_translate("Dialog", "Script pubkeys"))
        self.amounts_label.setText(_translate("Dialog", "Amounts"))
        # self.signed_button.setText(_translate("Dialog", "Create Signed"))
        self.version_label.setText(_translate("Dialog", "Version"))
        self.locktime_button.setText(_translate("Dialog", "Convert L-time"))

        self.txtype_combobox_1.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_1.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_1.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_1.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_1.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_1.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_1.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_1.setItemText(7, _translate("Txcreator", "P2WSH multisig"))
        
        self.txtype_combobox_2.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_2.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_2.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_2.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_2.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_2.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_2.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_2.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_3.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_3.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_3.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_3.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_3.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_3.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_3.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_3.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_4.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_4.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_4.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_4.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_4.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_4.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_4.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_4.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_5.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_5.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_5.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_5.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_5.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_5.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_5.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_5.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_6.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_6.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_6.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_6.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_6.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_6.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_6.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_6.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.outputformat_combobox.setItemText(0, _translate("Txcreator", "Scriptpub"))
        self.outputformat_combobox.setItemText(1, _translate("Txcreator", "Address"))

        self.privkey_comboBox.setItemText(0, _translate("Txcreator", "WIF"))
        self.privkey_comboBox.setItemText(1, _translate("Txcreator", "Hex"))
        self.privkey_comboBox.setItemText(2, _translate("Txcreator", "Scalar"))


segwit_flag='0001'
SIGHASH_ALL = 1

#can these and their refrences go in the address functions file?
OP_HASH160 = b'\xa9'
OP_EQUAL = b'\x87'
EDU_MODE_OUTPUT=[]
EDU_MODE_UNSIGNED=[]
EDU_MODE_SIGS=[]

class tx_data_obj:

    def __init__(self, outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs):
        self.outs=outs
        self.tx_selection_types=tx_selection_types
        self.segwitprefix=segwitprefix
        # self.segwit_txinputs1=segwit_txinputs1
        self.legacy_prefix=legacy_prefix
        self.tx_inputs=tx_inputs
        self.input_secrets=input_secrets
        self.script_pubs=script_pubs
        # self.segwit_inputs=segwit_inputs
        self.segwit_input_infos=segwit_input_infos
        self.select_inputs=select_inputs

    
def tx_data():
    outs=[ui.scriptout1_box.text(),ui.scriptout2_box.text(),ui.scriptout3_box.text(),ui.scriptout4_box.text(),ui.scriptout5_box.text(),ui.scriptout6_box.text()]
    tx_selection_types=[ui.txtype_combobox_1.currentIndex(), ui.txtype_combobox_2.currentIndex(), ui.txtype_combobox_3.currentIndex(), ui.txtype_combobox_4.currentIndex(), ui.txtype_combobox_5.currentIndex(), ui.txtype_combobox_6.currentIndex()]
    segwitprefix=[ui.version_box.text(),segwit_flag,tx_num_func(ui.numins_combo.currentIndex())]
    # segwit_txinputs1=[[txid_endian(ui.txin1_box.text()), ui.inputindex1_box.text(),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), ui.inputindex2_box.text(),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), ui.inputindex3_box.text(),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), ui.inputindex4_box.text(),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), ui.inputindex5_box.text(),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), ui.inputindex6_box.text(),ui.sequence6_box.text()]]
    legacy_prefix=[ui.version_box.text(),tx_num_func(ui.numins_combo.currentIndex())]
    #this is same as segwit- can merge
    tx_inputs=[[txid_endian(ui.txin1_box.text()), ui.inputindex1_box.text(),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), ui.inputindex2_box.text(),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), ui.inputindex3_box.text(),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), ui.inputindex4_box.text(),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), ui.inputindex5_box.text(),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), ui.inputindex6_box.text(),ui.sequence6_box.text()]]
    input_secrets=[ui.privkey1_box.text(),ui.privkey2_box.text(),ui.privkey3_box.text(),ui.privkey4_box.text(),ui.privkey5_box.text(),ui.privkey6_box.text()]
    script_pubs=[ui.scriptpub1_box.text(), ui.scriptpub2_box.text(), ui.scriptpub3_box.text(), ui.scriptpub4_box.text(),ui.scriptpub5_box.text(), ui.scriptpub6_box.text()]
    segwit_input_infos=[[txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+ui.scriptpub1_box.text()+amount_to_txhex(ui.txinamount_box1.text())+ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+ui.scriptpub2_box.text()+amount_to_txhex(ui.txinamount_box2.text())+ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+ui.scriptpub3_box.text()+amount_to_txhex(ui.txinamount_box3.text())+ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+ui.scriptpub4_box.text()+amount_to_txhex(ui.txinamount_box4.text())+ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+ui.scriptpub5_box.text()+amount_to_txhex(ui.txinamount_box5.text())+ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()+ui.scriptpub6_box.text()+amount_to_txhex(ui.txinamount_box6.text())+ui.sequence6_box.text()]]
    select_inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    return tx_data_obj(outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs)


def ok_button():
    EDU_MODE_OUTPUT=[]
    gui_data=tx_data()
    print('WORKEDDDDD?', gui_data.outs[0])
    dersigs=[]
    multisig_dersigs=[]
    witness_program=[]
    segwit_indexs=[]
    p2sh_segwit_indexs=[]
    ms_segwit_indexes=[]
    p2pkhindexs=[]
    segwit_multisigs=[]
    multisig_indexes=[]

    
    # script_pubs=[ui.scriptpub1_box.text(), ui.scriptpub2_box.text(), ui.scriptpub3_box.text(), ui.scriptpub4_box.text(),ui.scriptpub5_box.text(), ui.scriptpub6_box.text()]
    outs=gui_data.outs
    tx_selections=list(gui_data.tx_selection_types)
    print('TX SELECTS',tx_selections)
  
    if ui.outputformat_combobox.currentIndex() ==1:
        outs_list=address_to_scriptpub()
        outs=outs_list


    count=0
    for item in tx_selections:
        print('ITEM ComBO', item)

        if item == '0':
            count+=1
            pass

        if item == 1:
            try:
                result= join_info(0, count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            dersigs.append(result)
             ## ADD THIS TO EDU MODE PRINTS
            print('DERSIG', dersigs)
            p2pkhindexs.append(count)
            count+=1

        if item== 2:
            try:
                result= join_info(99, count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            dersigs.append(result)
             ## ADD THIS TO EDU MODE PRINTS
            print('DERSIG', dersigs)
            p2pkhindexs.append(count)### CORRECT???
            count+=1

        if item == 3:
            result=join_segwit(1, count) 
            witness_program.append(result)
            print('P2SH WITNESS',count, witness_program)
            p2sh_segwit_indexs.append(count)
            count+=1

        if item == 4:
            result=join_segwit(1, count)
            print('RRRRRR', result)
            witness_program.append(result)
            dersigs.append('00')
            print('WITNESS',count, witness_program)
            segwit_indexs.append(count)
            count+=1


        if item == 5: #p2wsh
            result=join_segwit(98, count)  # add flag here for p2wsh segwit
            witness_program.append(result)
            print('P2SH WITNESS',count, witness_program)
            segwit_indexs.append(count)
            count+=1

        if item == 6:
            tx_selections=gui_data.tx_selection_types
            first_index=tx_selections.index(6)
            result=join_info(count,first_index)
            if result=='00':
                multisig_dersigs.insert(0, result)
            else:

                multisig_dersigs.append(result)
            print('MULTI DERSIG', multisig_dersigs)
            multisig_indexes.append(count)
            count+=1

        if item == 7:
            print('item7 count', count)
            tx_selections=gui_data.tx_selection_types
            first_index=tx_selections.index(7)
            result=join_segwit(count, first_index)  # add flag here for p2wsh segwit
            witness_program.append(result)
            dersigs.append('00')
            print('P2WSH WITNESS',count, witness_program)
            ms_segwit_indexes.append(count)
            count+=1
            #p2WSH multisg




## change below to class reference
    
    try:
        outputs=[tx_num_func(ui.numouts_combo.currentIndex()), amount_to_txhex(ui.amount1_box.text()),outs[0], amount_to_txhex(ui.amount2_box.text()),outs[1], amount_to_txhex(ui.amount3_box.text()),outs[2], amount_to_txhex(ui.amount4_box.text()),outs[3], amount_to_txhex(ui.amount5_box.text()),outs[4], amount_to_txhex(ui.amount6_box.text()),outs[5],ui.nlocktime_box.text()]
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again4')

        print('it happened no4')
        return

    tx_inputs=gui_data.tx_inputs

    if len(witness_program) != 0:
        print('segwit detected')
        prefix=gui_data.segwitprefix
        for txin in segwit_indexs:
            tx_inputs[txin].insert(2,'00')

        # for txin in ms_segwit_indexes[0]:
            

        for txin in p2pkhindexs:
            tx_inputs[txin].insert(2, dersigs[txin])
        for txin in p2sh_segwit_indexs:
            tx_inputs[txin].insert(2, '171600'+(gui_data.script_pubs[txin])[6:-4])
        if len(p2pkhindexs) != 0:
            outputs.insert((len(outputs)-1),'00')

        if len(ms_segwit_indexes) != 0:
            print('p2wsh activated')
            tx_inputs[ms_segwit_indexes[0]].insert(2,'00')
            witness_program.insert(0,(bytes([ui.multisig_spinbox.value()+2]).hex())+'00')

        print('WIT', witness_program)
        print('SEGWIT TX- DERSIGS', witness_program)
        outputs.insert((len(outputs)-1),"".join(witness_program) )



    elif len(multisig_indexes) != 0:
        print('multisig detected')
        prefix=gui_data.legacy_prefix
        print('NUMBER OF BLANK MULTISIG SIGS', int(ui.multisig_spinbox.value())-len(multisig_indexes))
        for item in range(0, (int(ui.multisig_spinbox.value()))-len(multisig_indexes)+1):
            multisig_dersigs.insert(0, '00')

        complete_dersig=bytes.fromhex("".join(multisig_dersigs))
        print('COMPLETE DERSIG', complete_dersig.hex())
        print('COMPLETE LEN', len(complete_dersig.hex()))
        print('LEN IN HEX FUNC', len_in_hex(complete_dersig))
        final_dersig=len_in_hex(complete_dersig)+complete_dersig
        print('FINAL MULSIG SIG', final_dersig.hex())
        print('multisig index value', (multisig_indexes[0]))
        tx_inputs[(multisig_indexes[0])].insert(2, final_dersig.hex())



        for txin in list(range(0, int(ui.numins_combo.currentIndex())+1)):
            print('TXIN NUMBER', txin)
            try:
                tx_inputs[txin].insert(2, dersigs[txin])
            except IndexError:
                pass
    else:     
        print('$$ LEGACY TX $$$')   
        prefix=gui_data.legacy_prefix

        for txin in list(range(0, int(ui.numins_combo.currentIndex())+1)):
            print('TXIN NUMBER', txin)
            try:
                tx_inputs[txin].insert(2, dersigs[txin])
            except IndexError:
                ui.output_box.setText('Please Select a Transaction Type to Sign1')
                return






    combined_inputs=[y for x in tx_inputs for y in x]
    print('FINAL_ins',combined_inputs)
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
     
    print('FINAL input info',input_info)
    signed_items=[(item) for item in input_info if item is not ""]
    ## ADD THIS TO EDU MODE PRINTS
    print('FINAL INPUT LIST',signed_items)

    for item in signed_items:
        try:
            EDU_MODE_OUTPUT.append(item+'\n')
        except TypeError:
            'Line 1006- ** ERROR ***'

    try:
        signed_tx="".join(signed_items)
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('it happened no3')
        # sys.exit("message")
        return

    print(signed_tx)
    if ui.education_checkbox.isChecked()==True:
        title_txt='TX DATA'+'\n'
        EDU_MODE_OUTPUT.insert(0,title_txt )
        edu_mode_print="".join(EDU_MODE_OUTPUT)
        ui.output_box.setText(edu_mode_print)

    else:
        ui.output_box.setText(signed_tx)

    print('SIGNED TX', signed_tx)
    return signed_tx



def tx_num_func(data):
    num_data=['01','02','03','04','05','06', '07', '08']
    #replace this with num to hex func
    selection=num_data[data]
    return selection

def amount_to_txhex(amount):  #concatanate this abit- use list comprehension?s
    if amount == '':
        return ''
    else:
        amount_flt=float(amount)
        amount_int=int(amount_flt*100000000)
        amount_hex=format(amount_int, 'x')
        amount_final=amount_hex.rjust(16, '0')
        tx_bytes=bytes(reversed(bytes.fromhex(amount_final)))
        return (tx_bytes.hex())



def txid_endian(txid):
    input_bytes=bytes(reversed(bytes.fromhex(txid)))
    return input_bytes.hex()



def join_info(script, index):
    gui_data=tx_data()
    print('join LEGACY script=', script)
    print('join LEGACY index=', index)
    tx_selections=gui_data.tx_selection_types
    multisig_indexs=[]
    count=0
    for tx in tx_selections:
        if tx==6:
            multisig_indexs.append(count)
            count+=1


    print('MULTISIG INDEXES', multisig_indexs)
    try:
        final_index=len(tx_selections) - 1 - tx_selections[::-1].index(6)
        if final_index == script:
            multisig =2
            print('MULTISIG FINAL VALUE DETECTED')
        else:
            multisig=1
            print('MULTISIG NON-FINAL DETECTED')

    except ValueError:
        multisig=0
        print('** NOT A MULTISIG ***')

    if script==99:
        multisig=3

    # if script


    outs=gui_data.outs
    if ui.outputformat_combobox.currentIndex() ==1:
        outs_list=address_to_scriptpub()
        outs=outs_list
    scriptpubs=gui_data.script_pubs
    insert_points=[ui.inputindex1_box.text, ui.inputindex2_box.text, ui.inputindex3_box.text, ui.inputindex4_box.text, ui.inputindex5_box.text, ui.inputindex6_box.text]

    if ui.outputformat_combobox.currentIndex()==1:
        pass
  
    prefix=[ui.version_box.text(),tx_num_func(ui.numins_combo.currentIndex())]

    inputs=[[txid_endian(ui.txin1_box.text()), ui.inputindex1_box.text(),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), ui.inputindex2_box.text(),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), ui.inputindex3_box.text(),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), ui.inputindex4_box.text(),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), ui.inputindex5_box.text(),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), ui.inputindex6_box.text(),ui.sequence6_box.text()]]

    outputs=[tx_num_func(ui.numouts_combo.currentIndex()),amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5],ui.nlocktime_box.text(),ui.hashtype_box.text()]

    inputs[index].insert(2, scriptpubs[index])

# ******************* not having below this may cause invlaid sig????????????????????????????????????????????
    # empty_scriptpubs=[(item) for item in multisig_indexs if item is not index]
    # for txindex in empty_scriptpubs:
    #     inputs[txindex].insert(2, '00')
    # print('EMPTY SCRIPTPUBS',empty_scriptpubs)

    num_ins=list(range(0, int(ui.numins_combo.currentIndex()+1)))

    print('NI',num_ins)
    other_indexes=[value for value in num_ins if value != index]
    print('OI',other_indexes)

    for num in other_indexes:
        inputs[num].insert(2, '00')
        

    combined_inputs=[y for x in inputs for y in x]
    print('Combined ins',combined_inputs)
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    print('input info',input_info)
    input_list=[(item) for item in input_info if item is not ""]
    ## USE THIS AS THE FIRST EDU MODE PRINT OUT- BREAK IT DOWN INTO COMPONENTS
    print('INPUT LIST',input_list)
    rawtx="".join(input_list)
    print('RAW TX', rawtx)
    ui.output_box.setText(rawtx)

    if multisig==1:
        dersig=sign_tx(rawtx, index, 1) #CONFIRM THIS IS SUPPOSED TO BE INDEX
        print('MULTISIG VALUE 1 DERSIG GENERATED')

    elif multisig ==2:
        dersig=sign_tx(rawtx, script, 2)
        print('MULTISIG VALUE 2 DERSIG GENERATED')

    elif multisig ==3:
        dersig=sign_tx(rawtx, index, 3)
        print('NO MULTISIG VALUE PASSED')


    else:
        dersig=sign_tx(rawtx, index)
        print('NO MULTISIG VALUE PASSED')

    return dersig


def join_segwit(script, index):
    gui_data=tx_data()
    print('Sign segwit Func')
    print('join SEGWIT script=', script)
    print('join SEGWIT index=', index)
    # print('SEGWIT SIGN FUNCT MULTISIG VALUE ==', multisig)
    tx_selections=gui_data.tx_selection_types
    multisig_indexs=[]
    count=0
    for tx in tx_selections:
        if tx==7:
            multisig_indexs.append(count)
            count+=1


    print('MULTISIG INDEXES', multisig_indexs)
    try:
        final_index=len(tx_selections) - 1 - tx_selections[::-1].index(7)
        if final_index == script:
            multisig =4
            print('MULTISIG FINAL VALUE DETECTED')
        else:
            multisig=3
            print('MULTISIG NON-FINAL DETECTED')

    except ValueError:
        multisig=0
        print('** NOT A MULTISIG ***')



    outs=gui_data.outs
    if ui.outputformat_combobox.currentIndex() ==1:
        outs_list=address_to_scriptpub()
        outs=outs_list
    scriptpubs=gui_data.script_pubs

    input_infos=gui_data.segwit_input_infos
    this_tx_input_infos="".join(input_infos[index])

    print('segwit- ins to hash=',[txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()])

    hash_ins=hash256(bytes.fromhex(txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()))
    hash_sequence=hash256(bytes.fromhex(ui.sequence1_box.text())+bytes.fromhex(ui.sequence2_box.text())+bytes.fromhex(ui.sequence3_box.text())+bytes.fromhex(ui.sequence4_box.text())+bytes.fromhex(ui.sequence5_box.text())+bytes.fromhex(ui.sequence6_box.text()))
    hash_outs=hash256(bytes.fromhex(amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5]))



    input_info=[ui.version_box.text(), hash_ins.hex(),hash_sequence.hex(),this_tx_input_infos, hash_outs.hex(),ui.nlocktime_box.text(), ui.hashtype_box.text()]

    

    input_list=[(item) for item in input_info if item is not ""]

    print('SEGWIT TX SCRIPT and index Value=', script)

    
    rawtx="".join(input_list)
    print('RAWTX=',rawtx)
    ui.output_box.setText(rawtx)

    if script == 98:
        print('P2WSH DETECTED-',input_list)
        # rawtx="".join(input_list)
        print('RAWTX- P2WSH=',rawtx)
        # ui.output_box.setText(rawtx)
        ##
        dersig='0300'+sign_tx(rawtx, index, 2)[2:]
        dersigpre='02'+sign_tx(rawtx, index, 2)
        dersig1=dersigpre[2:]
        print('P2WSH DERSIG V1=',dersig1)
        print('P2WSH DERSIG', dersig)

    if multisig==3:
        dersig=sign_tx(rawtx, script, 3)[2:]
        print('P2WSH MULTISIG VALUE 3 DERSIG GENERATED')

    elif multisig ==4:
        dersig=sign_tx(rawtx, script, 4)
        print('P2WSH MULTISIG VALUE 4 DERSIG GENERATED')

    else:
        print('P2WPKH Detected')
        print(input_list)

        dersig='02'+sign_tx(rawtx, index)[2:]
        dersigpre='02'+sign_tx(rawtx, index)
        dersig1=dersigpre[2:]
        print('SEGWIT DERSIG V1=',dersig1)
        print('SEGWIT DERSIG', dersig)
    return dersig



def sign_tx(rawtx, index, multisig=0):
    print('SIGN TX INDEX', index)
    gui_data=tx_data()

    script_pubs=gui_data.script_pubs

    print('SIGN FUNCT MULTISIG VALUE ==', multisig)
    try:
        unsignedtx=bytes.fromhex(rawtx)
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('it happened again')
        return

    unsigned_tx_hash = hash256(unsignedtx)
    ## ADD THIS TO EDU MODE PRINTS
    print('UTXHASH',unsigned_tx_hash.hex())

    input_secrets=gui_data.input_secrets

    print('PRIV INDEX',ui.privkey_comboBox.currentIndex())
    selection=ui.privkey_comboBox.currentIndex()
    if input_secrets[index]=='00':
        print('EMPTY PRIVKEY AT', index)
        return input_secrets[index]
    if selection==0:
         input_secret=scalar_from_wif(input_secrets[index])
         print('sacar from wif selected')

    if ui.privkey_comboBox.currentIndex()==1:
        input_secret=scalar_from_hex(input_secrets[index])
        print('sacar from hex selected')
    if ui.privkey_comboBox.currentIndex()==2:
        input_secret=int(input_secrets[index])
        print('scalar selected')


    print('INDEXXXX', index)
     ## ADD THIS TO EDU MODE PRINTS
    print('INPUT SECET=', input_secret)

    private_key = PrivateKey(input_secret)
    public_key_bytes = private_key.point.sec(compressed=True)
    signature = private_key.sign(int.from_bytes(unsigned_tx_hash, byteorder='big'))
    signature_bytes =signature.der() + bytes([SIGHASH_ALL])
    signature_bytes2=bytes([len(signature_bytes)])+signature_bytes

    

    if multisig==1:
        dersig2 = signature_bytes2
        print('MULTISIG1- && DERSIG &&', dersig2)

    elif multisig==2:
        sec2=bytes.fromhex(script_pubs[index])#does scriptpubs need to be global?, is this for every multisig or only at the end?
        # dersig2=signature_bytes2+sec2
        #figure out if then condition to conver the oppushbytes here if not needed
        dersig2=signature_bytes2+b'\x4c'+sec2
        print('MULTISIG2-FINAL && DERSIG &&', dersig2)

    elif multisig==3:
        sec2=bytes.fromhex(script_pubs[index])
        dersig=signature_bytes2
        dersig2=bytes([len(dersig+sec2)])+dersig+sec2
        print('P2WSH NON FINAL && DERSIG &&', dersig2)


    elif multisig==4:
        sec2=bytes.fromhex(script_pubs[index])
        dersig=signature_bytes2
        dersig2=dersig+sec2
        print('P2WSH MS-FINAL && DERSIG &&', dersig2)
    
    else:
        sec=private_key.point.sec()
        sec2=bytes([len(sec)])+sec
        dersig=signature_bytes2+sec2
         ## ADD THIS TO EDU MODE PRINTS
        print('NON MULTISIG- && DERSIG &&', dersig)
         ## ADD THIS TO EDU MODE PRINTS
        print('***SEC2***', sec2.hex())
        dersig2=bytes([len(dersig)])+dersig

    print(dersig2.hex())
    return dersig2.hex()






def scalar_from_wif(priv_key):
    num = 0
    for c in priv_key.encode('ascii'):
        num *= 58
        num += BASE58.index(c)
    hex_secret=hex(num)[2:]
    combined = bytes.fromhex(hex_secret)
    checksum = combined[-4:]
    if hash256(combined[:-4])[:4] != checksum:
        raise RuntimeError('bad address: {} {}'.format(checksum, hash256(combined)[:4]))
    hex_secret_trimmed=codecs.encode(combined[1:-5], 'hex')
    hex_secret_trimmed_str=hex_secret_trimmed.decode("utf-8")
     ## ADD THIS TO EDU MODE PRINTS
    print('HEX SECRET=',hex_secret_trimmed_str)
    return int(hex_secret_trimmed_str, 16)


def scalar_from_hex(hexstring):
    return int(hexstring, 16)

#need option for none here
# def txtype_combo_func(data, index):
#     gui_data=tx_data()
#     address_data=['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig']
#     selection=address_data[data]
#     print('SELECTION=',selection)
#     if selection=='P2PKH':
#         # join_info(0, index)
#         try:
#             return join_info(0, index)
#         except TypeError:
#             ui.output_box.setText('Invalid Input- Please check your input data and try again')
#             return
#     elif selection=='p2shsegwit':
#         #Change function name below to just segwit- can it handle both with script option?
#         return join_segwit_p2sh(1, index)

#     elif selection=='p2sh':
#         join_info(1)
#     elif selection=='P2WPKH':
#         return join_segwit(1, index)
#     elif selection=='p2wsh':
#         output=join_segwit(1)

#     elif selection == 'P2SH multisig':
#         #this is an object as txcombo_types
#         # tx_types=[ui.txtype_combobox_1.currentIndex(), ui.txtype_combobox_2.currentIndex(), ui.txtype_combobox_3.currentIndex(), ui.txtype_combobox_4.currentIndex(), ui.txtype_combobox_5.currentIndex(), ui.txtype_combobox_6.currentIndex(),]
#         tx_selections=gui_data.tx_selection_types
#         first_index=tx_selections.index(6)
#         return join_info(index, first_index)







def p2sh_redeemscript(pubkey):
    h160=hash160(bytes.fromhex(pubkey))
    redeemscript_hash=hash160(OP_0+bytes([len(h160)])+h160)
    redeemscript=(OP_0+bytes([len(h160)])+h160).hex()
    script_pub= b''.join([
        OP_HASH160,
        bytes([len(redeemscript_hash)]),
        redeemscript_hash,
        OP_EQUAL,
        ])
    script_pub_full=bytes([len(script_pub)])+script_pub
    print('scriptpubkey- not used', script_pub_full.hex())
    return redeemscript


def address_to_scriptpub():
    gui_data=tx_data()
    outs=gui_data.outs
    scriptpub_list=[]
    for item in outs:
        if item[:2]=='tb':#AND bc
            hex_chars=decode(item[:2], item)[1]
            hex_chars_list=[]
            for i in hex_chars:
                hex_chars_list.append(bytes([i]).hex())
                h256="".join(hex_chars_list)
            h256len=str(int((int(bytes([len(h256)]).hex())/2)))
            print('h256len', h256len)
            scriptpub_raw='00'+h256len+h256
            scriptpub=bytes([len(bytes.fromhex(scriptpub_raw))]).hex()+scriptpub_raw
            print('THIS NEEDS TO BE APPENDED TO A LIST', scriptpub)
        
        if item[:1]=='3':# AND 2
            scriptpub='17a914'+decode_base58(item).hex()+'87'

        if item[:1]=='2':# AND 2
            scriptpub='17a914'+decode_base58(item).hex()+'87'

        if item[:1]=='m': #can m and n be put into one value to check for?
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return

        if item[:1]=='n':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return

        if item[:1]=='1':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
        if item=='':
            scriptpub=''


        scriptpub_list.append(scriptpub)

    return scriptpub_list

def int_to_nlocktime():
    try:
        block=int(ui.currentblock_box.text())
        print('BLOCK', block)
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        return

    block_hex=bytes(reversed(block.to_bytes(4, 'big')))
    print(block_hex)
    ui.nlocktime_box.setText(block_hex.hex())
    return block_hex



def len_in_hex(item):
    #this is hacky- make sureits consistent over various m of n multsig tx types- same with -1's below
    length=(len(item.hex())/2)-1
    print('len func LENGTH',length)

    if length > 4294967295:
        return b'\xff'+(len(bytes.fromhex(item.hex()))-1).to_bytes(8, byteorder='little')#.hex()

    elif length > 65535:
        return b'\xfe'+(len(bytes.fromhex(item.hex()))-1).to_bytes(4, byteorder='little')#.hex()

    elif length > 252:
        return b'\xfd'+(len(bytes.fromhex(item.hex()))).to_bytes(2, byteorder='little')#.hex()

    else:
        return bytes([len(bytes.fromhex(item.hex()))])#.hex()


def combofunc(index):
    print('COMBO ACT', index)
    tx_select_func(index)



# unessesary? remove along with references at line 470?
def tx_select_func(index):
    print('SELEC ACT', index)
    inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    address_data=['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig']
    selection=address_data[inputs[index-1].currentIndex()]
    # print('info', inputs[index].currentIndex())
    print('selection ACT', selection)


    ## refactor- delete the outpub boxes below and adjust list indess in conditions below

    boxes=[[ui.txinamount_box1,ui.inputindex1_box,ui.txin1_box,ui.scriptpub1_box,ui.sequence1_box,ui.amount1_box,ui.scriptout1_box,ui.privkey1_box],
            [ui.txinamount_box2,ui.inputindex2_box,ui.txin2_box,ui.scriptpub2_box,ui.sequence2_box,ui.amount2_box,ui.scriptout2_box,ui.privkey2_box],
            [ui.txinamount_box3,ui.inputindex3_box,ui.txin3_box,ui.scriptpub3_box,ui.sequence3_box,ui.amount3_box,ui.scriptout3_box,ui.privkey3_box],
            [ui.txinamount_box4,ui.inputindex4_box,ui.txin4_box,ui.scriptpub4_box,ui.sequence4_box,ui.amount4_box,ui.scriptout4_box,ui.privkey4_box],
            [ui.txinamount_box5,ui.inputindex5_box,ui.txin5_box,ui.scriptpub5_box,ui.sequence5_box,ui.amount5_box,ui.scriptout5_box,ui.privkey5_box],
            [ui.txinamount_box6,ui.inputindex6_box,ui.txin6_box,ui.scriptpub6_box,ui.sequence6_box,ui.amount6_box,ui.scriptout6_box,ui.privkey6_box]]

    if selection=='N/A':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(True)
        i[2].setDisabled(True)
        i[3].setDisabled(True)
        i[4].setDisabled(True)
        # i[5].setDisabled(True)
        # i[6].setDisabled(True)
        i[7].setDisabled(True)

    elif selection=='P2PKH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        # i[5].setDisabled(False)
        # i[6].setDisabled(False)
        i[7].setDisabled(False)
    
    elif selection=='P2SH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        # i[5].setDisabled(False)
        # i[6].setDisabled(False)
        i[7].setDisabled(False)

    elif selection=='P2SH multisig':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        # i[5].setDisabled(False)
        # i[6].setDisabled(False)
        i[7].setDisabled(False)

    else:
        i=boxes[index-1]
        i[0].setDisabled(False)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        # i[5].setDisabled(False)
        # i[6].setDisabled(False)
        i[7].setDisabled(False)
    return selection

def ins_activate(total):
    boxes=[[ui.txinamount_box1,ui.inputindex1_box,ui.txin1_box,ui.scriptpub1_box,ui.sequence1_box,ui.privkey1_box],
        [ui.txinamount_box2,ui.inputindex2_box,ui.txin2_box,ui.scriptpub2_box,ui.sequence2_box,ui.privkey2_box],
        [ui.txinamount_box3,ui.inputindex3_box,ui.txin3_box,ui.scriptpub3_box,ui.sequence3_box,ui.privkey3_box],
        [ui.txinamount_box4,ui.inputindex4_box,ui.txin4_box,ui.scriptpub4_box,ui.sequence4_box,ui.privkey4_box],
        [ui.txinamount_box5,ui.inputindex5_box,ui.txin5_box,ui.scriptpub5_box,ui.sequence5_box,ui.privkey5_box],
        [ui.txinamount_box6,ui.inputindex6_box,ui.txin6_box,ui.scriptpub6_box,ui.sequence6_box,ui.privkey6_box]]
    for outlist in boxes:
        for item in outlist:
            item.setDisabled(True)
    outs_list=range(0,total)
    for out in outs_list:
        i=boxes[out]
        i[0].setDisabled(False)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[5].setDisabled(False)


def outs_activate(total):
    boxes=[[ui.amount1_box,ui.scriptout1_box],[ui.amount2_box,ui.scriptout2_box],[ui.amount3_box,ui.scriptout3_box],[ui.amount4_box,ui.scriptout4_box],
            [ui.amount5_box,ui.scriptout5_box],[ui.amount6_box,ui.scriptout6_box]]
    for outlist in boxes:
        for item in outlist:
            item.setDisabled(True)
    outs_list=range(0,total)
    for out in outs_list:
        i=boxes[out]
        i[0].setDisabled(False)
        i[1].setDisabled(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    splash_pix = QPixmap('test_splash.png')
    splash = QtWidgets.QSplashScreen(splash_pix)#, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    time.sleep(1)
    Dialog.show()

    splash.finish(Dialog)
    
    sys.exit(app.exec_())
    app = QApplication(sys.argv)







