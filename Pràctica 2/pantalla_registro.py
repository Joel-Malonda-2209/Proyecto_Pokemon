# Form implementation generated from reading ui file 'pantalla_registro.ui'
#
# Created by: PySide6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap



class PantRegistro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 684)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.verticalWidget)
        self.horizontalWidget.setStyleSheet("background-color: rgb(222, 235, 231);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalWidget1 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget1.setStyleSheet("border-style: solid; \n"
"border-width: 4px;\n"
"border-color: rgb(255, 0, 0);\n"
"background-color: rgb(225, 225, 225);\n"
"border-radius: 5px")
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.verticalWidget1)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(350, 40))
        self.lineEdit_2.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.verticalWidget1)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(350, 40))
        self.lineEdit_3.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.verticalWidget1)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(350, 40))
        self.lineEdit_4.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalWidget1)
        self.lineEdit.setMaximumSize(QtCore.QSize(350, 40))
        self.lineEdit.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton = QtWidgets.QRadioButton(parent=self.verticalWidget1)
        self.radioButton.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_7.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.verticalWidget1)
        self.radioButton_2.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_7.addWidget(self.radioButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AccederLogin = QtWidgets.QPushButton(parent=self.verticalWidget1)
        self.AccederLogin.setMaximumSize(QtCore.QSize(16777215, 40))
        self.AccederLogin.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.AccederLogin.setObjectName("AccederLogin")
        self.horizontalLayout_4.addWidget(self.AccederLogin)
        self.Cancelar = QtWidgets.QPushButton(parent=self.verticalWidget1)
        self.Cancelar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Cancelar.setStyleSheet("border-style: solid; \n"
"border-width: 1px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.Cancelar.setObjectName("Cancelar")
        self.horizontalLayout_4.addWidget(self.Cancelar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addWidget(self.verticalWidget1)
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalWidget_2.setStyleSheet("image: url(:/Profesor_Oak.png);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3.addWidget(self.verticalWidget_2)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.verticalWidget)
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(48, 105, 106);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalWidget1 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.horizontalWidget1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5.addWidget(self.horizontalWidget1)
        self.horizontalWidget_21 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.horizontalWidget_21.setMinimumSize(QtCore.QSize(350, 0))
        self.horizontalWidget_21.setMaximumSize(QtCore.QSize(900, 250))
        self.horizontalWidget_21.setStyleSheet("")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.horizontalWidget_21)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("border-style: solid; \n"
"border-width: 8px;\n"
"border-color: rgb(170, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.horizontalWidget_21)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_2.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Entrenador (Nombre)"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Correo Electrónico"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Repetir Contraseña"))
        self.radioButton.setText(_translate("MainWindow", "Chico"))
        self.radioButton_2.setText(_translate("MainWindow", "Chica"))
        self.AccederLogin.setText(_translate("MainWindow", "Acceder"))
        self.Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "Bueno, cuéntame algo sobre ti."))
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PantRegistro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
