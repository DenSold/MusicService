import pymongo
import datetime
db_client = pymongo.MongoClient("mongodb://mongo:pnMPibl9MybIhP32sg7r@containers-us-west-207.railway.app:6059/")
current_db = db_client["MusicService"]
collection = current_db["musician"]
from PyQt5 import QtCore, QtGui, QtWidgets
table = 0
class Ui_UMForm(object):
    def setupUi(self, UMForm):
        UMForm.setObjectName("Form")
        UMForm.resize(1200, 800)
        self.tableWidget = QtWidgets.QTableWidget(UMForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1080, 750))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item_0 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item_0)
        item_1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item_1)
        item_2 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item_2)
        self.pushButton = QtWidgets.QPushButton(UMForm)
        self.pushButton.setGeometry(QtCore.QRect(10, 760, 75, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(UMForm)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 760, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(UMForm)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 760, 75, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(UMForm)
        QtCore.QMetaObject.connectSlotsByName(UMForm)
        self.pushButton.clicked.connect(self.MT)
        self.pushButton_2.clicked.connect(self.AT)
        self.pushButton_3.clicked.connect(self.ST)


    def MT(self):
        global table
        table = 1
        self.chose()
        collection = current_db["musician"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(360)
        row = 0
        for musician in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(musician["name"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(musician["monthly_listeners"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(musician["genre"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def AT(self):
        global table
        table = 2
        self.chose()
        collection = current_db["album"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(360)
        row = 0
        for album in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(album["album_name"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(album["album_duration"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(album["album_release_date"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def ST(self):
        global table
        table = 3
        self.chose()
        collection = current_db["song"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(360)
        row = 0
        for song in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(song["song_name"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(song["song_duration"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(song["played"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)

    def chose(self):
        _translate = QtCore.QCoreApplication.translate
        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)

        match table:
            case 1:
                item_0.setText(_translate("UMForm", "Исполнитель"))
                item_1.setText(_translate("UMForm", "Кол-во слушателей"))
                item_2.setText(_translate("MForm", "Жанры"))

            case 2:
                item_0.setText(_translate("UMForm", "Альбом"))
                item_1.setText(_translate("UMForm", "Длительность"))
                item_2.setText(_translate("UMForm", "Дата выхода"))

            case 3:
                item_0.setText(_translate("UMForm", "Песня"))
                item_1.setText(_translate("UMForm", "Длительность"))
                item_2.setText(_translate("UMForm", "Кол-во прослушиваний"))

    def retranslateUi(self, UMForm):
        _translate = QtCore.QCoreApplication.translate
        UMForm.setWindowTitle(_translate("UMForm", "Музыкальный сервис"))
        self.pushButton.setText(_translate("UMForm", "Исполнители"))
        self.pushButton_2.setText(_translate("UMForm", "Альбомы"))
        self.pushButton_3.setText(_translate("Form", "Песни"))

        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)

