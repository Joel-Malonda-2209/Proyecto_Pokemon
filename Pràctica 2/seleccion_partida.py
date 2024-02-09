from PySide6 import QtCore, QtGui, QtWidgets
from recursos2 import *

class SelPartida(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 665)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(0, 10))
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cerrarSesion = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.cerrarSesion.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cerrarSesion.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.cerrarSesion.setObjectName("cerrarSesion")
        self.MainWindow = MainWindow
        self.cerrarSesion.clicked.connect(self.volver_a_login)
        self.verticalLayout_8.addWidget(self.cerrarSesion)
        self.verticalLayout_6.addWidget(self.verticalWidget_2)
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(250, 200))
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(500, 700))
        self.horizontalWidget_2.setStyleSheet("border-image: url(:/pickachu.png);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6.addWidget(self.horizontalWidget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget_21 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_21.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalWidget_21.setMaximumSize(QtCore.QSize(500, 250))
        self.verticalWidget_21.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.verticalWidget_21.setStyleSheet("")
        self.verticalWidget_21.setObjectName("verticalWidget_21")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.verticalWidget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(200, 100))
        self.graphicsView.setStyleSheet("border-image: url(:/partida-rapida.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.partidaRapida = QtWidgets.QPushButton(parent=self.verticalWidget_21)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.partidaRapida.setFont(font)
        self.partidaRapida.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 255, 0);")
        self.partidaRapida.setObjectName("partidaRapida")
        self.partidaRapida.clicked.connect(self.iraPartidaRapida)
        self.verticalLayout_3.addWidget(self.partidaRapida)
        self.verticalLayout_2.addWidget(self.verticalWidget_21)
        self.verticalWidget_3 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_3.setMaximumSize(QtCore.QSize(500, 250))
        self.verticalWidget_3.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.verticalWidget_3.setStyleSheet("")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(200, 100))
        self.graphicsView_2.setStyleSheet("border-image: url(:/ladder.jpg);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_4.addWidget(self.graphicsView_2)
        self.ladder = QtWidgets.QPushButton(parent=self.verticalWidget_3)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.ladder.setFont(font)
        self.ladder.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.ladder.setObjectName("ladder")
        self.ladder.clicked.connect(self.abrir_eleccion_equipo)
        self.verticalLayout_4.addWidget(self.ladder)
        self.verticalLayout_2.addWidget(self.verticalWidget_3)
        self.verticalWidget_4 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.verticalWidget_4.setMaximumSize(QtCore.QSize(500, 250))
        self.verticalWidget_4.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.verticalWidget_4.setStyleSheet("")
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.verticalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setMinimumSize(QtCore.QSize(200, 100))
        self.graphicsView_3.setStyleSheet("border-image: url(:/build.jpg);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_5.addWidget(self.graphicsView_3)
        self.team = QtWidgets.QPushButton(parent=self.verticalWidget_4)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.team.setFont(font)
        self.team.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.team.setObjectName("team")
        self.verticalLayout_5.addWidget(self.team)
        self.verticalLayout_2.addWidget(self.verticalWidget_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.horizontalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def iraPartidaRapida(self):
            self.MainWindow.close()
        
            from pantalla_lucha_definitiva import Ui_MainWindow
            self.rapida = Ui_MainWindow()
            self.rapida.setupUi(self.MainWindow) 
            self.MainWindow.show()
        
    def abrir_eleccion_equipo(self):
            self.MainWindow.close()
            
            from Eleccion_equipo import Ui_MainWindow
            self.eleccion = Ui_MainWindow()
            self.eleccion.setupUi(self.MainWindow) 
            self.MainWindow.show()
    
    def volver_a_login(self):
            self.MainWindow.close()
            
            from NovaLogin import Login
            self.registro_window = Login()
            self.registro_window.setupUi(self.MainWindow) 
            self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cerrarSesion.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.partidaRapida.setText(_translate("MainWindow", "Partida Rápida"))
        self.ladder.setText(_translate("MainWindow", "Ladder"))
        self.team.setText(_translate("MainWindow", "Team Builder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SelPartida()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
