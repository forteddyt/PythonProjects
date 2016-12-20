import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from AddressBookGUI import Ui_Dialog

class MyFirstWidget(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)

		self.AddContact.clicked.connect(self.addNewContact)
		self.ResetContact.clicked.connect(self.resetNewContact)

	def addNewContact(self):
		name = self.NewContactName.text()
		address = self.NewContactAddress.text()
		city = self.NewContactCity.text()
		state = self.NewContactState.text()
		zip_code = self.NewContactZipCode.text()
		email = self.NewContactEmail.text()
		phone_num = self.NewContactPhoneNumber.text()
		emergency_name = self.NewContactEmergencyContactName.text()
		emergency_phone_num = self.NewContactEmergencyContactPhoneNumber.text()

		new_contact_list = [name, address, city, state, zip_code, email, phone_num, emergency_name, emergency_phone_num]

		text_file = open("AddressInfo.txt", "a")
		for element in new_contact_list:
			text_file.write(element + "~,~")
		text_file.write("\n")
		self.ResetContact.click()

	def resetNewContact(self):
		self.NewContactName.clear()
		self.NewContactAddress.clear()
		self.NewContactCity.clear()
		self.NewContactState.clear()
		self.NewContactZipCode.clear()
		self.NewContactEmail.clear()
		self.NewContactPhoneNumber.clear()
		self.NewContactEmergencyContactName.clear()
		self.NewContactEmergencyContactPhoneNumber.clear()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstWidget(dialog)
 
	dialog.show()
	sys.exit(app.exec_())