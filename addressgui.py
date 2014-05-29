#!/usr/bin/python
import sys
from PyQt4 import QtGui

class Book(QtGui.QWidget):
    def __init__(self):
        super(Book, self).__init__()

        self.initUI()

    def initUI(self):
        name = QtGui.QLabel("Name",self);
        name.move(20,20);
        self.nametxt = QtGui.QLineEdit(self);
        self.nametxt.move(80,20);

        phone = QtGui.QLabel("phone",self);
        phone.move(20,60);
        self.phonetxt = QtGui.QLineEdit(self);
        self.phonetxt.move(80,60);

        email = QtGui.QLabel("email",self);
        email.move(20,100);
        self.emailtxt = QtGui.QLineEdit(self);
        self.emailtxt.move(80,100);

        address = QtGui.QLabel("address",self);
        address.move(20,140);
        self.addresstxt = QtGui.QTextEdit(self);
        self.addresstxt.resize(200,130);
        self.addresstxt.move(80,140);

        addbtn = QtGui.QPushButton("Add",self)
        addbtn.clicked.connect(self.buttonClicked)
        addbtn.move(80,285)

        clrbtn = QtGui.QPushButton("Clear",self)
        clrbtn.clicked.connect(self.clearClicked)
        clrbtn.move(180,285)


        self.setGeometry(300,350,320,320);
        self.setFixedSize(320,320);
        self.setWindowTitle("AddressBook")
        self.show()

    def buttonClicked(self):
        name = self.nametxt.text()
        phone = self.phonetxt.text()
        email = self.emailtxt.text()
        address = self.addresstxt.toPlainText()

        str = "%s, %s, %s, %s\n"%(name,phone,email,address)

        f = open('address.txt','a')
        f.write(str);
        f.close()

        QtGui.QMessageBox.information(self,'info','added to book',1)

    def clearClicked(self):
        self.nametxt.setText("")
        self.phonetxt.setText("")
        self.emailtxt.setText("")
        self.addresstxt.setText("")

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Book()

    sys.exit(app.exec_())

if __name__=='__main__':
    main()

