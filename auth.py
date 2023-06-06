from PyQt5 import QtCore, QtGui, QtWidgets
from musician import Ui_MForm
from deny import Ui_DForm

class Ui_AForm(object):
    def setupUi(self, AForm):
        AForm.setObjectName("AForm")
        AForm.resize(360, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(AForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LlineEdit = QtWidgets.QLineEdit(AForm)
        self.LlineEdit.setObjectName("LlineEdit")
        self.verticalLayout.addWidget(self.LlineEdit)
        self.PlineEdit = QtWidgets.QLineEdit(AForm)
        self.PlineEdit.setObjectName("PlineEdit")
        self.verticalLayout.addWidget(self.PlineEdit)
        self.pushButton = QtWidgets.QPushButton(AForm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(AForm)
        QtCore.QMetaObject.connectSlotsByName(AForm)

        self.pushButton.clicked.connect(self.reg)
    def reg(self):
        if (self.LlineEdit.text() == "ADM" and self.PlineEdit.text() == "123ADM321"):
            self.MForm = QtWidgets.QWidget()
            self.ui = Ui_MForm()
            self.ui.setupUi(self.MForm)
            self.MForm.show()
        else:
            self.DForm = QtWidgets.QWidget()
            self.ui = Ui_DForm()
            self.ui.setupUi(self.DForm)
            self.DForm.show()


    def retranslateUi(self, AForm):
        _translate = QtCore.QCoreApplication.translate
        AForm.setWindowTitle(_translate("AForm", "Авторизация"))
        self.pushButton.setText(_translate("AForm", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AForm = QtWidgets.QWidget()
    ui = Ui_AForm()
    ui.setupUi(AForm)
    AForm.show()
    sys.exit(app.exec_())
