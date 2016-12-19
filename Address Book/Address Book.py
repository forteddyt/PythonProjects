import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from AddressBookGUI import Ui_Dialog

class MyFirstWidget(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)

		self.AddContact.clicked.connect(self.addNewContact)

	def addNewContact(self):
		name = self.NewContactName.text()
		address = self.NewContactName.text()
		email = self.NewContactName.text()
		phone_num = self.NewContactName.text()
		emergency_name = self.NewContactName.text()
		emergency_phone_num = self.NewContactName.text()

		text_file = open("AddressInfo.txt", "a")
		text_file.write(name + "~,~" + address + "~,~" + email + "~,~" + phone_num + "~,~" + emergency_name + "~,~" + emergency_phone_num + "\n")



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstWidget(dialog)
 
	dialog.show()