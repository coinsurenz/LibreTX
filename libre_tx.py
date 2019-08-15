# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'txcreator4e.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from ecdsa_functions import *
from address_functions import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
import libre_tx_rc
import time
import struct


class Ui_Libre_Tx(object):
    def setupUi(self, Libre_Tx):
        Libre_Tx.setObjectName("Libre_Tx")
        Libre_Tx.resize(1618, 862)
        Libre_Tx.setMinimumSize(QtCore.QSize(1668, 862))
        Libre_Tx.setMaximumSize(QtCore.QSize(1668, 886))
        Libre_Tx.setProperty("script_pubkey", "")
        self.gridLayout = QtWidgets.QGridLayout(Libre_Tx)
        self.gridLayout.setObjectName("gridLayout")
        self.privkey6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey6_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey6_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey6_box.setObjectName("privkey6_box")
        self.gridLayout.addWidget(self.privkey6_box, 28, 4, 1, 1)
        self.scriptpub1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub1_box.setObjectName("scriptpub1_box")
        self.gridLayout.addWidget(self.scriptpub1_box, 6, 4, 1, 1)
        self.txin6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin6_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin6_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin6_box.setObjectName("txin6_box")
        self.gridLayout.addWidget(self.txin6_box, 11, 3, 1, 1)
        self.privkey3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey3_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey3_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey3_box.setObjectName("privkey3_box")
        self.gridLayout.addWidget(self.privkey3_box, 23, 4, 1, 1)
        self.inputindex1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex1_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex1_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex1_box.setObjectName("inputindex1_box")
        self.gridLayout.addWidget(self.inputindex1_box, 6, 2, 1, 1)
        self.txinamounts_label = QtWidgets.QLabel(Libre_Tx)
        self.txinamounts_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txinamounts_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.txinamounts_label.setFont(font)
        self.txinamounts_label.setObjectName("txinamounts_label")
        self.gridLayout.addWidget(self.txinamounts_label, 5, 0, 1, 1)
        self.scriptpubkey_label = QtWidgets.QLabel(Libre_Tx)
        self.scriptpubkey_label.setMinimumSize(QtCore.QSize(0, 20))
        self.scriptpubkey_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setItalic(False)
        font.setBold(True)
        self.scriptpubkey_label.setFont(font)
        self.scriptpubkey_label.setObjectName("scriptpubkey_label")
        self.gridLayout.addWidget(self.scriptpubkey_label, 5, 4, 1, 1)
        self.outputformat_label = QtWidgets.QLabel(Libre_Tx)
        self.outputformat_label.setMinimumSize(QtCore.QSize(0, 20))
        self.outputformat_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setBold(True)
        self.outputformat_label.setFont(font)
        self.outputformat_label.setObjectName("outputformat_label")
        self.gridLayout.addWidget(self.outputformat_label, 5, 5, 1, 1)
        self.inputindex2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex2_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex2_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex2_box.setObjectName("inputindex2_box")
        self.gridLayout.addWidget(self.inputindex2_box, 7, 2, 1, 1)
        self.scriptout2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout2_box.setObjectName("scriptout2_box")
        self.gridLayout.addWidget(self.scriptout2_box, 21, 3, 1, 1)
        self.scriptout3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout3_box.setObjectName("scriptout3_box")
        self.gridLayout.addWidget(self.scriptout3_box, 23, 3, 1, 1)
        self.txinamount_box6 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box6.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box6.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box6.setObjectName("txinamount_box6")
        self.gridLayout.addWidget(self.txinamount_box6, 11, 0, 1, 1)
        self.txtype_combobox_1 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_1.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_1.setObjectName("txtype_combobox")
        self.gridLayout.addWidget(self.txtype_combobox_1, 6, 1, 1, 1)
        self.inputindex5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex5_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex5_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex5_box.setObjectName("inputindex5_box")
        self.gridLayout.addWidget(self.inputindex5_box, 10, 2, 1, 1)
        self.scriptpub6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub6_box.setObjectName("scriptpub6_box")
        self.gridLayout.addWidget(self.scriptpub6_box, 11, 4, 1, 1)
        self.txtype_combobox_4 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_4.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_4.setObjectName("txtype_combobox_4")
        self.gridLayout.addWidget(self.txtype_combobox_4, 9, 1, 1, 1)
        self.outputformat_combobox = QtWidgets.QComboBox(Libre_Tx)
        self.outputformat_combobox.setProperty("bitcoin_address", "")
        self.outputformat_combobox.setObjectName("outputformat_combobox")
        self.gridLayout.addWidget(self.outputformat_combobox, 6, 5, 1, 1)
        self.txin2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin2_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin2_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin2_box.setObjectName("txin2_box")
        self.gridLayout.addWidget(self.txin2_box, 7, 3, 1, 1)
        self.txin3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin3_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin3_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin3_box.setObjectName("txin3_box")
        self.gridLayout.addWidget(self.txin3_box, 8, 3, 1, 1)
        self.inputindex4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex4_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex4_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex4_box.setObjectName("inputindex4_box")
        self.gridLayout.addWidget(self.inputindex4_box, 9, 2, 1, 1)
        self.inputindex6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex6_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex6_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex6_box.setObjectName("inputindex6_box")
        self.gridLayout.addWidget(self.inputindex6_box, 11, 2, 1, 1)
        self.privkey1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey1_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey1_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey1_box.setObjectName("privkey1_box")
        self.gridLayout.addWidget(self.privkey1_box, 18, 4, 1, 1)
        self.privkey4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey4_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey4_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey4_box.setObjectName("privkey4_box")
        self.gridLayout.addWidget(self.privkey4_box, 25, 4, 1, 1)
        self.privkeyformat_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.privkeyformat_label.setFont(font)
        self.privkeyformat_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.privkeyformat_label.setObjectName("privkeyformat_label")
        self.gridLayout.addWidget(self.privkeyformat_label, 12, 4, 1, 1)
        self.scriptout1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout1_box.setObjectName("scriptout1_box")
        self.gridLayout.addWidget(self.scriptout1_box, 18, 3, 1, 1)
        self.unsigned_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.unsigned_label.setFont(font)
        self.unsigned_label.setObjectName("unsigned_label")
        self.gridLayout.addWidget(self.unsigned_label, 23, 6, 1, 1)
        self.txin4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin4_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin4_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin4_box.setObjectName("txin4_box")
        self.gridLayout.addWidget(self.txin4_box, 9, 3, 1, 1)
        self.txinamount_box1 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box1.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box1.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box1.setObjectName("txinamount_box1")
        self.gridLayout.addWidget(self.txinamount_box1, 6, 0, 1, 1)
        self.txtype_combobox_3 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_3.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_3.setObjectName("txtype_combobox_3")
        self.gridLayout.addWidget(self.txtype_combobox_3, 8, 1, 1, 1)
        self.txin5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin5_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin5_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin5_box.setObjectName("txin5_box")
        self.gridLayout.addWidget(self.txin5_box, 10, 3, 1, 1)
        self.txinamount_box3 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box3.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box3.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box3.setObjectName("txinamount_box3")
        self.gridLayout.addWidget(self.txinamount_box3, 8, 0, 1, 1)
        self.privkey2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey2_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey2_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey2_box.setObjectName("privkey2_box")
        self.gridLayout.addWidget(self.privkey2_box, 21, 4, 1, 1)
        self.sequence2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence2_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence2_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence2_box.setObjectName("sequence2_box")
        self.gridLayout.addWidget(self.sequence2_box, 21, 0, 1, 1)
        self.output_box = QtWidgets.QTextBrowser(Libre_Tx)
        self.output_box.setMinimumSize(QtCore.QSize(1600, 300))
        self.output_box.setMaximumSize(QtCore.QSize(1600, 300))
        output_font = QtGui.QFont()
        output_font.setFamily("Sans Serif")
        output_font.setPointSize(14)
        font.setBold(True)
        self.output_box.setFont(output_font)
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 34, 0, 4, 13)
        self.icon = QtWidgets.QLabel(Libre_Tx)
        self.icon.setMaximumSize(QtCore.QSize(150, 195))
        self.icon.setText("")

        #
        self.icon.setPixmap(QtGui.QPixmap(":/images/libre_tx_inappicon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 6, 6, 7, 1)
        self.tx_type1_label = QtWidgets.QLabel(Libre_Tx)
        self.tx_type1_label.setMinimumSize(QtCore.QSize(0, 20))
        self.tx_type1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.tx_type1_label.setFont(font)
        self.tx_type1_label.setObjectName("tx_type1_label")
        self.gridLayout.addWidget(self.tx_type1_label, 5, 1, 1, 1)
        self.scriptpub3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub3_box.setObjectName("scriptpub3_box")
        self.gridLayout.addWidget(self.scriptpub3_box, 8, 4, 1, 1)
        self.sequence_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.sequence_label.setFont(font)
        self.sequence_label.setObjectName("sequence_label")
        self.gridLayout.addWidget(self.sequence_label, 12, 0, 1, 1)
        self.privkey5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey5_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey5_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey5_box.setObjectName("privkey5_box")
        self.gridLayout.addWidget(self.privkey5_box, 26, 4, 1, 1)
        self.amount1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount1_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount1_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount1_box.setObjectName("amount1_box")
        self.gridLayout.addWidget(self.amount1_box, 18, 2, 1, 1)
        self.amount4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount4_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount4_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount4_box.setObjectName("amount4_box")
        self.gridLayout.addWidget(self.amount4_box, 25, 2, 1, 1)
        self.txinamount_box5 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box5.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box5.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box5.setObjectName("txinamount_box5")
        self.gridLayout.addWidget(self.txinamount_box5, 10, 0, 1, 1)
        self.txin1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin1_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin1_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin1_box.setObjectName("txin1_box")
        self.gridLayout.addWidget(self.txin1_box, 6, 3, 1, 1)
        self.scriptout5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout5_box.setObjectName("scriptout5_box")
        self.gridLayout.addWidget(self.scriptout5_box, 26, 3, 1, 1)
        self.txtype_combobox_5 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_5.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_5.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_5.setObjectName("txtype_combobox_5")
        self.gridLayout.addWidget(self.txtype_combobox_5, 10, 1, 1, 1)
        self.locktime_button = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.locktime_button.setFont(font)
        self.locktime_button.setObjectName("locktime_button")
        self.gridLayout.addWidget(self.locktime_button, 11, 5, 1, 1)
        self.scriptpub4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub4_box.setObjectName("scriptpub4_box")
        self.gridLayout.addWidget(self.scriptpub4_box, 9, 4, 1, 1)
        self.amounts_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.amounts_label.setFont(font)
        self.amounts_label.setObjectName("amounts_label")
        self.gridLayout.addWidget(self.amounts_label, 12, 2, 1, 1)
        self.Title_label = QtWidgets.QLabel(Libre_Tx)
        self.Title_label.setMinimumSize(QtCore.QSize(20, 30))
        self.Title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Title_label.setPixmap(QtGui.QPixmap(":/images/librelogo.png"))
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        self.gridLayout.addWidget(self.Title_label, 0, 3, 1, 2)
        self.sequence3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence3_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence3_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence3_box.setObjectName("sequence3_box")
        self.gridLayout.addWidget(self.sequence3_box, 23, 0, 1, 1)
        self.txins_label = QtWidgets.QLabel(Libre_Tx)
        self.txins_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txins_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.txins_label.setFont(font)
        self.txins_label.setObjectName("txins_label")
        self.gridLayout.addWidget(self.txins_label, 5, 3, 1, 1)
        self.privkey_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.privkey_label.setFont(font)
        self.privkey_label.setObjectName("privkey_label")
        self.gridLayout.addWidget(self.privkey_label, 12, 4, 1, 1)
        self.sequence1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence1_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence1_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence1_box.setObjectName("sequence1_box")
        self.gridLayout.addWidget(self.sequence1_box, 18, 0, 1, 1)
        self.sequence5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence5_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence5_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence5_box.setObjectName("sequence5_box")
        self.gridLayout.addWidget(self.sequence5_box, 26, 0, 1, 1)
        self.inputindex_label = QtWidgets.QLabel(Libre_Tx)
        self.inputindex_label.setMinimumSize(QtCore.QSize(0, 20))
        self.inputindex_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.inputindex_label.setFont(font)
        self.inputindex_label.setObjectName("inputindex_label")
        self.gridLayout.addWidget(self.inputindex_label, 5, 2, 1, 1)
        self.version_box = QtWidgets.QLineEdit(Libre_Tx)
        self.version_box.setMinimumSize(QtCore.QSize(100, 0))
        self.version_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.version_box.setObjectName("version_box")
        self.gridLayout.addWidget(self.version_box, 28, 5, 1, 1)
        self.signed_button = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.signed_button.setFont(font)
        self.signed_button.setObjectName("Signed_button")
        self.gridLayout.addWidget(self.signed_button, 28, 6, 1, 1)
        self.txtype_combobox_2 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_2.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_2.setObjectName("txtype_combobox_2")
        self.gridLayout.addWidget(self.txtype_combobox_2, 7, 1, 1, 1)
        self.hashtype_box = QtWidgets.QLineEdit(Libre_Tx)
        self.hashtype_box.setMinimumSize(QtCore.QSize(100, 0))
        self.hashtype_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hashtype_box.setObjectName("hashtype_box")
        self.gridLayout.addWidget(self.hashtype_box, 25, 5, 1, 1)
        self.currentblock_box = QtWidgets.QLineEdit(Libre_Tx)
        self.currentblock_box.setMinimumSize(QtCore.QSize(100, 0))
        self.currentblock_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.currentblock_box.setObjectName("currentblock_box")
        self.gridLayout.addWidget(self.currentblock_box, 10, 5, 1, 1)
        self.pubouts_label = QtWidgets.QLabel(Libre_Tx)
        self.pubouts_label.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.pubouts_label.setFont(font)
        self.pubouts_label.setObjectName("pubouts_label")
        self.gridLayout.addWidget(self.pubouts_label, 12, 3, 1, 1)
        self.amount6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount6_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount6_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount6_box.setObjectName("amount6_box")
        self.gridLayout.addWidget(self.amount6_box, 28, 2, 1, 1)
        self.txinamount_box4 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box4.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box4.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box4.setObjectName("txinamount_box4")
        self.gridLayout.addWidget(self.txinamount_box4, 9, 0, 1, 1)
        self.numins_combo = QtWidgets.QComboBox(Libre_Tx)
        self.numins_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numins_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numins_combo.setObjectName("numins_combo")
        self.gridLayout.addWidget(self.numins_combo, 18, 1, 1, 1)
        self.sequence6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence6_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence6_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence6_box.setObjectName("sequence6_box")
        self.gridLayout.addWidget(self.sequence6_box, 28, 0, 1, 1)
        self.amount3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount3_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount3_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount3_box.setObjectName("amount3_box")
        self.gridLayout.addWidget(self.amount3_box, 23, 2, 1, 1)
        self.currentblock_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.currentblock_label.setFont(font)
        self.currentblock_label.setObjectName("currentblock_label")
        self.gridLayout.addWidget(self.currentblock_label, 9, 5, 1, 1)
        self.privkey_comboBox = QtWidgets.QComboBox(Libre_Tx)
        self.privkey_comboBox.setObjectName("privkey_comboBox")
        self.gridLayout.addWidget(self.privkey_comboBox, 12, 5, 1, 1)
        self.numouts_combo = QtWidgets.QComboBox(Libre_Tx)
        self.numouts_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numouts_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numouts_combo.setObjectName("numouts_combo")
        self.gridLayout.addWidget(self.numouts_combo, 23, 1, 1, 1)
        self.txinamount_box2 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box2.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box2.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box2.setObjectName("txinamount_box2")
        self.gridLayout.addWidget(self.txinamount_box2, 7, 0, 1, 1)
        self.numins_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.numins_label.setFont(font)
        self.numins_label.setObjectName("numins_label")
        self.gridLayout.addWidget(self.numins_label, 12, 1, 1, 1)
        self.hashtype_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.hashtype_label.setFont(font)
        self.hashtype_label.setObjectName("hashtype_label")
        self.gridLayout.addWidget(self.hashtype_label, 23, 5, 1, 1)
        self.signtx_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.signtx_label.setFont(font)
        self.signtx_label.setObjectName("signtx_label")
        self.gridLayout.addWidget(self.signtx_label, 26, 6, 1, 1)
        self.nlocktime_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.nlocktime_label.setFont(font)
        self.nlocktime_label.setObjectName("nlocktime_label")
        self.gridLayout.addWidget(self.nlocktime_label, 18, 5, 1, 1)
        self.numouts_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.numouts_label.setFont(font)
        self.numouts_label.setObjectName("numouts_label")
        self.gridLayout.addWidget(self.numouts_label, 21, 1, 1, 1)
        self.sequence4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence4_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence4_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence4_box.setObjectName("sequence4_box")
        self.gridLayout.addWidget(self.sequence4_box, 25, 0, 1, 1)
        self.scriptpub2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub2_box.setObjectName("scriptpub2_box")
        self.gridLayout.addWidget(self.scriptpub2_box, 7, 4, 1, 1)
        self.scriptout6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout6_box.setObjectName("scriptout6_box")
        self.gridLayout.addWidget(self.scriptout6_box, 28, 3, 1, 1)
        self.txtype_combobox_6 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_6.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_6.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_6.setObjectName("txtype_combobox_6")
        self.gridLayout.addWidget(self.txtype_combobox_6, 11, 1, 1, 1)
        self.scriptpub5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub5_box.setObjectName("scriptpub5_box")
        self.gridLayout.addWidget(self.scriptpub5_box, 10, 4, 1, 1)
        self.scriptout4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout4_box.setObjectName("scriptout4_box")
        self.gridLayout.addWidget(self.scriptout4_box, 25, 3, 1, 1)
        self.amount2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount2_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount2_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount2_box.setObjectName("amount2_box")
        self.gridLayout.addWidget(self.amount2_box, 21, 2, 1, 1)
        self.nlocktime_box = QtWidgets.QLineEdit(Libre_Tx)
        self.nlocktime_box.setMinimumSize(QtCore.QSize(100, 0))
        self.nlocktime_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.nlocktime_box.setObjectName("nlocktime_box")
        self.gridLayout.addWidget(self.nlocktime_box, 21, 5, 1, 1)
        self.inputindex3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex3_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex3_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex3_box.setObjectName("inputindex3_box")
        self.gridLayout.addWidget(self.inputindex3_box, 8, 2, 1, 1)
        self.version_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.gridLayout.addWidget(self.version_label, 26, 5, 1, 1)
        self.amount5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount5_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount5_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount5_box.setObjectName("amount5_box")
        self.gridLayout.addWidget(self.amount5_box, 26, 2, 1, 1)
        self.txtype_combobox_1.activated.connect(lambda: tx_select_func(1))
        self.txtype_combobox_2.activated.connect(lambda: tx_select_func(2))
        self.txtype_combobox_3.activated.connect(lambda: tx_select_func(3))
        self.txtype_combobox_4.activated.connect(lambda: tx_select_func(4))
        self.txtype_combobox_5.activated.connect(lambda: tx_select_func(5))
        self.txtype_combobox_6.activated.connect(lambda: tx_select_func(6))
        self.numouts_combo.activated.connect(lambda: outs_activate(self.numouts_combo.currentIndex()+1))
        self.txinamount_box1.setDisabled(True)
        self.inputindex1_box.setDisabled(True)
        self.scriptpub1_box.setDisabled(True)
        self.txin1_box.setDisabled(True)
        self.privkey1_box.setDisabled(True)
        self.sequence1_box.setDisabled(True)
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
        self.privkey_comboBox.addItems(['WIF','Hex','Scalar'])
        self.numins_combo.addItems(['01','02','03','04','05','06'])
        self.numouts_combo.addItems(['01','02','03','04','05','06'])
        self.outputformat_combobox.addItems(['Address','Scriptpub'])
        self.signed_button.clicked.connect(ok_button)
        self.txtype_combobox_1.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_2.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_3.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_4.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_5.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_6.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.locktime_button.clicked.connect(int_to_nlocktime)
        
        self.retranslateUi(Libre_Tx)
        QtCore.QMetaObject.connectSlotsByName(Libre_Tx)
        Libre_Tx.setTabOrder(self.txtype_combobox_1, self.inputindex1_box)
        Libre_Tx.setTabOrder(self.inputindex1_box, self.txin1_box)
        Libre_Tx.setTabOrder(self.txin1_box, self.scriptpub1_box)
        Libre_Tx.setTabOrder(self.scriptpub1_box, self.sequence1_box)
        Libre_Tx.setTabOrder(self.sequence1_box, self.numins_combo)
        Libre_Tx.setTabOrder(self.numins_combo, self.numouts_combo)
        Libre_Tx.setTabOrder(self.numouts_combo, self.amount1_box)
        Libre_Tx.setTabOrder(self.amount1_box, self.scriptout1_box)
        Libre_Tx.setTabOrder(self.scriptout1_box, self.privkey1_box)
        Libre_Tx.setTabOrder(self.privkey1_box, self.txtype_combobox_2)
        Libre_Tx.setTabOrder(self.txtype_combobox_2, self.inputindex2_box)
        Libre_Tx.setTabOrder(self.inputindex2_box, self.txin2_box)
        Libre_Tx.setTabOrder(self.txin2_box, self.scriptpub2_box)
        Libre_Tx.setTabOrder(self.scriptpub2_box, self.sequence2_box)
        Libre_Tx.setTabOrder(self.sequence2_box, self.amount2_box)
        Libre_Tx.setTabOrder(self.amount2_box, self.scriptout2_box)
        Libre_Tx.setTabOrder(self.scriptout2_box, self.privkey2_box)
        Libre_Tx.setTabOrder(self.privkey2_box, self.txtype_combobox_3)
        Libre_Tx.setTabOrder(self.txtype_combobox_3, self.inputindex3_box)
        Libre_Tx.setTabOrder(self.inputindex3_box, self.txin3_box)
        Libre_Tx.setTabOrder(self.txin3_box, self.scriptpub3_box)
        Libre_Tx.setTabOrder(self.scriptpub3_box, self.sequence3_box)
        Libre_Tx.setTabOrder(self.sequence3_box, self.amount3_box)
        Libre_Tx.setTabOrder(self.amount3_box, self.scriptout3_box)
        Libre_Tx.setTabOrder(self.scriptout3_box, self.privkey3_box)
        Libre_Tx.setTabOrder(self.privkey3_box, self.txtype_combobox_4)
        Libre_Tx.setTabOrder(self.txtype_combobox_4, self.inputindex4_box)
        Libre_Tx.setTabOrder(self.inputindex4_box, self.txin4_box)
        Libre_Tx.setTabOrder(self.txin4_box, self.scriptpub4_box)
        Libre_Tx.setTabOrder(self.scriptpub4_box, self.sequence4_box)
        Libre_Tx.setTabOrder(self.sequence4_box, self.amount4_box)
        Libre_Tx.setTabOrder(self.amount4_box, self.scriptout4_box)
        Libre_Tx.setTabOrder(self.scriptout4_box, self.privkey4_box)
        Libre_Tx.setTabOrder(self.privkey4_box, self.txtype_combobox_5)
        Libre_Tx.setTabOrder(self.txtype_combobox_5, self.inputindex5_box)
        Libre_Tx.setTabOrder(self.inputindex5_box, self.txin5_box)
        Libre_Tx.setTabOrder(self.txin5_box, self.scriptpub5_box)
        Libre_Tx.setTabOrder(self.scriptpub5_box, self.sequence5_box)
        Libre_Tx.setTabOrder(self.sequence5_box, self.amount5_box)
        Libre_Tx.setTabOrder(self.amount5_box, self.scriptout5_box)
        Libre_Tx.setTabOrder(self.scriptout5_box, self.privkey5_box)
        Libre_Tx.setTabOrder(self.privkey5_box, self.txtype_combobox_6)
        Libre_Tx.setTabOrder(self.txtype_combobox_6, self.inputindex6_box)
        Libre_Tx.setTabOrder(self.inputindex6_box, self.txin6_box)
        Libre_Tx.setTabOrder(self.txin6_box, self.scriptpub6_box)
        Libre_Tx.setTabOrder(self.scriptpub6_box, self.sequence6_box)
        Libre_Tx.setTabOrder(self.sequence6_box, self.amount6_box)
        Libre_Tx.setTabOrder(self.amount6_box, self.scriptout6_box)
        Libre_Tx.setTabOrder(self.scriptout6_box, self.privkey6_box)
        Libre_Tx.setTabOrder(self.privkey6_box, self.outputformat_combobox)
        Libre_Tx.setTabOrder(self.outputformat_combobox, self.currentblock_box)
        Libre_Tx.setTabOrder(self.currentblock_box, self.locktime_button)
        Libre_Tx.setTabOrder(self.locktime_button, self.privkey_comboBox)
        Libre_Tx.setTabOrder(self.privkey_comboBox, self.nlocktime_box)
        Libre_Tx.setTabOrder(self.nlocktime_box, self.hashtype_box)
        Libre_Tx.setTabOrder(self.hashtype_box, self.version_box)
        Libre_Tx.setTabOrder(self.version_box, self.signed_button)


    def retranslateUi(self, Libre_Tx):
        _translate = QtCore.QCoreApplication.translate
        Libre_Tx.setWindowTitle(_translate("Libre_Tx", "Libre Tx"))
        self.txinamounts_label.setText(_translate("Libre_Tx", "Txin Amounts"))
        self.scriptpubkey_label.setText(_translate("Libre_Tx", "Script pubkeys"))
        self.outputformat_label.setText(_translate("Libre_Tx", "Output Address Format"))
        self.privkeyformat_label.setText(_translate("Libre_Tx", "Priv Key Format"))
        self.tx_type1_label.setText(_translate("Libre_Tx", "Tx Type"))
        self.sequence_label.setText(_translate("Libre_Tx", "Sequence"))
        self.locktime_button.setText(_translate("Libre_Tx", "Convert L-Time"))
        self.amounts_label.setText(_translate("Libre_Tx", "Amounts"))
        self.txins_label.setText(_translate("Libre_Tx", "Txins TXID\'s"))
        self.privkey_label.setText(_translate("Libre_Tx", "Priv Keys"))
        self.inputindex_label.setText(_translate("Libre_Tx", "Input Index"))
        self.signed_button.setText(_translate("Libre_Tx", "Create Signed"))
        self.pubouts_label.setText(_translate("Libre_Tx", "Script pub outs"))
        self.currentblock_label.setText(_translate("Libre_Tx", "Block hgt/UNIX Time"))
        self.numins_label.setText(_translate("Libre_Tx", "Num Ins"))
        self.hashtype_label.setText(_translate("Libre_Tx", "Hash type"))
        self.signtx_label.setText(_translate("Libre_Tx", "Sign Tx"))
        self.nlocktime_label.setText(_translate("Libre_Tx", "N-locktime"))
        self.numouts_label.setText(_translate("Libre_Tx", "Num Outs"))
        self.version_label.setText(_translate("Libre_Tx", "Version"))


segwit_flag='0001'




class tx_data_obj:

    def __init__(self, outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs, num_ins_by_index):
        self.outs=outs
        self.tx_selection_types=tx_selection_types
        self.segwitprefix=segwitprefix
        self.legacy_prefix=legacy_prefix
        self.tx_inputs=tx_inputs
        self.input_secrets=input_secrets
        self.script_pubs=script_pubs
        self.segwit_input_infos=segwit_input_infos
        self.select_inputs=select_inputs
        self.num_ins_by_index=num_ins_by_index




    
def tx_data():
    outs=[ui.scriptout1_box.text(),ui.scriptout2_box.text(),ui.scriptout3_box.text(),ui.scriptout4_box.text(),ui.scriptout5_box.text(),ui.scriptout6_box.text()] 
    if ui.outputformat_combobox.currentText()=='Address':
        outs_list=address_to_scriptpub(outs)
        outs=outs_list
    tx_selection_types=[ui.txtype_combobox_1.currentText(), ui.txtype_combobox_2.currentText(), ui.txtype_combobox_3.currentText(), ui.txtype_combobox_4.currentText(), ui.txtype_combobox_5.currentText(), ui.txtype_combobox_6.currentText()]
    segwitprefix=[ui.version_box.text(),segwit_flag,ui.numins_combo.currentText()]
    legacy_prefix=[ui.version_box.text(),ui.numins_combo.currentText()]
    tx_inputs=[[txid_endian(ui.txin1_box.text()), format_input_index(ui.inputindex1_box.text()),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), format_input_index(ui.inputindex2_box.text()),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), format_input_index(ui.inputindex3_box.text()),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), format_input_index(ui.inputindex4_box.text()),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), format_input_index(ui.inputindex5_box.text()),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), format_input_index(ui.inputindex6_box.text()),ui.sequence6_box.text()]]
    input_secrets=[ui.privkey1_box.text(),ui.privkey2_box.text(),ui.privkey3_box.text(),ui.privkey4_box.text(),ui.privkey5_box.text(),ui.privkey6_box.text()]
    script_pubs=[ui.scriptpub1_box.text(), ui.scriptpub2_box.text(), ui.scriptpub3_box.text(), ui.scriptpub4_box.text(),ui.scriptpub5_box.text(), ui.scriptpub6_box.text()]
    segwit_input_infos=[[txid_endian(ui.txin1_box.text())+format_input_index(ui.inputindex1_box.text())+ui.scriptpub1_box.text()+amount_to_txhex(ui.txinamount_box1.text())+ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text())+format_input_index(ui.inputindex2_box.text())+ui.scriptpub2_box.text()+amount_to_txhex(ui.txinamount_box2.text())+ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text())+format_input_index(ui.inputindex3_box.text())+ui.scriptpub3_box.text()+amount_to_txhex(ui.txinamount_box3.text())+ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text())+format_input_index(ui.inputindex4_box.text())+ui.scriptpub4_box.text()+amount_to_txhex(ui.txinamount_box4.text())+ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text())+format_input_index(ui.inputindex5_box.text())+ui.scriptpub5_box.text()+amount_to_txhex(ui.txinamount_box5.text())+ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text())+format_input_index(ui.inputindex6_box.text())+ui.scriptpub6_box.text()+amount_to_txhex(ui.txinamount_box6.text())+ui.sequence6_box.text()]]
    select_inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    num_ins_by_index=[format_input_index(ui.inputindex1_box.text()),format_input_index(ui.inputindex2_box.text()),format_input_index(ui.inputindex3_box.text()),format_input_index(ui.inputindex4_box.text()),format_input_index(ui.inputindex5_box.text()),format_input_index(ui.inputindex6_box.text())]
    return tx_data_obj(outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs, num_ins_by_index)


def ok_button(rawtx=False):
    gui_data=tx_data()
    witness_program=[]
    all_inputs=[]
    outs=gui_data.outs
    tx_selections_raw=list(gui_data.tx_selection_types)
    tx_selections=[item for item in tx_selections_raw if item != 'N/A']
    is_segwit=[i for i in tx_selections if i in ('P2SH-P2wPKH','P2WPKH', 'P2WSH', 'P2WSH multisig')]
    count=0
    for item in tx_selections:
        if item == 'P2PKH':
            try:
                result= join_info('public_point', count) 
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 749')
                return
            data= gui_data.tx_inputs[count] 
            data.insert(2,result)
            all_inputs.append(data)
            if is_segwit:
                witness_program.append('00')
            count+=1
        elif item== 'P2SH':
            try:
                result= join_info('p2sh_redeemscript', count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 762')
                return          
            data= gui_data.tx_inputs[count] 
            data.insert(2,result)
            all_inputs.append(data)
            if is_segwit:
                witness_program.append('00')
            count+=1
        elif item == 'P2SH-P2wPKH':
            try:
                result=join_segwit('public_point', count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 775')
                return
            witness_program.append('02')
            witness_program.append(result)
            data= gui_data.tx_inputs[count] 
            data.insert(2,'171600'+(gui_data.script_pubs[count])[6:-4])
            all_inputs.append(data)
            count+=1
        elif item == 'P2WPKH':
            try:
                result=join_segwit('public_point', count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('error line 934')
                return
            witness_program.append('02')
            witness_program.append(result)
            data= gui_data.tx_inputs[count] 
            data.insert(2,'00')
            all_inputs.append(data)
            count+=1
        elif item == 'P2WSH': 
            try:
                result=join_segwit('redeemscript', count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('error line 951')
                return
            witness_program.append('02')
            witness_program.append(result)
            data= gui_data.tx_inputs[count] 
            data.insert(2,'00')
            all_inputs.append(data)
            count+=1
        elif item == 'P2SH multisig':
            try:
                result= join_info('multisig_redeemscript', count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 814')
                return
            data= gui_data.tx_inputs[count] 
            data.insert(2,result)
            all_inputs.append(data)
            if is_segwit:
                witness_program.append('00')
            count+=1
        elif item == 'P2WSH multisig': 
            try:
                result= join_segwit('multisig_redeemscript', count)
                split_keys=gui_data.input_secrets[count].split(',')
                wit_items=(len(split_keys)+2).to_bytes(1, byteorder='little').hex()
                end_result='00'+result
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 830')
                return
            witness_program.append(wit_items)
            witness_program.append(end_result)
            data= gui_data.tx_inputs[count] 
            data.insert(2,'00')
            all_inputs.append(data)            
            count+=1
    try:
        outputs=[ui.numouts_combo.currentText(), amount_to_txhex(ui.amount1_box.text()),outs[0], amount_to_txhex(ui.amount2_box.text()),outs[1], amount_to_txhex(ui.amount3_box.text()),outs[2], amount_to_txhex(ui.amount4_box.text()),outs[3], amount_to_txhex(ui.amount5_box.text()),outs[4], amount_to_txhex(ui.amount6_box.text()),outs[5],ui.nlocktime_box.text()]
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again4')
        print('ERROR ~ LINE 842')
        return
    if witness_program:
        prefix=gui_data.segwitprefix
        sz4_outs="".join([ui.numouts_combo.currentText(), amount_to_txhex(ui.amount1_box.text()),outs[0], amount_to_txhex(ui.amount2_box.text()),outs[1], amount_to_txhex(ui.amount3_box.text()),outs[2], amount_to_txhex(ui.amount4_box.text()),outs[3], amount_to_txhex(ui.amount5_box.text()),outs[4], amount_to_txhex(ui.amount6_box.text()),outs[5],ui.nlocktime_box.text()])
    else:     
        prefix=gui_data.legacy_prefix
    combined_inputs=[y for x in all_inputs for y in x]
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    signed_items=[(item) for item in input_info if item != ""]
    try:
        signed_tx="".join(signed_items)
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 857')
        return
    if witness_program:
        sz4_items=[gui_data.segwitprefix[0]+ gui_data.segwitprefix[2]+"".join(combined_inputs)+sz4_outs]
        sz1_items=gui_data.segwitprefix[1]+"".join(witness_program)
        sz4_values="".join(sz4_items)
        sz1_values="".join(sz1_items)
        format_output('segwit',prefix, all_inputs, outputs,sz4_values, sz1_values, witness_program)
    elif not witness_program:
        format_output('legacy',prefix, all_inputs, outputs)
    return signed_tx


def join_info(s_value, index):
    gui_data=tx_data()
    tx_selections=gui_data.tx_selection_types
    outs=gui_data.outs
    scriptpubs=gui_data.script_pubs
    prefix=gui_data.legacy_prefix
    inputs=gui_data.tx_inputs
    outputs=[ui.numouts_combo.currentText(),amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5],ui.nlocktime_box.text(),ui.hashtype_box.text()]
    inputs[index].insert(2, scriptpubs[index])
    num_ins=list(range(0, int(ui.numins_combo.currentText())))
    other_indexes=[value for value in num_ins if value != index]
    for num in other_indexes:
        inputs[num].insert(2, '00')
    combined_inputs=[y for x in inputs for y in x]
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    input_list=[(item) for item in input_info if item != ""]
    rawtx="".join(input_list)
    if s_value=='none':
        dersig=sign_tx(rawtx, index, s_value)
    elif s_value =='multisig_redeemscript':
        dersig=sign_tx(rawtx, index, s_value)
    elif s_value =='p2sh_redeemscript': 
        dersig=sign_tx(rawtx, index, s_value)
    elif s_value == 'rawtx':
        ui.output_box.setText(rawtx)
        return rawtx
    else:
        dersig=sign_tx(rawtx, index)
    return dersig


def join_segwit(s_value, index):
    gui_data=tx_data()
    tx_selections=gui_data.tx_selection_types
    outs=gui_data.outs
    scriptpubs=gui_data.script_pubs
    input_infos=gui_data.segwit_input_infos
    this_tx_input_infos="".join(input_infos[index])
    try:
        hash_outs=hash256(bytes.fromhex(amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5]))
        
        hash_ins=hash256(bytes.fromhex(txid_endian(ui.txin1_box.text())+format_input_index(ui.inputindex1_box.text())+txid_endian(ui.txin2_box.text())+format_input_index(ui.inputindex2_box.text())+txid_endian(ui.txin3_box.text())+format_input_index(ui.inputindex3_box.text())+txid_endian(ui.txin4_box.text())+format_input_index(ui.inputindex4_box.text())+txid_endian(ui.txin5_box.text())+format_input_index(ui.inputindex5_box.text())+txid_endian(ui.txin6_box.text())+format_input_index(ui.inputindex6_box.text())))
    
        hash_sequence=hash256(bytes.fromhex(ui.sequence1_box.text())+bytes.fromhex(ui.sequence2_box.text())+bytes.fromhex(ui.sequence3_box.text())+bytes.fromhex(ui.sequence4_box.text())+bytes.fromhex(ui.sequence5_box.text())+bytes.fromhex(ui.sequence6_box.text()))
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 917')
        return
    input_info=[ui.version_box.text(), hash_ins.hex(),hash_sequence.hex(),this_tx_input_infos, hash_outs.hex(),ui.nlocktime_box.text(), ui.hashtype_box.text()]
    input_list=[(item) for item in input_info if item != ""]
    rawtx="".join(input_list)
    if s_value =='redeemscript':
        dersig=sign_tx(rawtx, index, s_value)
    elif s_value=='none':
        dersig=sign_tx(rawtx, index, s_value)
    elif s_value =='multisig_redeemscript':
        dersig=sign_tx(rawtx, index, 'redeemscript')
    elif s_value == 'public_point':
        dersig=sign_tx(rawtx, index)[2:]
    elif s_value == 'rawtx':
        ui.output_box.setText(rawtx)
        return rawtx
    return dersig


def sign_tx(rawtx, index, s_value='public_point'):
    gui_data=tx_data()
    script_pubs=gui_data.script_pubs
    try:
        unsignedtx=bytes.fromhex(rawtx)
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 943')
        return
    unsigned_tx_hash = hash256(unsignedtx)
    input_secrets=gui_data.input_secrets
    if gui_data.tx_selection_types[index] in ('P2SH multisig', 'P2WSH multisig'):
        signature_list=[]
        split_keys=input_secrets[index].split(',')
        keys_sans_whitespace=[item.strip(" ") for item in split_keys]
        for key in keys_sans_whitespace:
            selection=ui.privkey_comboBox.currentText()
            if selection=='WIF':
                 input_secret=scalar_from_wif(key)
            if selection == 'Hex':
                input_secret=scalar_from_hex(key)
            if selection == 'Scalar':
                input_secret=int(key)
            private_key = PrivateKey(input_secret)
            public_key_bytes = private_key.point.sec(compressed=True)
            signature = private_key.sign(int.from_bytes(unsigned_tx_hash, byteorder='big'))
            signature_bytes=signature.der() + bytes.fromhex(ui.hashtype_box.text()[:2])
            signature_bytes_and_length=bytes([len(signature_bytes)])+signature_bytes
            signature_list.append(signature_bytes_and_length.hex())
        signature_joined="".join(signature_list)
        signature_bytes=bytes.fromhex(signature_joined)
    else:
        selection=ui.privkey_comboBox.currentIndex()
        if selection==0:
             input_secret=scalar_from_wif(input_secrets[index])
        if ui.privkey_comboBox.currentIndex()==1:
            input_secret=scalar_from_hex(input_secrets[index])
        if ui.privkey_comboBox.currentIndex()==2:
            input_secret=int(input_secrets[index])
        private_key = PrivateKey(input_secret)
        public_key_bytes = private_key.point.sec(compressed=True)
        signature = private_key.sign(int.from_bytes(unsigned_tx_hash, byteorder='big'))
        der_sig=signature.der() + bytes.fromhex(ui.hashtype_box.text()[:2])
        signature_bytes=bytes([len(der_sig)])+der_sig
    if s_value=='none':
        dersig_full = signature_bytes
    elif s_value=="multisig_redeemscript":
        dersig_s=bytes.fromhex(script_pubs[index])
        tx_selections=list(gui_data.tx_selection_types)
        if len(dersig_s.hex())>133070:
            dersig_pre=b'\x00'+signature_bytes+b'\x4E'+dersig_s[1:]
            dersig_full=len_in_hex(dersig_pre)+dersig_pre
        elif len(dersig_s.hex())>510:
            dersig_pre=b'\x00'+signature_bytes+b'\x4D'+dersig_s[1:]
            dersig_full=len_in_hex(dersig_pre)+dersig_pre
        elif len(dersig_s.hex())>504:
            dersig_pre=b'\x00'+signature_bytes+b'\x4C'+dersig_s[1:]
            dersig_full=len_in_hex(dersig_pre)+dersig_pre
        elif len(dersig_s.hex())>152:
            dersig_pre=b'\x00'+signature_bytes+b'\x4C'+dersig_s
            dersig_full=len_in_hex(dersig_pre)+dersig_pre
        else:
            dersig_pre=b'\x00'+signature_bytes+dersig_s
            dersig_full=len_in_hex(dersig_pre)+dersig_pre
    elif s_value=='p2sh_redeemscript':
        dersig_s=bytes.fromhex(script_pubs[index])
        dersig_full=bytes([len(signature_bytes+dersig_s)])+signature_bytes+dersig_s
    elif s_value=='redeemscript':
        dersig_s=bytes.fromhex(script_pubs[index])
        dersig_full=signature_bytes+dersig_s
    elif s_value=='redeemscript':
        dersig_s=bytes.fromhex(script_pubs[index])
        dersig_full=signature_bytes+dersig_s
    elif s_value== 'public_point':
        dersig_point=private_key.point.sec()
        dersig_s=bytes([len(dersig_point)])+dersig_point
        dersig=signature_bytes+dersig_s
        dersig_full=bytes([len(dersig)])+dersig
    return dersig_full.hex()


def amount_to_txhex(amount):
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


def scalar_from_wif(priv_key):
    num = 0
    for c in priv_key.encode('ascii'):
        num *= 58
        num += BASE58.index(c)
    hex_secret=hex(num)[2:]
    try:
        combined = bytes.fromhex(hex_secret)
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 1046')
        return
    checksum = combined[-4:]
    if hash256(combined[:-4])[:4] != checksum:
        raise RuntimeError('bad address: {} {}'.format(checksum, hash256(combined)[:4]))
    hex_secret_trimmed=codecs.encode(combined[1:-5], 'hex')
    hex_secret_trimmed_str=hex_secret_trimmed.decode("utf-8")
    return int(hex_secret_trimmed_str, 16)


def scalar_from_hex(hexstring):
    return int(hexstring, 16)


def address_to_scriptpub(outs):
    scriptpub_list=[]
    for item in outs:
        if item[:2]=='tb':
            hex_chars=decode(item[:2], item)[1]
            hex_chars_list=[]
            for i in hex_chars:
                hex_chars_list.append(bytes([i]).hex())
                h256="".join(hex_chars_list)
            h256len=str(int((int(bytes([len(h256)]).hex())/2)))
            scriptpub_raw='00'+h256len+h256
            scriptpub=bytes([len(bytes.fromhex(scriptpub_raw))]).hex()+scriptpub_raw
        if item[:2]=='bc':
            hex_chars=decode(item[:2], item)[1]
            hex_chars_list=[]
            for i in hex_chars:
                hex_chars_list.append(bytes([i]).hex())
                h256="".join(hex_chars_list)
            h256len=str(int((int(bytes([len(h256)]).hex())/2)))
            scriptpub_raw='00'+h256len+h256
            scriptpub=bytes([len(bytes.fromhex(scriptpub_raw))]).hex()+scriptpub_raw
        if item[:1]=='3':
            scriptpub='17a914'+decode_base58(item).hex()+'87'
        if item[:1]=='2':
            scriptpub='17a914'+decode_base58(item).hex()+'87'
        if item[:1]=='m':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 1090')
                return
        if item[:1]=='n':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 1097')
                return
        if item[:1]=='1':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                print('ERROR LINE 1104')
                return
        if item=='':
            scriptpub=''
        scriptpub_list.append(scriptpub)
    return scriptpub_list


def int_to_nlocktime():
    try:
        block=int(ui.currentblock_box.text())
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR LINE 1117')
        return
    block_hex=bytes(reversed(block.to_bytes(4, 'big')))
    ui.nlocktime_box.setText(block_hex.hex())
    return block_hex


def len_in_hex(item):
    length=len(item)
    if length > 4294967295:
        return b'\xFF' + (length).to_bytes(8, byteorder='little')
    elif length > 65535:
        return b'\xFE' + (length).to_bytes(4, byteorder='little')
    elif length > 252:
        return b'\xFD'+(length).to_bytes(2, byteorder='little')
    else:
        return length.to_bytes(1, byteorder='little')

def format_input_index(input_idx):
    if input_idx == "":
        return input_idx
    return struct.pack("<l", int(input_idx)).hex()


def tx_select_func(index):
    inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    selection=inputs[index-1].currentText()
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
        i[7].setDisabled(True)
    elif selection=='P2PKH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    elif selection=='P2SH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    elif selection=='P2SH multisig':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    else:
        i=boxes[index-1]
        i[0].setDisabled(False)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    return selection


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


def colourize(text, colour):
    colourmap={'brown': '#de8d00', 'black':'#f000000', 'red':'#ff0000' , 'blue':'#0062ff', 'pink':'#ffa3a3', 'yellow':'#a3a600', 'aqua':'#00dec0', 'green':'#007d00', 'orange':'#ff8400', 'drkbrown':'#996633', 'purple':'#9900ff'}
    return"".join("<span style=\" font-size:12pt; font-weight:600; color:"+colourmap[colour]+";\" >"+text+"</span>")


def format_output(tx_type, prefix, tx_inputs, outputs2, sz4_values=None, sz1_values=None, witness_program=None):
    outputs=[(item) for item in outputs2 if item != ""]
    combined_inputs=[y for x in tx_inputs for y in x if x != ""]
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    signed_items=[(item) for item in input_info if item != ""]
    tx_data=''.join(signed_items)
    tx_size=len(bytes.fromhex(tx_data))
    edu_mode_output=[colourize('VERSION', 'brown'),  '-', colourize('SEGWIT FLAG', 'black'),'-', colourize('NUM INS', 'red'), '-', colourize('TXID', 'blue'), '-', colourize('PREV INDEX', 'pink'), '-', colourize('SCRIPT SIG', 'yellow'), '-', colourize('SEQUENCE', 'aqua'), '-', colourize('NUM OUTS', 'red'), '-', colourize('AMOUNT', 'green'), '-', colourize('SCRIPT PUBKEY', 'orange') , '-', colourize('WITNESS ITEMS', 'purple'), '-', colourize('WITNESS PROG', 'drkbrown'), '-', colourize('LOCKTIME', 'black'), '<br>', '<br>']    
    if tx_type=='segwit':
        tx_id=bytes(reversed(hash256(bytes.fromhex(sz4_values)))).hex()
        tx_id_output=colourize(('TX ID='+str(tx_id)+'<br>'), 'black')
        edu_mode_output.append(tx_id_output)
        size_data=colourize(('TX SIZE='+str(len(bytes.fromhex(sz4_values)))+' BYTES'+ '<br>'), 'black')


        edu_mode_output.append(size_data)
        tx_weight=(len(bytes.fromhex(sz4_values))*4)+len(bytes.fromhex(sz1_values))
        weight_data=colourize(('TX WEIGHT='+str(tx_weight)+' BYTES'+ '<br>'), 'black')
        edu_mode_output.append(weight_data)
        virt_size=colourize(('VIRTUAL SIZE='+str(int(tx_weight/4))+' BYTES'+ '<br>'), 'black')
        edu_mode_output.append(virt_size)
    else:
        tx_id=bytes(reversed(hash256(bytes.fromhex(tx_data)))).hex()
        tx_id_output=colourize(('TX ID='+str(tx_id)+'<br>'), 'black')
        edu_mode_output.append(tx_id_output)
        size_data=colourize(('TX SIZE='+str(tx_size)+' BYTES'+ '<br>'), 'black')
        edu_mode_output.append(size_data)

    if tx_type=='segwit':
        prefix[0]=colourize(prefix[0],'brown')
        prefix[1]=colourize(prefix[1],'black')
        prefix[2]=colourize(prefix[2],'red')

    elif tx_type=='legacy':
        prefix[0]=colourize(prefix[0], 'brown')
        prefix[1]=colourize(prefix[1], 'red')
    for item in tx_inputs:
        try:
            item[3]=colourize(item[3], 'aqua')
            item[0]=colourize(item[0], 'blue')
            item[1]=colourize(item[1], 'pink')
            item[2]=colourize(item[2], 'yellow')
        except IndexError:
            pass
    combined_inputs=[y for x in tx_inputs for y in x if x != ""]
    outputs[0]=colourize(outputs[0], 'red')
    outputs[-1]=colourize(outputs[-1], 'black')
    if tx_type=='segwit':
        wit_counter=1
        indexes=1
        for item in witness_program:
            if item =='00':
                witness_program[indexes-1]=colourize(item, 'purple')

            else:
                if wit_counter %2==0:
                    witness_program[indexes-1]=colourize(item, 'drkbrown')
                    wit_counter+=1
                else:
                    witness_program[indexes-1]=colourize(item, 'purple')
                    wit_counter+=1
            indexes+=1
        outputs.insert(len(outputs)-1, "".join(witness_program))
        outputs[-1]=colourize(outputs[-1], 'black')
        new_list=outputs[1:-1]
        outs_counter=1
        for item in range(1, len(new_list)+1):

            if outs_counter %2==0:
                outputs[item]=colourize(outputs[item], 'orange')
            else:
                outputs[item]=colourize(outputs[item], 'green')
            outs_counter+=1
    elif tx_type=='legacy':
        counter=1
        new_list=outputs[1:-1]
        for item in range(1, len(new_list)+1):
            if counter %2==0:
                outputs[item]=colourize(outputs[item], 'orange')
            else:
                outputs[item]=colourize(outputs[item], 'green')
            counter+=1
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    signed_items=[(item) for item in input_info if item != ""]
    for item in signed_items:
        try:
            edu_mode_output.append(item)
        except TypeError:
            print('ERROR - LINE 1296')
    try:
        signed_tx="".join(edu_mode_output)
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR - LINE 1301')

    edu_mode_print="".join(prefix+combined_inputs+outputs)
    ui.output_box.setText(signed_tx)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('libre_tx_icon.png'))
    splash_pix = QPixmap('splash.png')
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()


    Libre_Tx = QtWidgets.QDialog()
    ui = Ui_Libre_Tx()
    ui.setupUi(Libre_Tx)
    time.sleep(3)
    Libre_Tx.show()
    splash.finish(Libre_Tx)
    sys.exit(app.exec_())
    