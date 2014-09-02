# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/about.ui'
#
# Created: Tue Sep  2 21:59:25 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(292, 154)
        self.picture = QtGui.QLabel(About)
        self.picture.setGeometry(QtCore.QRect(20, 50, 81, 81))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(":/image/walkman.png"))
        self.picture.setObjectName("picture")
        self.nickname = QtGui.QLabel(About)
        self.nickname.setGeometry(QtCore.QRect(110, 110, 151, 16))
        self.nickname.setObjectName("nickname")
        self.email = QtGui.QLabel(About)
        self.email.setGeometry(QtCore.QRect(140, 80, 140, 16))
        self.email.setTextFormat(QtCore.Qt.RichText)
        self.email.setOpenExternalLinks(True)
        self.email.setObjectName("email")
        self.website = QtGui.QLabel(About)
        self.website.setGeometry(QtCore.QRect(140, 50, 140, 16))
        self.website.setTextFormat(QtCore.Qt.RichText)
        self.website.setOpenExternalLinks(True)
        self.website.setObjectName("website")
        self.icon1 = QtGui.QLabel(About)
        self.icon1.setGeometry(QtCore.QRect(110, 50, 21, 21))
        font = QtGui.QFont()
        font.setFamily("General Foundicons")
        font.setPointSize(18)
        self.icon1.setFont(font)
        self.icon1.setObjectName("icon1")
        self.icon2 = QtGui.QLabel(About)
        self.icon2.setGeometry(QtCore.QRect(110, 80, 21, 21))
        font = QtGui.QFont()
        font.setFamily("General Foundicons")
        font.setPointSize(18)
        self.icon2.setFont(font)
        self.icon2.setObjectName("icon2")
        self.program = QtGui.QLabel(About)
        self.program.setGeometry(QtCore.QRect(20, 20, 251, 16))
        self.program.setAlignment(QtCore.Qt.AlignCenter)
        self.program.setObjectName("program")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.nickname.setText(QtGui.QApplication.translate("About", "Kiss György (Walkman)", None, QtGui.QApplication.UnicodeUTF8))
        self.email.setText(QtGui.QApplication.translate("About", "<html><head/><body><p><a href=\"mailto:kissgyorgy@me.com?subject=Program: Munkabeosztas\"><span style=\" text-decoration: underline; color:#0000ff;\">kissgyorgy@me.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.website.setText(QtGui.QApplication.translate("About", "<html><head/><body><p><a href=\"http://kissgyorgy.me\"><span style=\" text-decoration: underline; color:#0000ff;\">http://kissgyorgy.me</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.icon1.setText(QtGui.QApplication.translate("About", "", None, QtGui.QApplication.UnicodeUTF8))
        self.icon2.setText(QtGui.QApplication.translate("About", "", None, QtGui.QApplication.UnicodeUTF8))
        self.program.setText(QtGui.QApplication.translate("About", "Womanager v1.0", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
