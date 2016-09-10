# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word_quiz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class WUi_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 301)
        Form.setMinimumSize(QtCore.QSize(761, 301))
        Form.setMaximumSize(QtCore.QSize(761, 301))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resim/logo_wq.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 20, 701, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.word_quiz = QtWidgets.QLabel(self.frame)
        self.word_quiz.setGeometry(QtCore.QRect(0, 0, 651, 211))
        self.word_quiz.setText("")
        self.word_quiz.setPixmap(QtGui.QPixmap(":/resim/WordQuiz/word_quiz.png"))
        self.word_quiz.setObjectName("word_quiz")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 210, 701, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.basla = QtWidgets.QPushButton(self.frame_2)
        self.basla.setGeometry(QtCore.QRect(10, 10, 141, 34))
        self.basla.setObjectName("basla")
        self.bilgi = QtWidgets.QLabel(self.frame_2)
        self.bilgi.setGeometry(QtCore.QRect(160, 10, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(8)
        self.bilgi.setFont(font)
        self.bilgi.setObjectName("bilgi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Word Quiz"))
        self.basla.setText(_translate("Form", "Başla!"))
        self.bilgi.setText(_translate("Form", "İngilizcenizi geliştirmek mi istiyorsunuz? O zaman Word Quiz tam size göre!"))
