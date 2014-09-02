# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Thu Oct 10 20:12:29 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(292, 154)
        self.picture = QtGui.QLabel(About)
        self.picture.setGeometry(QtCore.QRect(20, 50, 81, 81))
        self.picture.setText(_fromUtf8(""))
        self.picture.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/walkman.png")))
        self.picture.setObjectName(_fromUtf8("picture"))
        self.nickname = QtGui.QLabel(About)
        self.nickname.setGeometry(QtCore.QRect(110, 110, 151, 16))
        self.nickname.setObjectName(_fromUtf8("nickname"))
        self.email = QtGui.QLabel(About)
        self.email.setGeometry(QtCore.QRect(140, 80, 140, 16))
        self.email.setTextFormat(QtCore.Qt.RichText)
        self.email.setOpenExternalLinks(True)
        self.email.setObjectName(_fromUtf8("email"))
        self.website = QtGui.QLabel(About)
        self.website.setGeometry(QtCore.QRect(140, 50, 140, 16))
        self.website.setTextFormat(QtCore.Qt.RichText)
        self.website.setOpenExternalLinks(True)
        self.website.setObjectName(_fromUtf8("website"))
        self.icon1 = QtGui.QLabel(About)
        self.icon1.setGeometry(QtCore.QRect(110, 50, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("General Foundicons"))
        font.setPointSize(18)
        self.icon1.setFont(font)
        self.icon1.setObjectName(_fromUtf8("icon1"))
        self.icon2 = QtGui.QLabel(About)
        self.icon2.setGeometry(QtCore.QRect(110, 80, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("General Foundicons"))
        font.setPointSize(18)
        self.icon2.setFont(font)
        self.icon2.setObjectName(_fromUtf8("icon2"))
        self.program = QtGui.QLabel(About)
        self.program.setGeometry(QtCore.QRect(20, 20, 251, 16))
        self.program.setAlignment(QtCore.Qt.AlignCenter)
        self.program.setObjectName(_fromUtf8("program"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.nickname.setText(_translate("About", "Kiss György (Walkman)", None))
        self.email.setText(_translate("About", "<html><head/><body><p><a href=\"mailto:kissgyorgy@me.com?subject=Program: Munkabeosztas\"><span style=\" text-decoration: underline; color:#0000ff;\">kissgyorgy@me.com</span></a></p></body></html>", None))
        self.website.setText(_translate("About", "<html><head/><body><p><a href=\"http://kissgyorgy.me\"><span style=\" text-decoration: underline; color:#0000ff;\">http://kissgyorgy.me</span></a></p></body></html>", None))
        self.icon1.setText(_translate("About", "", None))
        self.icon2.setText(_translate("About", "", None))
        self.program.setText(_translate("About", "Womanager v1.0", None))

import resources_rc
