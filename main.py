
import mysql.connector
from mysql.connector import Error
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox, QTableWidgetItem, QLineEdit, QComboBox, QLabel
from PyQt5.QtGui import QPixmap




class Main(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        super(Main,self).__init__()
        loadUi("list.ui",self)
        self.Message_Box = Message_UI()
        self.ClaimButton.clicked.connect(self.claimer)
        self.ClaimButton.clicked.connect(lambda: self.Message_Box.show())

        self.AdminButton.clicked.connect(self.Admin)
        self.Refresh_2.clicked.connect(self.clear)
        self.Search.clicked.connect(self.search)

        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 250)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)

        self.tableWidget.setColumnWidth(11, 100)
        self.tableWidget.setColumnWidth(12, 100)
        self.tableWidget.setColumnWidth(13, 100)
        self.tableWidget.setHorizontalHeaderLabels(["ID","CATEGORY","ITEM-NAME","LOCATION","DATE","ITEM-DESCRIPTION","FIRST-NAME",
                                                   "LAST-NAME","EMAIL","CONTACT #","CLAIMER-LNAME","CLAIMER-FNAME","CONTACT #","EMAIL"])

        self.loaddata()
        self.refresh_bts()
        self.tableWidget.clicked.connect(self.getItem)

        # adding list of items to combo box
        self.combo = self.findChild(QComboBox,"comboBox")
        self.label = self.findChild(QLineEdit, "lineEdit_25")

        # add item
        #self.combo.addItem("-Type-")
        type1 = self.combo.addItem("Type 1")
        type2 = self.combo.addItem("Type 2")

        self.combo.activated.connect(self.clicker)

        pass


    def search(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            query = ("SELECT * FROM `items` WHERE CATEGORY = %s")
            data = (self.lineEdit_25.text(),)


            cur = con.cursor()
            cur.execute(query, data)
            tablerow = 0
            records = cur.fetchall()
            print("Number of records in the table: ", cur.rowcount)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(records):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


        except Error as error:
            print("Error in the program {}".format(error))
        finally:
            if con.is_connected():
                cur.close()
                con.close()
                print("MySQL Connection is now CLOSED!")

    def clicker(self):
        self.label.setText(f'{self.combo.currentText()}')

        pass

    def getItem(self):
        row = self.tableWidget.currentRow()
        print(str(row))
        ID = self.tableWidget.item(row, 0).text()
        Categ = self.tableWidget.item(row, 1).text()
        ItmName = self.tableWidget.item(row, 2).text()
        LocFound = self.tableWidget.item(row, 3).text()
        DateFound = self.tableWidget.item(row, 4).text()
        FounderName1 = self.tableWidget.item(row, 7).text()
        FounderName2 = self.tableWidget.item(row, 6).text()
        FounderEmail = self.tableWidget.item(row, 8).text()
        FounderContact = self.tableWidget.item(row, 9).text()

        ClaimerLname = self.tableWidget.item(row, 10).text()
        ClaimerFname = self.tableWidget.item(row, 11).text()
        ClaimerContact = self.tableWidget.item(row, 12).text()
        ClaimerEmail = self.tableWidget.item(row, 13).text()

        self.lineEdit_16.setText(ID)
        self.lineEdit_17.setText(Categ)
        self.lineEdit_18.setText(ItmName)
        self.lineEdit_19.setText(LocFound)
        self.lineEdit_20.setText(DateFound)
        self.lineEdit_21.setText(FounderName1)
        self.lineEdit_22.setText(FounderName2)
        self.lineEdit_23.setText(FounderEmail)
        self.lineEdit_24.setText(FounderContact)

        self.lineEdit_13.setText(ClaimerLname)
        self.lineEdit_15.setText(ClaimerFname)
        self.lineEdit_12.setText(ClaimerContact)
        self.lineEdit_14.setText(ClaimerEmail)

    def claimer(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            cursor = connection.cursor()
            id = self.lineEdit_16.text()
            clname = self.lineEdit_13.text()
            cfname = self.lineEdit_15.text()
            ccontact = self.lineEdit_12.text()
            cemail = self.lineEdit_14.text()



            print("Before updating a record ")
            sql_select_query = "select * from items where ID = '" + id + "'"
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

            # Update single record now
            sql_update_query = "Update items set CLNAME = '" + clname + "', CFNAME = '" + cfname + "', CCONTACT = '" + ccontact + "',CEMAIL = '" + cemail + "' where ID = '" + id + "'"
            cursor.execute(sql_update_query)
            connection.commit()
            print("Record Updated successfully ")

            print("After updating record ")
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

        except mysql.connector.Error as error:
            print("Failed to update table record: {}".format(error))
        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

    def refresh_bts(self):
        self.Refresh.clicked.connect(self.loaddata)


    def clear(self):

        self.lineEdit_16.clear()
        self.lineEdit_17.clear()
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.lineEdit_13.clear()
        self.lineEdit_15.clear()
        self.lineEdit_12.clear()
        self.lineEdit_14.clear()
    def loaddata(self):

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            query = "SELECT * FROM `items`"

            cur = con.cursor()
            cur.execute(query)
            self.lineEdit_25.clear()
            tablerow = 0
            records = cur.fetchall()
            print("Number of records in the table: ", cur.rowcount)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(records):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


        except Error as error:
            print("Error in the program {}".format(error))
        finally:
            if con.is_connected():
                cur.close()
                con.close()
                print("MySQL Connection is now CLOSED!")
    def Admin(self):
        passwrd = PasswordPage()
        widget.addWidget(passwrd)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class adminpage(QDialog):
    def __init__(self):
        super(adminpage, self).__init__()
        loadUi("AdminPage.ui",self)

        self.LogoutButton.clicked.connect(self.backmain)
        self.AddBtn.clicked.connect(self.insertdata)
        self.DelButton.clicked.connect(self.delete)
        self.SaveButton.clicked.connect(self.update)
        self.SaveButton_2.clicked.connect(self.clear)

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 250)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(9, 100)
        self.tableWidget.setColumnWidth(10, 100)

        self.tableWidget.setColumnWidth(11, 100)
        self.tableWidget.setColumnWidth(12, 100)
        self.tableWidget.setColumnWidth(13, 100)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "CATEGORY", "ITEM-NAME", "LOCATION", "DATE", "ITEM-DESCRIPTION", "FIRST-NAME",
             "LAST-NAME", "EMAIL", "CONTACT #", "CLAIMER-LNAME", "CLAIMER-FNAME", "CONTACT #", "EMAIL"])

        self.refresh_bts()
        self.tableWidget.clicked.connect(self.getItem)

        # adding list of items to combo box
        self.combo1 = self.findChild(QComboBox,"comboBox1")
        self.label = self.findChild(QLineEdit, "lineEdit_12")

        # add item
        self.combo1.addItem("Type 1")
        self.combo1.addItem("Type 2")

        self.combo1.activated.connect(self.clicker)

        pass
    def clicker(self):
        self.label.setText(f'{self.combo1.currentText()}')





    def clear(self):
        self.lineEdit_9.clear()
        self.lineEdit_12.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
        self.lineEdit_5.clear()


    def refresh_bts(self):
        self.UpdateButton.clicked.connect(self.loaddata)

    def delete(self):
        print("Hello")


        con = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")

        cur = con.cursor()
        query = ("DELETE FROM `items` WHERE ID = %s")
        data = (self.lineEdit_9.text(),)
        try:
            cur.execute(query, data)
            con.commit()
            print("Data deleted")
            self.lineEdit_9.clear()
            self.lineEdit_12.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_7.clear()
            self.lineEdit_6.clear()
            self.lineEdit_8.clear()
            self.lineEdit_5.clear()
        except:
            con.close()
            print("Closed")

    def update(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            cursor = connection.cursor()
            id = self.lineEdit_9.text()
            categ = self.lineEdit_12.text()
            itname = self.lineEdit_3.text()
            loc = self.lineEdit_4.text()
            date = self.lineEdit_10.text()
            descrip = self.lineEdit_11.text()
            fname = self.lineEdit_7.text()
            lname = self.lineEdit_6.text()
            email = self.lineEdit_8.text()
            contact = self.lineEdit_5.text()

            print("Before updating a record ")
            sql_select_query = "select * from items where id = '" + id + "'"
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

            # Update single record now
            sql_update_query = "Update items set CATEGORY = '" + categ + "', ITMNAME = '" + itname + "', LOCATION = '" + loc + "',DATE = '" + date + "', DESCRIPTION = '" + descrip + "',FNAME = '" + fname + "',LNAME = '" + lname + "',EMAIL = '" + email + "',CONTACT = '" + contact + "' where id = '" + id + "'"
            cursor.execute(sql_update_query)
            connection.commit()
            print("Record Updated successfully ")

            print("After updating record ")
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

        except mysql.connector.Error as error:
            print("Failed to update table record: {}".format(error))
        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")


    def insertdata(self):

        print("Hello")

        con = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")

        cur = con.cursor()
        query = (
            "INSERT INTO `items` (`ID`, `CATEGORY`, `ITMNAME`, `LOCATION`, `DATE`, `DESCRIPTION`, `FNAME`, `LNAME`, `EMAIL`, `CONTACT`)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (self.lineEdit_9.text(), self.lineEdit_12.text(), self.lineEdit_3.text(),
                self.lineEdit_4.text(), self.lineEdit_10.text(), self.lineEdit_11.text(),
                self.lineEdit_7.text(), self.lineEdit_6.text(), self.lineEdit_8.text(), self.lineEdit_5.text())
        try:
            cur.execute(query, data)
            con.commit()
            print("Data inserted")
        except:
            con.close()
            print("Closed")

    def loaddata(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            query = "SELECT * FROM `items`"

            cur = con.cursor()
            cur.execute(query)
            tablerow = 0
            records = cur.fetchall()
            print("Number of records in the table: ", cur.rowcount)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(records):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


        except Error as error:
            print("Error in the program {}".format(error))
        finally:
            if con.is_connected():
                cur.close()
                con.close()
                print("MySQL Connection is now CLOSED!")

    def backmain(self):
        back = Main()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getItem(self):
        row = self.tableWidget.currentRow()
        print(str(row))
        ID = self.tableWidget.item(row, 0).text()
        Categ = self.tableWidget.item(row, 1).text()
        ItmName = self.tableWidget.item(row, 2).text()
        LocFound = self.tableWidget.item(row, 3).text()
        Desc = self.tableWidget.item(row, 5).text()
        DateFound = self.tableWidget.item(row, 4).text()
        FounderName1 = self.tableWidget.item(row, 7).text()
        FounderName2 = self.tableWidget.item(row, 6).text()
        FounderEmail = self.tableWidget.item(row, 8).text()
        FounderContact = self.tableWidget.item(row, 9).text()

        self.lineEdit_9.setText(ID)
        self.lineEdit_12.setText(Categ)



        self.lineEdit_3.setText(ItmName)
        self.lineEdit_4.setText(LocFound)
        self.lineEdit_10.setText(DateFound)
        self.lineEdit_11.setText(Desc)
        self.lineEdit_6.setText(FounderName1)
        self.lineEdit_7.setText(FounderName2)
        self.lineEdit_8.setText(FounderEmail)
        self.lineEdit_5.setText(FounderContact)




class PasswordPage(QDialog):
    def __init__(self):
        super(PasswordPage, self).__init__()
        loadUi("PasswordPage.ui", self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.loginfunction1)
        self.commandLinkButton.clicked.connect(self.backmain)

    def backmain(self):
        back = Main()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginfunction(self):
        fillprofile = Main()
        widget.addWidget(fillprofile)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginfunction1(self):
        user = self.UsernameField.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="python_database")
            mycursor = mydb.cursor()
            user = self.UsernameField.text()
            password = self.passwordfield.text()

            sql = "SELECT * FROM `login` WHERE Username = %s and Password = %s"
            mycursor.execute(sql, [(user), (password)])
            results = mycursor.fetchall()
            if results:
                print("GG")
                back = adminpage()
                widget.addWidget(back)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.error.setText("Invalid username or password")

class Message_UI(QtWidgets.QDialog):
    def __init__(self):
        super(Message_UI, self).__init__()
        QtWidgets.QDialog.__init__(self)
        loadUi("DIALOG.ui", self)


#main
app = QApplication(sys.argv)
main = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedHeight(660)
widget.setFixedWidth(900)
widget.setWindowTitle("Lost and Found Item")
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")