# -*- coding: utf-8 -*-

# DForm implementation generated from reading ui file 'deny.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DForm(object):
    def setupUi(self, DForm):
        DForm.setObjectName("DForm")
        DForm.resize(256, 30)
        self.textBrowser = QtWidgets.QTextBrowser(DForm)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 256, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DForm)
        QtCore.QMetaObject.connectSlotsByName(DForm)

    def retranslateUi(self, DForm):
        _translate = QtCore.QCoreApplication.translate
        DForm.setWindowTitle(_translate("DForm", "DForm"))
        self.textBrowser.setHtml(_translate("DForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">В доступе отказано</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DForm = QtWidgets.QWidget()
    ui = Ui_DForm()
    ui.setupUi(DForm)
    DForm.show()
    sys.exit(app.exec_())
