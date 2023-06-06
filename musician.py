import pymongo
import datetime
from fpdf import FPDF
db_client = pymongo.MongoClient("mongodb://mongo:pnMPibl9MybIhP32sg7r@containers-us-west-207.railway.app:6059/")
current_db = db_client["MusicService"]
collection = current_db["musician"]
from PyQt5 import QtCore, QtGui, QtWidgets
table = 0
class Ui_MForm(object):
    def setupUi(self, MForm):
        MForm.setObjectName("Form")
        MForm.resize(1200, 800)
        self.tableWidget = QtWidgets.QTableWidget(MForm)
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
        self.pushButton = QtWidgets.QPushButton(MForm)
        self.pushButton.setGeometry(QtCore.QRect(10, 760, 75, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MForm)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 760, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MForm)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 760, 75, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MForm)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 760, 75, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(MForm)
        self.pushButton_5.setGeometry(QtCore.QRect(960, 760, 75, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MForm)
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 760, 75, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(MForm)
        self.pushButton_7.setGeometry(QtCore.QRect(1120, 760, 75, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(MForm)
        self.pushButton_8.setGeometry(QtCore.QRect(880, 760, 75, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.retranslateUi(MForm)
        QtCore.QMetaObject.connectSlotsByName(MForm)
        self.pushButton.clicked.connect(self.MT)
        self.pushButton_2.clicked.connect(self.AT)
        self.pushButton_3.clicked.connect(self.ST)
        self.pushButton_5.clicked.connect(self.insert)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.update)
        self.pushButton_4.clicked.connect(self.PDT)
        self.pushButton_8.clicked.connect(self.letter)
    def insert(self):
        match table:
            case 1:
                collection = current_db["musician"]
                new = {
                    "name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                    "monthly_listeners": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "genre": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                }
                collection.insert_one(new)
                self.MT()
            case 2:
                collection = current_db["album"]
                new = {
                    "album_name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                    "album_duration": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "album_release_date": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),

                }
                collection.insert_one(new)
                self.AT()
            case 3:
                collection = current_db["song"]
                new = {
                    "song_name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                    "song_duration": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "played": int(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()),

                }
                collection.insert_one(new)
                self.ST()
            case 4:
                collection = current_db["personal_data"]
                new = {
                    "mail_adress": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                    "surname": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "password": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),

                }
                collection.insert_one(new)
                self.PDT()

    def delete(self):
        currentitem = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        match table:
            case 1:
                collection = current_db["musician"]
                collection.delete_one({"name": str(currentitem)})
                self.MT()
            case 2:
                collection = current_db["album"]
                collection.delete_one({"album_name": int(currentitem)})
                self.AT()
            case 3:
                collection = current_db["song"]
                collection.delete_one({"song_name": int(currentitem)})
                self.ST()
            case 4:
                collection = current_db["personal_data"]
                collection.delete_one({"mail_adress": int(currentitem)})
                self.PDT()

    def update(self):
        currentitem = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        match table:
            case 1:
                collection = current_db["musician"]
                collection.update_many({"name": str(currentitem)}, {
                        "$set": {"name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                                 "monthly_listeners": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                                 "genre": self.tableWidget.item(self.tableWidget.currentRow(), 2).text()}})
                self.MT()
            case 2:
                collection = current_db["album"]
                collection.update_many({"album_name": str(currentitem)}, {
                        "$set": {"album_name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                                 "album_duration": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                                 "album_release_date": self.tableWidget.item(self.tableWidget.currentRow(), 2).text()}})
                self.AT()
            case 3:
                collection = current_db["song"]
                collection.update_many({"song_name": str(currentitem)}, {
                        "$set": {"song_name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                                 "song_duration": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                                 "played": int(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())}})
                self.ST()
            case 4:
                collection = current_db["personal_data"]
                collection.update_many({"mail_adress": str(currentitem)}, {
                        "$set": {"mail_adress": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                                 "surname": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                                 "password": self.tableWidget.item(self.tableWidget.currentRow(), 2).text()}})
                self.PDT()

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
    def PDT(self):
        global table
        table = 4
        self.chose()
        collection = current_db["personal_data"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(360)
        row = 0
        for personal_data in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(personal_data["mail_adress"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(personal_data["surname"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(personal_data["password"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def letter(self):
        currentitem = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        match table:
            case 4:
             collection = current_db["personal_data"]
             pdf = FPDF('P', 'mm', 'Letter')
             pdf.add_page()
             pdf.set_font('helvetica', '', 16)
             pdf.cell(14, 10, 'Dear')
             pdf.cell(0, 10, currentitem, ln=True)
             pdf.cell(50, 20, 'It seems that you like our app! We would appreciate if you left a review.', ln=True)
             pdf.cell(50, 10, 'From', ln=True)
             pdf.cell(50,10, 'XYZ Team', ln=True)
             pdf.output('letter.pdf')


    def chose(self):
        _translate = QtCore.QCoreApplication.translate
        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)

        match table:
            case 1:
                item_0.setText(_translate("MForm", "Исполнитель"))
                item_1.setText(_translate("MForm", "Кол-во слушателей"))
                item_2.setText(_translate("MForm", "Жанры"))

            case 2:
                item_0.setText(_translate("MForm", "Альбом"))
                item_1.setText(_translate("MForm", "Длительность"))
                item_2.setText(_translate("MForm", "Дата выхода"))

            case 3:
                item_0.setText(_translate("MForm", "Песня"))
                item_1.setText(_translate("MForm", "Длительность"))
                item_2.setText(_translate("MForm", "Кол-во прослушиваний"))
            case 4:
                item_0.setText(_translate("MForm", "Электронная почта"))
                item_1.setText(_translate("MForm", "Фамилия"))
                item_2.setText(_translate("MForm", "Пароль"))

    def retranslateUi(self, MForm):
        _translate = QtCore.QCoreApplication.translate
        MForm.setWindowTitle(_translate("MForm", "Окно администратора"))
        self.pushButton.setText(_translate("MForm", "Исполнители"))
        self.pushButton_2.setText(_translate("MForm", "Альбомы"))
        self.pushButton_3.setText(_translate("Form", "Песни"))
        self.pushButton_5.setText(_translate("MForm", "Вставить"))
        self.pushButton_6.setText(_translate("MForm", "Удалить"))
        self.pushButton_7.setText(_translate("MForm", "Изменить"))
        self.pushButton_4.setText(_translate("MForm", "Аккаунты"))
        self.pushButton_8.setText(_translate("MForm", "Письмо"))
        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)

