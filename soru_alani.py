# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soru_alanı.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SUi_Form(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(581, 251)
        Form2.setMinimumSize(QtCore.QSize(491, 182))
        Form2.setMaximumSize(QtCore.QSize(345353, 345334))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resim/logo_wq.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form2.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 181, 221))
        self.groupBox.setObjectName("groupBox")
        self.kalan_kelime = QtWidgets.QLabel(self.groupBox)
        self.kalan_kelime.setGeometry(QtCore.QRect(20, 40, 131, 19))
        self.kalan_kelime.setObjectName("kalan_kelime")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 141, 121))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(Form2)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 10, 311, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.kelime = QtWidgets.QLabel(self.groupBox_2)
        self.kelime.setGeometry(QtCore.QRect(80, 50, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        self.kelime.setFont(font)
        self.kelime.setObjectName("kelime")
        self.anlam = QtWidgets.QLabel(self.groupBox_2)
        self.anlam.setGeometry(QtCore.QRect(20, 100, 68, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(9)
        self.anlam.setFont(font)
        self.anlam.setObjectName("anlam")
        self.verigirisi = QtWidgets.QLineEdit(self.groupBox_2)
        self.verigirisi.setGeometry(QtCore.QRect(80, 100, 211, 21))
        self.verigirisi.setObjectName("verigirisi")
        self.tamam = QtWidgets.QPushButton(self.groupBox_2)
        self.tamam.setGeometry(QtCore.QRect(80, 140, 211, 31))
        self.tamam.setObjectName("tamam")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form", "Word Quiz"))
        self.groupBox.setTitle(_translate("Form", "Durum"))
        self.kalan_kelime.setText(_translate("Form", "Kalan Kelime:{}".format(30)))
        self.groupBox_2.setTitle(_translate("Form", "Quiz"))
        self.kelime.setText(_translate("Form", "Kelime"))
        self.anlam.setText(_translate("Form", "Anlamı:"))
        self.tamam.setText(_translate("Form", "Tamam"))
