import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from AddressBookGUI import Ui_Dialog

class MyFirstWidget(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)

		self.AddContact.clicked.connect(self.storeNewContact)

	def storeNewContact(self):
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
		text_file.close()
		self.ResetContact.click()

	def displayStoredContacts(self):
		text_file = open("AddressInfo.txt", "r")
		lines = text_file.readlines()
		for line in lines:
			data = line.split("~,~")
			for info in data:
				print(info)
		text_file.close()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstWidget(dialog)
	prog.displayStoredContacts()
 
	dialog.show()
	sys.exit(app.exec_())