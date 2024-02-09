from PySide6 import QtCore, QtGui, QtWidgets


class VistaPokemonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("vista_pokemon_1")
        self.setStyleSheet("background-color: rgb(206, 206, 206);")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName("vista_pokemon_2")

        self.verticalWidget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout_11")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("border-image: url(:/bulbasur.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.editar = QtWidgets.QPushButton(self.verticalWidget)
        self.editar.setObjectName("editar")
        self.verticalLayout.addWidget(self.editar)

        self.layout.addWidget(self.verticalWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 725)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_2.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.layout1 = QtWidgets.QHBoxLayout(parent=self.centralwidget)
        self.verticalWidget_2.addWidget(self.layout1)
        self.horizontalLayout_2.addWidget(self.verticalWidget_2)

        self.verticalWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget1.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalWidget1.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.verticalWidget2 = QtWidgets.QWidget(parent=self.verticalWidget1)
        self.verticalWidget2.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget2.setObjectName("verticalWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalWidget3 = QtWidgets.QWidget(parent=self.verticalWidget2)
        self.verticalWidget3.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.verticalWidget3.setObjectName("verticalWidget3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalWidget3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.verticalWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setStyleSheet("border-image: url(:/bulbasur.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_14.addWidget(self.graphicsView_2)

        self.verticalLayout_4.addWidget(self.verticalWidget3)

        self.label_4 = QtWidgets.QLabel(parent=self.verticalWidget2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)

        self.cambiarEquipo = QtWidgets.QPushButton(parent=self.verticalWidget2)
        self.cambiarEquipo.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.cambiarEquipo.setObjectName("cambiarEquipo")
        self.verticalLayout_4.addWidget(self.cambiarEquipo)

        self.verticalLayout.addWidget(self.verticalWidget2)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

        self.horizontalWidget_4 = QtWidgets.QWidget(parent=self.verticalWidget1)
        self.horizontalWidget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalWidget_4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.volverInicio = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.volverInicio.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.volverInicio.setObjectName("volverInicio")
        self.horizontalLayout_5.addWidget(self.volverInicio)

        self.empezarJugar = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.empezarJugar.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.empezarJugar.setObjectName("empezarJugar")
        self.horizontalLayout_5.addWidget(self.empezarJugar)

        self.verticalLayout.addWidget(self.horizontalWidget_4)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem4)

        self.horizontalLayout_2.addWidget(self.verticalWidget1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cambiarEquipo.setText(_translate("MainWindow", "Cambiar equipo"))
        self.volverInicio.setText(_translate("MainWindow", "Volver al inicio"))
        self.empezarJugar.setText(_translate("MainWindow", "Empezar a jugar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
