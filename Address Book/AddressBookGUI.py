# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddressBookGUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(954, 754)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(340, 250))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(450, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(129, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(156, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 914, 391))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 150))
        self.groupBox_2.setMaximumSize(QtCore.QSize(936, 270))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.AddContact = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.AddContact.setFont(font)
        self.AddContact.setAutoDefault(False)
        self.AddContact.setObjectName("AddContact")
        self.gridLayout_5.addWidget(self.AddContact, 0, 1, 1, 1)
        self.ResetContact = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ResetContact.setFont(font)
        self.ResetContact.setAutoDefault(False)
        self.ResetContact.setObjectName("ResetContact")
        self.gridLayout_5.addWidget(self.ResetContact, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setStyleSheet("border-color: rgba(255, 255, 255, 0);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 762, 230))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)
        self.NewContactEmail = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactEmail.setFont(font)
        self.NewContactEmail.setObjectName("NewContactEmail")
        self.gridLayout_8.addWidget(self.NewContactEmail, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 8, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 7, 0, 1, 1)
        self.NewContactEmergencyContactPhoneNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactEmergencyContactPhoneNumber.setFont(font)
        self.NewContactEmergencyContactPhoneNumber.setObjectName("NewContactEmergencyContactPhoneNumber")
        self.gridLayout_8.addWidget(self.NewContactEmergencyContactPhoneNumber, 8, 3, 1, 1)
        self.NewContactEmergencyContactName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactEmergencyContactName.setFont(font)
        self.NewContactEmergencyContactName.setObjectName("NewContactEmergencyContactName")
        self.gridLayout_8.addWidget(self.NewContactEmergencyContactName, 7, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 2, 0, 1, 1)
        self.NewContactPhoneNumber = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactPhoneNumber.setFont(font)
        self.NewContactPhoneNumber.setObjectName("NewContactPhoneNumber")
        self.gridLayout_8.addWidget(self.NewContactPhoneNumber, 5, 3, 1, 1)
        self.NewContactAddress = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactAddress.setFont(font)
        self.NewContactAddress.setObjectName("NewContactAddress")
        self.gridLayout_8.addWidget(self.NewContactAddress, 1, 3, 1, 1)
        self.NewContactName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewContactName.sizePolicy().hasHeightForWidth())
        self.NewContactName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactName.setFont(font)
        self.NewContactName.setText("")
        self.NewContactName.setClearButtonEnabled(False)
        self.NewContactName.setObjectName("NewContactName")
        self.gridLayout_8.addWidget(self.NewContactName, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NewContactCity = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewContactCity.sizePolicy().hasHeightForWidth())
        self.NewContactCity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactCity.setFont(font)
        self.NewContactCity.setObjectName("NewContactCity")
        self.horizontalLayout_2.addWidget(self.NewContactCity)
        self.NewContactState = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewContactState.sizePolicy().hasHeightForWidth())
        self.NewContactState.setSizePolicy(sizePolicy)
        self.NewContactState.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactState.setFont(font)
        self.NewContactState.setObjectName("NewContactState")
        self.horizontalLayout_2.addWidget(self.NewContactState)
        self.NewContactZipCode = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewContactZipCode.sizePolicy().hasHeightForWidth())
        self.NewContactZipCode.setSizePolicy(sizePolicy)
        self.NewContactZipCode.setMinimumSize(QtCore.QSize(100, 0))
        self.NewContactZipCode.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.NewContactZipCode.setFont(font)
        self.NewContactZipCode.setObjectName("NewContactZipCode")
        self.horizontalLayout_2.addWidget(self.NewContactZipCode)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 2, 3, 1, 1)
        self.label.raise_()
        self.NewContactName.raise_()
        self.label_2.raise_()
        self.NewContactAddress.raise_()
        self.label_5.raise_()
        self.NewContactEmail.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.NewContactEmergencyContactName.raise_()
        self.NewContactPhoneNumber.raise_()
        self.NewContactEmergencyContactPhoneNumber.raise_()
        self.label_9.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.NewContactName, self.NewContactAddress)
        Dialog.setTabOrder(self.NewContactAddress, self.NewContactCity)
        Dialog.setTabOrder(self.NewContactCity, self.NewContactState)
        Dialog.setTabOrder(self.NewContactState, self.NewContactZipCode)
        Dialog.setTabOrder(self.NewContactZipCode, self.NewContactEmail)
        Dialog.setTabOrder(self.NewContactEmail, self.NewContactPhoneNumber)
        Dialog.setTabOrder(self.NewContactPhoneNumber, self.NewContactEmergencyContactName)
        Dialog.setTabOrder(self.NewContactEmergencyContactName, self.NewContactEmergencyContactPhoneNumber)
        Dialog.setTabOrder(self.NewContactEmergencyContactPhoneNumber, self.AddContact)
        Dialog.setTabOrder(self.AddContact, self.ResetContact)
        Dialog.setTabOrder(self.ResetContact, self.scrollArea)
        Dialog.setTabOrder(self.scrollArea, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.scrollArea_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Contacts"))
        self.pushButton.setText(_translate("Dialog", "Remove Selected"))
        self.groupBox_2.setTitle(_translate("Dialog", "New Contact"))
        self.AddContact.setText(_translate("Dialog", "Add"))
        self.ResetContact.setText(_translate("Dialog", "Reset"))
        self.label_6.setText(_translate("Dialog", "Phone Number:"))
        self.label_5.setText(_translate("Dialog", "Email:"))
        self.label_2.setText(_translate("Dialog", "Address:"))
        self.NewContactEmail.setPlaceholderText(_translate("Dialog", "jdoe@email.com"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_8.setText(_translate("Dialog", "Emergency Contact Phone Number: "))
        self.label_7.setText(_translate("Dialog", "Emergency Contact Name: "))
        self.NewContactEmergencyContactPhoneNumber.setPlaceholderText(_translate("Dialog", "(987) 654-3210"))
        self.NewContactEmergencyContactName.setPlaceholderText(_translate("Dialog", "James Doe"))
        self.label_9.setText(_translate("Dialog", "City/State:"))
        self.NewContactPhoneNumber.setPlaceholderText(_translate("Dialog", "(123) 456-7890"))
        self.NewContactAddress.setPlaceholderText(_translate("Dialog", "12345 Generic Pl "))
        self.NewContactName.setPlaceholderText(_translate("Dialog", "John Doe"))
        self.NewContactCity.setPlaceholderText(_translate("Dialog", "City"))
        self.NewContactState.setPlaceholderText(_translate("Dialog", "ie VA"))
        self.NewContactZipCode.setPlaceholderText(_translate("Dialog", "Zip Code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

