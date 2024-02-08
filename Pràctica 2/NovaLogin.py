from PySide6 import QtCore, QtGui, QtWidgets

from seleccion_partida import SelPartida as Ui_SecondWindow
from pantalla_registro import PantRegistro 
from recursos2 import *
import json

class PasswordLineEdit(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.line_edit)
        
        self.show_password_button = QtWidgets.QPushButton(self)
        self.show_password_button.setIcon(QtGui.QIcon(":/eyeicon.png"))
        self.show_password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_password_button.setToolTip("Show Password")
        self.show_password_button.clicked.connect(self.password_visibility)
        self.layout.addWidget(self.show_password_button)

    def password_visibility(self):
        if self.line_edit.echoMode() == QtWidgets.QLineEdit.Password:
            self.line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_password_button.setIcon(QtGui.QIcon(":/eyeicon.png"))
        else:
            self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_password_button.setIcon(QtGui.QIcon(":/eyeicon.png"))

    def text(self):
        return self.line_edit.text()

class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalWidget = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.verticalWidget.setMinimumSize(QtCore.QSize(350, 200))
        self.verticalWidget.setStyleSheet("image: url(:/logo.png);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3.addWidget(self.verticalWidget)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.horizontalWidget.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalWidget_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.verticalWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalWidget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.lineEdit_2 = PasswordLineEdit(parent=self.verticalWidget_2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Acceder = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.Acceder.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Acceder.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Acceder.setObjectName("Acceder")
       
        self.horizontalLayout_2.addWidget(self.Acceder)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Registrarse = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.Registrarse.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Registrarse.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Registrarse.setObjectName("Registrarse")
        self.Registrarse.clicked.connect(self.abrir_pantalla_registro)
        self.horizontalLayout_2.addWidget(self.Registrarse)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalWidget_21 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalWidget_21.setMinimumSize(QtCore.QSize(350, 175))
        self.horizontalWidget_21.setStyleSheet("image: url(:/pokemons.png);")
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5.addWidget(self.horizontalWidget_21)
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow
        self.Acceder.clicked.connect(self.verificar_credenciales)
        self.Acceder.clicked.connect(self.abrirPantallaPartidas)
        
        
    def verificar_credenciales(self):
        correo = self.lineEdit.text()
        contraseña = self.lineEdit_2.text()
        
        try:
            with open('usuarios.json', 'r') as file:
                usuarios = json.load(file)
                
            for usuario in usuarios:
                if usuario['correo'] == correo and usuario['contraseña'] == contraseña:
                    self.abrirPantallaPartidas()
                    return
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error de inicio de sesión", "Credenciales incorrectas.")  

        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Archivo de usuarios no encontrado.")
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Usuario (Correo)"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_2.line_edit.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.Acceder.setText(_translate("MainWindow", "Acceder"))
        self.Registrarse.setText(_translate("MainWindow", "Registrarse"))

    
    def abrir_pantalla_registro(self):
        self.MainWindow.close()
        self.registro_window = PantRegistro()
        self.registro_window.setupUi(self.MainWindow)
        self.MainWindow.show()

    def abrirPantallaPartidas(self):
        correo = self.lineEdit.text()
        contraseña = self.lineEdit_2.text()

        try:
            with open('usuarios.json', 'r') as file:
                usuarios = json.load(file)

            for usuario in usuarios:
                if usuario['correo'] == correo and usuario['contraseña'] == contraseña:
                    
                    for i in reversed(range(self.verticalLayout_2.count())):
                        widget = self.verticalLayout_2.itemAt(i).widget()
                        if widget is not None:
                            widget.deleteLater()

                    self.ui = Ui_SecondWindow()
                    self.ui.setupUi(MainWindow)
                    return

           
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error de inicio de sesión", "Credenciales incorrectas.")

        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Archivo de usuarios no encontrado.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
