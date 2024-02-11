from PySide6 import QtCore, QtGui, QtWidgets
from recursos2 import *
import requests
import json
import random
from PySide6.QtCore import QTimer, QDateTime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridWidget = QtWidgets.QWidget(parent=self.verticalWidget)
        self.gridWidget.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6.addWidget(self.gridWidget)
        self.verticalWidget1 = QtWidgets.QWidget(parent=self.verticalWidget)
        self.verticalWidget1.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6.addWidget(self.verticalWidget1)
        self.horizontalLayout_7.addWidget(self.verticalWidget)
        self.gridWidget1 = QtWidgets.QWidget(parent=self.widget)
        self.gridWidget1.setMinimumSize(QtCore.QSize(300, 0))
        self.gridWidget1.setMaximumSize(QtCore.QSize(900, 16777215))
        self.gridWidget1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_8.addWidget(self.graphicsView)
        self.label = QtWidgets.QLabel(parent=self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.gridWidget1)
        self.label_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_2.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_5.addWidget(self.graphicsView_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.gridWidget1)
        self.verticalWidget2 = QtWidgets.QWidget(parent=self.widget)
        self.verticalWidget2.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalWidget2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget2.setObjectName("verticalWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.verticalWidget2)
        self.verticalWidget_2.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_7.addWidget(self.verticalWidget_2)
        self.gridWidget_2 = QtWidgets.QWidget(parent=self.verticalWidget2)
        self.gridWidget_2.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_7.addWidget(self.gridWidget_2)
        self.horizontalLayout_7.addWidget(self.verticalWidget2)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.horizontalWidget.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridWidget2 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.gridWidget2.setMinimumSize(QtCore.QSize(250, 0))
        self.gridWidget2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.gridWidget2.setObjectName("gridWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridWidget2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.gridWidget2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_5.setStyleSheet("border-style: solid;border-width:4px; border-color: rgb(236, 217, 51); background-color: rgb(196, 241, 160); color: rgb(0,0,0); border-radius: 5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.gridWidget2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setStyleSheet("border-style: solid;border-width:4px; border-color: rgb(236, 217, 51); background-color: rgb(196, 241, 160); color: rgb(0,0,0); border-radius: 5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridWidget2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.setStyleSheet("border-style: solid;border-width:4px; border-color: rgb(236, 217, 51); background-color: rgb(196, 241, 160); color: rgb(0,0,0); border-radius: 5px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.gridWidget2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setStyleSheet("border-style: solid;border-width:4px; border-color: rgb(236, 217, 51); background-color: rgb(196, 241, 160); color: rgb(0,0,0); border-radius: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.abandonar = QtWidgets.QPushButton(parent=self.gridWidget2)
        self.abandonar.setStyleSheet("border-style: solid;border-width:2px; border-color: rgb(0,0,0); color: rgb(0,0,0); border-radius: 5px;\n"
"background-color: rgb(171, 219, 205);")
        self.abandonar.setObjectName("abandonar")
        self.abandonar.clicked.connect(self.abandonarPartida)
        self.gridLayout_2.addWidget(self.abandonar, 2, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.gridWidget2)
        self.Mochila = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.Mochila.setMaximumSize(QtCore.QSize(150, 150))
        self.Mochila.setStyleSheet("image:url(:/bolsa.png)")
        self.Mochila.setText("")
        self.Mochila.setObjectName("Mochila")
        self.Mochila.clicked.connect(self.cambiarPokemon)
        self.horizontalLayout_3.addWidget(self.Mochila)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalWidget_21 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_21.setMinimumSize(QtCore.QSize(250, 0))
        self.verticalWidget_21.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalWidget_21.setObjectName("verticalWidget_21")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalWidget3 = QtWidgets.QWidget(parent=self.verticalWidget_21)
        self.verticalWidget3.setMinimumSize(QtCore.QSize(240, 0))
        self.verticalWidget3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalWidget3.setStyleSheet("background-color: rgb(201, 143, 143);")
        self.verticalWidget3.setObjectName("verticalWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addWidget(self.verticalWidget3)
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.verticalWidget_21)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(300, 50))
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(parent=self.horizontalWidget_2)
        self.label_18.setMaximumSize(QtCore.QSize(125, 40))
        self.label_18.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.horizontalWidget_2)
        self.textEdit_3.setMaximumSize(QtCore.QSize(220, 40))
        self.textEdit_3.setStyleSheet("border-style: solid;border-width:1px; border-color: rgb(0, 0, 0); background-color: rgb(217, 217, 217); color: rgb(0,0,0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_6.addWidget(self.textEdit_3)
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)
        self.horizontalLayout.addWidget(self.verticalWidget_21)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.leer_datos_correo()
        self.obtener_pokemon(self.label, self.graphicsView)
        self.obtener_pokemon(self.label_2, self.graphicsView_2)
        self.mostrar_imagen(":/leon.png", self.verticalWidget_2)
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)


        pokeball_image = QtGui.QPixmap(":/pokeball.png").scaled(50,50)
        for i in range(3):
            for j in range(2):
                label_pokeball = QtWidgets.QLabel(parent=self.gridWidget2)
                label_pokeball.setPixmap(pokeball_image)
                self.gridLayout_4.addWidget(label_pokeball, i, j)
        
        for i in range(3):
            for j in range(2):
                label_pokeball = QtWidgets.QLabel(parent=self.gridWidget)
                label_pokeball.setPixmap(pokeball_image)
                self.gridLayout_3.addWidget(label_pokeball, i, j)

    def actualizar_hora(self):
        ahora = QDateTime.currentDateTime()
        tiempo_actual = ahora.toString("hh:mm:ss")
        self.label_18.setText(tiempo_actual)
      
    def leer_datos_correo(self):
    
        try:
            with open("correo.json", 'r') as file:
                correo_data = json.load(file)

            genero = correo_data['correo']['genero']
    
            
            if genero.lower() == "chica":
                self.mostrar_imagen(":/maya.png", self.verticalWidget1)
            else:
                self.mostrar_imagen(":/leon.png", self.verticalWidget1)


        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Archivo correo.json no encontrado.")
        except KeyError:
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error", "Clave 'genero' no encontrada en el archivo correo.json.")
            
        
    def mostrar_imagen(self, imagen_path, vertical_widget):
        vertical_widget.setStyleSheet(f"""
            background-image: url({imagen_path});
            background-repeat: no-repeat;
            background-position: center;
        """)        
        vertical_widget.setAutoFillBackground(True)
                
    def obtener_pokemon(self, label, graphicsView, ):

        with open("pokemon_first_generation.json", "r") as json_file:
            pokemon_data = json.load(json_file)
        
        random_pokemon = random.choice(pokemon_data)

        pokemon_name = random_pokemon.get("name", "")
        pokemon_life = random_pokemon.get("stats", {}).get("Hp", "")
        pokemon_type = random_pokemon.get("type", "")

        
        label.setText(
            f"<span style='color: white; font-size: 20px;'>"
            f"&nbsp;&nbsp;&nbsp;Nombre: {pokemon_name}<br>"
            f"&nbsp;&nbsp;&nbsp;Vida: <b><span style='color: green'>{pokemon_life}</span></b><br>"
            f"&nbsp;&nbsp;&nbsp;Tipo: {pokemon_type}"
            "</span>"
        )
           
        image_url = random_pokemon.get("image_url", "")

        response = requests.get(image_url)

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(response.content)

        pixmap = pixmap.scaled(200,200,QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.obtener_movimientos(pokemon_data)

        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)

        graphicsView.setScene(scene)
        graphicsView.setSceneRect(0, 0, pixmap.width(), pixmap.height())
        
        
        
    def obtener_movimientos(self, pokemon_data):

        random_pokemon = random.choice(pokemon_data)
        moves = random_pokemon.get("moves", [])
        random_moves = random.sample(moves, min(4, len(moves)))

        for i, move_name in enumerate(random_moves):
            if i == 0:
                self.pushButton_2.setText(move_name)
            elif i == 1:
                self.pushButton_3.setText(move_name)
            elif i == 2:
                self.pushButton_4.setText(move_name)
            elif i == 3:
                self.pushButton_5.setText(move_name)
    

    def cambiarPokemon(self):
        self.MainWindow.close() 
        from pantalla_cambiar_pokemon import Ui_MainWindow
        self.cambiar = Ui_MainWindow()
        self.cambiar.setupUi(self.MainWindow) 
        self.MainWindow.showMaximized()
        
    def abandonarPartida(self):
        self.MainWindow.close() 
        from seleccion_partida import SelPartida
        self.rapida = SelPartida()
        self.rapida.setupUi(self.MainWindow) 
        self.MainWindow.showMaximized()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.abandonar.setText(_translate("MainWindow", "Abandonar Partida"))
        self.label_18.setText(_translate("MainWindow", "Date Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())