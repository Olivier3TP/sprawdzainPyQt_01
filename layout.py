# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(683, 351)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 661, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.internistaRadio = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.internistaRadio.setObjectName("internistaRadio")
        self.gridLayout.addWidget(self.internistaRadio, 2, 0, 1, 1)
        self.dermatologRadio = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.dermatologRadio.setObjectName("dermatologRadio")
        self.gridLayout.addWidget(self.dermatologRadio, 4, 0, 1, 1)
        self.privateCheck = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.privateCheck.setEnabled(True)
        self.privateCheck.setChecked(True)
        self.privateCheck.setObjectName("privateCheck")
        self.gridLayout.addWidget(self.privateCheck, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pediatraRadio = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.pediatraRadio.setObjectName("pediatraRadio")
        self.gridLayout.addWidget(self.pediatraRadio, 3, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.surnameEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.surnameEdit.setObjectName("surnameEdit")
        self.gridLayout.addWidget(self.surnameEdit, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)
        self.resultLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.resultLabel.setText("")
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setObjectName("resultLabel")
        self.gridLayout.addWidget(self.resultLabel, 2, 1, 4, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.internistaRadio.setText(_translate("Dialog", "Internista"))
        self.dermatologRadio.setText(_translate("Dialog", "Dermatolog"))
        self.privateCheck.setText(_translate("Dialog", "Wizyta prywatna"))
        self.label.setText(_translate("Dialog", "Podaj imię: "))
        self.pediatraRadio.setText(_translate("Dialog", "Pediatra"))
        self.label_2.setText(_translate("Dialog", "Podaj nazwisko:"))
        self.pushButton.setText(_translate("Dialog", "Rezerwój"))
