from PySide6 import QtCore, QtGui, QtWidgets
import json
import requests

class VistaPokemonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.setObjectName("vista_pokemon_1")
        self.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.MainWindow = main_window 
        self.vista_pokemon_2 = QtWidgets.QVBoxLayout(self)
        self.vista_pokemon_2.setObjectName("vista_pokemon_2")

        self.verticalWidget = QtWidgets.QWidget(self)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_11.addWidget(self.graphicsView)

        self.vista_pokemon_2.addWidget(self.verticalWidget)

        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setTabletTracking(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Equipo")
        self.vista_pokemon_2.addWidget(self.label)

        self.editar = QtWidgets.QPushButton(self)
        self.editar.setObjectName("editar")
        self.editar.setText("Editar equipo")
        self.editar.clicked.connect(self.change_edicion_equipo)
        self.vista_pokemon_2.addWidget(self.editar)
        
    def change_edicion_equipo(self):
        self.MainWindow.close()
            
        from Edicion_equipo_test import Ui_MainWindow
        self.edicion_window = Ui_MainWindow()
        self.edicion_window.setupUi(self.MainWindow)
        self.MainWindow.show()
            
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.setObjectName("layout1")
        self.vista_pokemon_1 = VistaPokemonWidget(main_window=MainWindow)
        self.layout1.addWidget(self.vista_pokemon_1)
        self.vista_pokemon_2 = VistaPokemonWidget(main_window=MainWindow)
        self.layout1.addWidget(self.vista_pokemon_2)
        self.verticalLayout_3.addLayout(self.layout1)
        self.layout2 = QtWidgets.QHBoxLayout()
        self.vista_pokemon_3 = VistaPokemonWidget(main_window=MainWindow)
        self.layout2.addWidget(self.vista_pokemon_3)
        self.vista_pokemon_4 = VistaPokemonWidget(main_window=MainWindow)  
        self.layout2.addWidget(self.vista_pokemon_4)
        self.layout2.setObjectName("layout2")
        self.verticalLayout_3.addLayout(self.layout2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
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
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.verticalWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
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
        self.volverInicio.clicked.connect(self.volver_a_partidas)
        self.horizontalLayout_5.addWidget(self.volverInicio)
        self.empezarJugar = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        self.empezarJugar.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.empezarJugar.setObjectName("empezarJugar")
        self.empezarJugar.clicked.connect(self.iraPartidaRapida)
        self.horizontalLayout_5.addWidget(self.empezarJugar)
        self.verticalLayout.addWidget(self.horizontalWidget_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.verticalWidget1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

        self.load_team_data()

    def iraPartidaRapida(self):
        self.MainWindow.close()
    
        from pantalla_lucha_definitiva import Ui_MainWindow
        self.rapida = Ui_MainWindow()
        self.rapida.setupUi(self.MainWindow) 
        self.MainWindow.showMaximized()
            
    def volver_a_partidas(self):
        self.MainWindow.close()    
        from seleccion_partida import SelPartida
        self.registro_window = SelPartida()
        self.registro_window.setupUi(self.MainWindow) 
        self.MainWindow.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cambiarEquipo.setText(_translate("MainWindow", "Cambiar equipo"))
        self.volverInicio.setText(_translate("MainWindow", "Volver al inicio"))
        self.empezarJugar.setText(_translate("MainWindow", "Empezar a jugar"))

    def load_team_data(self):
        with open('team_data.json', 'r') as file:
            team_data = json.load(file)
        
        team_name = team_data['team_name']
        self.vista_pokemon_1.label.setText(team_name)
        
        pokemon_name = team_data['pokemon_team'][0]['name']

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            pokemon_data = response.json()
            img_url = pokemon_data['sprites']['front_default']

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(requests.get(img_url).content)
            scaled_pixmap = pixmap.scaledToHeight(250, QtCore.Qt.TransformationMode.SmoothTransformation)

            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(scaled_pixmap)

            self.vista_pokemon_1.graphicsView.setScene(scene)
            self.graphicsView_2.setScene(scene)
            
        else:
            print(f"No se pudo obtener los datos del Pokémon {pokemon_name}.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
