from PySide6 import QtCore, QtGui, QtWidgets


class VistaPokemon(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.setObjectName("vista_pokemon_1")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setObjectName("vista_pokemon_2")

        self.graphicsView = QtWidgets.QGraphicsView(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("border-image: url(:/bulbasur.png);")
        self.graphicsView.setObjectName("graphicsView")
        layout.addWidget(self.graphicsView)

        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        layout.addWidget(self.label)

        self.editar = QtWidgets.QPushButton("Editar equipo", self)
        self.editar.setObjectName("editar")
        layout.addWidget(self.editar)


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

        # Widget vista_pokemon_1 utilizando la clase VistaPokemon
        self.vista_pokemon_1 = VistaPokemon(parent=self.centralwidget)
        self.horizontalLayout_2.addWidget(self.vista_pokemon_1)

        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_2.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vista_pokemon_1.label.setText(_translate("MainWindow", "Equipo 1"))
        self.vista_pokemon_1.editar.setText(_translate("MainWindow", "Editar equipo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
