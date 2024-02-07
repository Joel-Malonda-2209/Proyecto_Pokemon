from PySide6 import QtCore, QtGui, QtWidgets
import requests
import json
import os

class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(MainWindow)
        self.asignar_pokemon()
        self.asignar_datos()

    def guardar_en_json(self):
        data = {"name": self.comboBox.currentText()}
        with open("datos_pokemon.json", "w") as json_file:
            json.dump(data, json_file)

    def actualizar_imagen_pokemon(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView.setScene(scene)
        self.graphicsView.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.graphicsView_8.setScene(scene)
        self.graphicsView_8.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox = QtWidgets.QComboBox(parent=None)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(nombre_pokemons)

        self.comboBox.currentIndexChanged.connect(self.asignar_datos)
        
        return self.comboBox
    
    def asignar_datos(self):
        pokemon_seleccionado = self.comboBox.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_11.clear()  

        if "abilities" in data:
            habilidades = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_11.addItems(habilidades)
        
        self.obtener_movimientos(data)
        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas(data,nivel)

        self.mostrar_estadisticas(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_66.setText(str(nivel))
        self.label_68.setText(tipo)


        self.actualizar_imagen_pokemon(data)
    
    def obtener_estadisticas(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed


    def mostrar_estadisticas(self, hp, attack, defense, speed):
        self.label_71.setText(f"HP: {hp}")
        self.label_72.setText(f"Ataque: {attack}")
        self.label_73.setText(f"Defensa: {defense}")
        self.label_74.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos(self, data):
        self.comboBox_29.clear()
        self.comboBox_30.clear()
        self.comboBox_31.clear()
        self.comboBox_32.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_29.addItems(movimientos)
            self.comboBox_30.addItems(movimientos)
            self.comboBox_31.addItems(movimientos)
            self.comboBox_32.addItems(movimientos)
            
    def actualizar_imagen_pokemon2(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView_7.setScene(scene)
        self.graphicsView_7.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon2(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox2 = QtWidgets.QComboBox(parent=None)
        self.comboBox2.setObjectName("comboBox")
        self.comboBox2.addItems(nombre_pokemons)

        self.comboBox2.currentIndexChanged.connect(self.asignar_datos2)
        
        return self.comboBox2
    
    def asignar_datos2(self):
        pokemon_seleccionado = self.comboBox2.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_12.clear()  

        if "abilities" in data:
            habilidades2 = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_12.addItems(habilidades2)
        
        self.obtener_movimientos2(data)

        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas2(data,nivel)
        self.mostrar_estadisticas2(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_56.setText(str(nivel))
        self.label_58.setText(tipo)


        self.actualizar_imagen_pokemon2(data)
    
    def obtener_estadisticas2(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed

    def mostrar_estadisticas2(self, hp, attack, defense, speed):
        self.label_61.setText(f"HP: {hp}")
        self.label_62.setText(f"Ataque: {attack}")
        self.label_63.setText(f"Defensa: {defense}")
        self.label_64.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos2(self, data):
        self.comboBox_25.clear()
        self.comboBox_26.clear()
        self.comboBox_27.clear()
        self.comboBox_28.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_25.addItems(movimientos)
            self.comboBox_26.addItems(movimientos)
            self.comboBox_27.addItems(movimientos)
            self.comboBox_28.addItems(movimientos)
            
    def actualizar_imagen_pokemon3(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView_6.setScene(scene)
        self.graphicsView_6.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon3(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox3 = QtWidgets.QComboBox(parent=None)
        self.comboBox3.setObjectName("comboBox")
        self.comboBox3.addItems(nombre_pokemons)

        self.comboBox3.currentIndexChanged.connect(self.asignar_datos3)
        
        return self.comboBox3
    
    def asignar_datos3(self):
        pokemon_seleccionado = self.comboBox3.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_33.clear()  

        if "abilities" in data:
            habilidades3 = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_33.addItems(habilidades3)
        
        self.obtener_movimientos3(data)

        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas3(data,nivel)
        self.mostrar_estadisticas3(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_46.setText(str(nivel))
        self.label_48.setText(tipo)


        self.actualizar_imagen_pokemon3(data)
    
    def obtener_estadisticas3(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed

    def mostrar_estadisticas3(self, hp, attack, defense, speed):
        self.label_51.setText(f"HP: {hp}")
        self.label_52.setText(f"Ataque: {attack}")
        self.label_53.setText(f"Defensa: {defense}")
        self.label_54.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos3(self, data):
        self.comboBox_21.clear()
        self.comboBox_22.clear()
        self.comboBox_23.clear()
        self.comboBox_24.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_21.addItems(movimientos)
            self.comboBox_22.addItems(movimientos)
            self.comboBox_23.addItems(movimientos)
            self.comboBox_24.addItems(movimientos)
            
    def actualizar_imagen_pokemon4(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView_5.setScene(scene)
        self.graphicsView_5.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon4(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox4 = QtWidgets.QComboBox(parent=None)
        self.comboBox4.setObjectName("comboBox")
        self.comboBox4.addItems(nombre_pokemons)

        self.comboBox4.currentIndexChanged.connect(self.asignar_datos4)
        
        return self.comboBox4
    
    def asignar_datos4(self):
        pokemon_seleccionado = self.comboBox4.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_34.clear()  

        if "abilities" in data:
            habilidades3 = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_34.addItems(habilidades3)
        
        self.obtener_movimientos4(data)

        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas4(data,nivel)
        self.mostrar_estadisticas4(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_36.setText(str(nivel))
        self.label_38.setText(tipo)


        self.actualizar_imagen_pokemon4(data)
    
    def obtener_estadisticas4(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed

    def mostrar_estadisticas4(self, hp, attack, defense, speed):
        self.label_41.setText(f"HP: {hp}")
        self.label_42.setText(f"Ataque: {attack}")
        self.label_43.setText(f"Defensa: {defense}")
        self.label_44.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos4(self, data):
        self.comboBox_17.clear()
        self.comboBox_18.clear()
        self.comboBox_19.clear()
        self.comboBox_20.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_17.addItems(movimientos)
            self.comboBox_18.addItems(movimientos)
            self.comboBox_19.addItems(movimientos)
            self.comboBox_20.addItems(movimientos)
            
    def actualizar_imagen_pokemon5(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView_4.setScene(scene)
        self.graphicsView_4.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon5(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox5 = QtWidgets.QComboBox(parent=None)
        self.comboBox5.setObjectName("comboBox")
        self.comboBox5.addItems(nombre_pokemons)

        self.comboBox5.currentIndexChanged.connect(self.asignar_datos5)
        
        return self.comboBox5
    
    def asignar_datos5(self):
        pokemon_seleccionado = self.comboBox5.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_35.clear()  

        if "abilities" in data:
            habilidades3 = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_35.addItems(habilidades3)
        
        self.obtener_movimientos5(data)

        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas5(data,nivel)
        self.mostrar_estadisticas5(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_10.setText(str(nivel))
        self.label_16.setText(tipo)


        self.actualizar_imagen_pokemon5(data)
    
    def obtener_estadisticas5(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed

    def mostrar_estadisticas5(self, hp, attack, defense, speed):
        self.label_31.setText(f"HP: {hp}")
        self.label_32.setText(f"Ataque: {attack}")
        self.label_33.setText(f"Defensa: {defense}")
        self.label_34.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos5(self, data):
        self.comboBox_13.clear()
        self.comboBox_14.clear()
        self.comboBox_15.clear()
        self.comboBox_16.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_13.addItems(movimientos)
            self.comboBox_14.addItems(movimientos)
            self.comboBox_15.addItems(movimientos)
            self.comboBox_16.addItems(movimientos)
            
    def actualizar_imagen_pokemon6(self, data):
        sprites = data["sprites"]
        image_url = sprites["front_default"]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        
        scene = QtWidgets.QGraphicsScene()
        pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.fitInView(pixmap_item, QtCore.Qt.AspectRatioMode.KeepAspectRatio)


    def asignar_pokemon6(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        data = response.json()

        nombre_pokemons = [pokemon["name"].capitalize() for pokemon in data["results"]]
        
        self.comboBox6 = QtWidgets.QComboBox(parent=None)
        self.comboBox6.setObjectName("comboBox")
        self.comboBox6.addItems(nombre_pokemons)

        self.comboBox6.currentIndexChanged.connect(self.asignar_datos6)
        
        return self.comboBox6
    
    def asignar_datos6(self):
        pokemon_seleccionado = self.comboBox6.currentText().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_seleccionado}"
        response = requests.get(url)
        data = response.json()

        self.comboBox_36.clear()  

        if "abilities" in data:
            habilidades6 = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]
            self.comboBox_36.addItems(habilidades6)
        
        self.obtener_movimientos6(data)

        nivel = 100
        hp, attack, defense, speed = self.obtener_estadisticas6(data,nivel)
        self.mostrar_estadisticas6(hp, attack, defense, speed)

        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]
        tipo = '/'.join(tipos)

        self.label_6.setText(str(nivel))
        self.label_8.setText(tipo)


        self.actualizar_imagen_pokemon6(data)
    
    def obtener_estadisticas6(self, data, nivel):
        stats = data["stats"]
        hp, attack, defense, speed = 0,0,0,0
        for stat in stats:
            base_stat = stat["base_stat"]
            if stat["stat"]["name"] == "hp":
                hp = ((base_stat * 2 * nivel) / 100) + nivel + 10
            else:
                if stat["stat"]["name"] == "attack":
                    attack = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "defense":
                    defense = ((base_stat * 2 * nivel) / 100) + 5
                elif stat["stat"]["name"] == "speed":
                    speed = ((base_stat * 2 * nivel) / 100) + 5
        return hp, attack, defense, speed

    def mostrar_estadisticas6(self, hp, attack, defense, speed):
        self.label_19.setText(f"HP: {hp}")
        self.label_20.setText(f"Ataque: {attack}")
        self.label_21.setText(f"Defensa: {defense}")
        self.label_22.setText(f"Velocidad: {speed}")
    
    def obtener_movimientos6(self, data):
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        self.comboBox_7.clear()
        self.comboBox_8.clear()

        if "moves" in data:
            movimientos = [move["move"]["name"].capitalize() for move in data["moves"]]
            self.comboBox_5.addItems(movimientos)
            self.comboBox_6.addItems(movimientos)
            self.comboBox_7.addItems(movimientos)
            self.comboBox_8.addItems(movimientos)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1610, 775)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.volverLobby = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        self.volverLobby.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.volverLobby.setObjectName("volverLobby")
        self.verticalLayout_5.addWidget(self.volverLobby)
        self.guardarDatos = QtWidgets.QPushButton(parent=self.horizontalWidget_2)
        self.guardarDatos.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.guardarDatos.setObjectName("guardarDatos")
        self.guardarDatos.setText("Guardar")
        self.verticalLayout_5.addWidget(self.guardarDatos)
        self.guardarDatos.clicked.connect(self.guardar_en_json)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalWidget_13 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.verticalWidget_13.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.verticalWidget_13.setObjectName("verticalWidget_13")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.verticalWidget_13)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.verticalWidget_13)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_36.addWidget(self.lineEdit_7)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalWidget_13)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_36.addWidget(self.pushButton)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.verticalWidget_13)
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_16.addWidget(self.graphicsView)
        self.verticalLayout_36.addLayout(self.horizontalLayout_16)
        self.verticalLayout_7.addWidget(self.verticalWidget_13)
        self.verticalWidget_16 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.verticalWidget_16.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.verticalWidget_16.setObjectName("verticalWidget_16")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.verticalWidget_16)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.verticalWidget_16)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_39.addWidget(self.lineEdit_10)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalWidget_16)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_39.addWidget(self.pushButton_2)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.graphicsView_11 = QtWidgets.QGraphicsView(parent=self.verticalWidget_16)
        self.graphicsView_11.setStyleSheet("")
        self.graphicsView_11.setObjectName("graphicsView_11")
        self.horizontalLayout_19.addWidget(self.graphicsView_11)
        self.verticalLayout_39.addLayout(self.horizontalLayout_19)
        self.verticalLayout_7.addWidget(self.verticalWidget_16)
        self.verticalWidget_26 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.verticalWidget_26.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.verticalWidget_26.setObjectName("verticalWidget_26")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.verticalWidget_26)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.verticalWidget_26)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_68.addWidget(self.lineEdit_12)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalWidget_26)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_68.addWidget(self.pushButton_3)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.graphicsView_13 = QtWidgets.QGraphicsView(parent=self.verticalWidget_26)
        self.graphicsView_13.setStyleSheet("")
        self.graphicsView_13.setObjectName("graphicsView_13")
        self.horizontalLayout_29.addWidget(self.graphicsView_13)
        self.verticalLayout_68.addLayout(self.horizontalLayout_29)
        self.verticalLayout_7.addWidget(self.verticalWidget_26)
        self.verticalWidget_25 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.verticalWidget_25.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.verticalWidget_25.setObjectName("verticalWidget_25")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.verticalWidget_25)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.verticalWidget_25)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_67.addWidget(self.lineEdit_11)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalWidget_25)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_67.addWidget(self.pushButton_4)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.graphicsView_12 = QtWidgets.QGraphicsView(parent=self.verticalWidget_25)
        self.graphicsView_12.setStyleSheet("")
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.horizontalLayout_28.addWidget(self.graphicsView_12)
        self.verticalLayout_67.addLayout(self.horizontalLayout_28)
        self.verticalLayout_7.addWidget(self.verticalWidget_25)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalWidget_23 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_23.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_23.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_23.setObjectName("verticalWidget_23")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.verticalWidget_23)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.scrollArea_8 = QtWidgets.QScrollArea(parent=self.verticalWidget_23)
        self.scrollArea_8.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_8.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 203, 735))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.horizontalWidget_15 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_8)
        self.horizontalWidget_15.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_15.setObjectName("horizontalWidget_15")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalWidget_15)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.graphicsView_8 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_15)
        self.graphicsView_8.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_8.setStyleSheet("")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.verticalLayout_62.addWidget(self.graphicsView_8)
        self.verticalLayout_62.addWidget(self.asignar_pokemon())
        self.horizontalWidget_16 = QtWidgets.QWidget(parent=self.horizontalWidget_15)
        self.horizontalWidget_16.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_16.setObjectName("horizontalWidget_16")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.horizontalWidget_16)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout()
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.label_65 = QtWidgets.QLabel(parent=self.horizontalWidget_16)
        self.label_65.setObjectName("label_65")
        self.verticalLayout_63.addWidget(self.label_65)
        self.label_66 = QtWidgets.QLabel(parent=self.horizontalWidget_16)
        self.label_66.setText("")
        self.label_66.setObjectName("label_66")
        self.verticalLayout_63.addWidget(self.label_66)
        self.horizontalLayout_27.addLayout(self.verticalLayout_63)
        self.verticalLayout_64 = QtWidgets.QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.label_67 = QtWidgets.QLabel(parent=self.horizontalWidget_16)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_64.addWidget(self.label_67)
        self.label_68 = QtWidgets.QLabel(parent=self.horizontalWidget_16)
        self.label_68.setText("")
        self.label_68.setObjectName("label_68")
        self.verticalLayout_64.addWidget(self.label_68)
        self.horizontalLayout_27.addLayout(self.verticalLayout_64)
        self.verticalLayout_62.addWidget(self.horizontalWidget_16)
        self.widget_7 = QtWidgets.QWidget(parent=self.horizontalWidget_15)
        self.widget_7.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.label_69 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_65.addWidget(self.label_69)
        self.comboBox_11 = QtWidgets.QComboBox(parent=self.widget_7)
        self.comboBox_11.setObjectName("comboBox_11")
        self.verticalLayout_65.addWidget(self.comboBox_11)
        self.verticalLayout_62.addWidget(self.widget_7)
        self.verticalWidget_24 = QtWidgets.QWidget(parent=self.horizontalWidget_15)
        self.verticalWidget_24.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_24.setObjectName("verticalWidget_24")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.verticalWidget_24)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.label_71 = QtWidgets.QLabel(parent=self.verticalWidget_24)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_66.addWidget(self.label_71)
        self.label_72 = QtWidgets.QLabel(parent=self.verticalWidget_24)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_66.addWidget(self.label_72)
        self.label_73 = QtWidgets.QLabel(parent=self.verticalWidget_24)
        self.label_73.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_73.setObjectName("label_73")
        self.verticalLayout_66.addWidget(self.label_73)
        self.label_74 = QtWidgets.QLabel(parent=self.verticalWidget_24)
        self.label_74.setObjectName("label_74")
        self.verticalLayout_66.addWidget(self.label_74)
        self.verticalLayout_62.addWidget(self.verticalWidget_24)
        self.comboBox_29 = QtWidgets.QComboBox(parent=self.horizontalWidget_15)
        self.comboBox_29.setObjectName("comboBox_29")
        self.verticalLayout_62.addWidget(self.comboBox_29)
        self.comboBox_30 = QtWidgets.QComboBox(parent=self.horizontalWidget_15)
        self.comboBox_30.setObjectName("comboBox_30")
        self.verticalLayout_62.addWidget(self.comboBox_30)
        self.comboBox_31 = QtWidgets.QComboBox(parent=self.horizontalWidget_15)
        self.comboBox_31.setObjectName("comboBox_31")
        self.verticalLayout_62.addWidget(self.comboBox_31)
        self.comboBox_32 = QtWidgets.QComboBox(parent=self.horizontalWidget_15)
        self.comboBox_32.setObjectName("comboBox_32")
        self.verticalLayout_62.addWidget(self.comboBox_32)
        self.horizontalLayout_26.addLayout(self.verticalLayout_62)
        self.verticalLayout_61.addWidget(self.horizontalWidget_15)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_60.addWidget(self.scrollArea_8)
        self.horizontalLayout_7.addWidget(self.verticalWidget_23)
        self.verticalWidget_21 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_21.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_21.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_21.setObjectName("verticalWidget_21")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.scrollArea_7 = QtWidgets.QScrollArea(parent=self.verticalWidget_21)
        self.scrollArea_7.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_7.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 202, 735))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.horizontalWidget_13 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_7)
        self.horizontalWidget_13.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_13.setObjectName("horizontalWidget_13")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.horizontalWidget_13)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout()
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.graphicsView_7 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_13)
        self.graphicsView_7.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_7.setStyleSheet("")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.verticalLayout_55.addWidget(self.graphicsView_7)
        self.verticalLayout_55.addWidget(self.asignar_pokemon2())
        self.horizontalWidget_14 = QtWidgets.QWidget(parent=self.horizontalWidget_13)
        self.horizontalWidget_14.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalWidget_14)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout()
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_55 = QtWidgets.QLabel(parent=self.horizontalWidget_14)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_56.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(parent=self.horizontalWidget_14)
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.verticalLayout_56.addWidget(self.label_56)
        self.horizontalLayout_25.addLayout(self.verticalLayout_56)
        self.verticalLayout_57 = QtWidgets.QVBoxLayout()
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_57 = QtWidgets.QLabel(parent=self.horizontalWidget_14)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_57.addWidget(self.label_57)
        self.label_58 = QtWidgets.QLabel(parent=self.horizontalWidget_14)
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.verticalLayout_57.addWidget(self.label_58)
        self.horizontalLayout_25.addLayout(self.verticalLayout_57)
        self.verticalLayout_55.addWidget(self.horizontalWidget_14)
        self.widget_6 = QtWidgets.QWidget(parent=self.horizontalWidget_13)
        self.widget_6.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.label_59 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_58.addWidget(self.label_59)
        self.comboBox_12 = QtWidgets.QComboBox(parent=self.widget_6)
        self.comboBox_12.setObjectName("comboBox_12")
        self.verticalLayout_58.addWidget(self.comboBox_12)
        self.verticalLayout_55.addWidget(self.widget_6)
        self.verticalWidget_22 = QtWidgets.QWidget(parent=self.horizontalWidget_13)
        self.verticalWidget_22.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_22.setObjectName("verticalWidget_22")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.verticalWidget_22)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_61 = QtWidgets.QLabel(parent=self.verticalWidget_22)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_59.addWidget(self.label_61)
        self.label_62 = QtWidgets.QLabel(parent=self.verticalWidget_22)
        self.label_62.setObjectName("label_62")
        self.verticalLayout_59.addWidget(self.label_62)
        self.label_63 = QtWidgets.QLabel(parent=self.verticalWidget_22)
        self.label_63.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_63.setObjectName("label_63")
        self.verticalLayout_59.addWidget(self.label_63)
        self.label_64 = QtWidgets.QLabel(parent=self.verticalWidget_22)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_59.addWidget(self.label_64)
        self.verticalLayout_55.addWidget(self.verticalWidget_22)
        self.comboBox_25 = QtWidgets.QComboBox(parent=self.horizontalWidget_13)
        self.comboBox_25.setObjectName("comboBox_25")
        self.verticalLayout_55.addWidget(self.comboBox_25)
        self.comboBox_26 = QtWidgets.QComboBox(parent=self.horizontalWidget_13)
        self.comboBox_26.setObjectName("comboBox_26")
        self.verticalLayout_55.addWidget(self.comboBox_26)
        self.comboBox_27 = QtWidgets.QComboBox(parent=self.horizontalWidget_13)
        self.comboBox_27.setObjectName("comboBox_27")
        self.verticalLayout_55.addWidget(self.comboBox_27)
        self.comboBox_28 = QtWidgets.QComboBox(parent=self.horizontalWidget_13)
        self.comboBox_28.setObjectName("comboBox_28")
        self.verticalLayout_55.addWidget(self.comboBox_28)
        self.horizontalLayout_24.addLayout(self.verticalLayout_55)
        self.verticalLayout_54.addWidget(self.horizontalWidget_13)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_53.addWidget(self.scrollArea_7)
        self.horizontalLayout_7.addWidget(self.verticalWidget_21)
        self.verticalWidget_19 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_19.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_19.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_19.setObjectName("verticalWidget_19")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.verticalWidget_19)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.scrollArea_6 = QtWidgets.QScrollArea(parent=self.verticalWidget_19)
        self.scrollArea_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_6.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 202, 735))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.horizontalWidget_11 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_6)
        self.horizontalWidget_11.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_11.setObjectName("horizontalWidget_11")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalWidget_11)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.graphicsView_6 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_11)
        self.graphicsView_6.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_6.setStyleSheet("")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.verticalLayout_48.addWidget(self.graphicsView_6)
        self.verticalLayout_48.addWidget(self.asignar_pokemon3())
        self.horizontalWidget_12 = QtWidgets.QWidget(parent=self.horizontalWidget_11)
        self.horizontalWidget_12.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_12.setObjectName("horizontalWidget_12")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalWidget_12)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_45 = QtWidgets.QLabel(parent=self.horizontalWidget_12)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_49.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(parent=self.horizontalWidget_12)
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.verticalLayout_49.addWidget(self.label_46)
        self.horizontalLayout_23.addLayout(self.verticalLayout_49)
        self.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.label_47 = QtWidgets.QLabel(parent=self.horizontalWidget_12)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_50.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(parent=self.horizontalWidget_12)
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.verticalLayout_50.addWidget(self.label_48)
        self.horizontalLayout_23.addLayout(self.verticalLayout_50)
        self.verticalLayout_48.addWidget(self.horizontalWidget_12)
        self.widget_5 = QtWidgets.QWidget(parent=self.horizontalWidget_11)
        self.widget_5.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_49 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_51.addWidget(self.label_49)
        self.comboBox_33 = QtWidgets.QComboBox(parent=self.widget_5)
        self.comboBox_33.setObjectName("comboBox_33")
        self.verticalLayout_51.addWidget(self.comboBox_33)
        self.verticalLayout_48.addWidget(self.widget_5)
        self.verticalWidget_20 = QtWidgets.QWidget(parent=self.horizontalWidget_11)
        self.verticalWidget_20.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_20.setObjectName("verticalWidget_20")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.verticalWidget_20)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.label_51 = QtWidgets.QLabel(parent=self.verticalWidget_20)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_52.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(parent=self.verticalWidget_20)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_52.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(parent=self.verticalWidget_20)
        self.label_53.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_53.setObjectName("label_53")
        self.verticalLayout_52.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(parent=self.verticalWidget_20)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_52.addWidget(self.label_54)
        self.verticalLayout_48.addWidget(self.verticalWidget_20)
        self.comboBox_21 = QtWidgets.QComboBox(parent=self.horizontalWidget_11)
        self.comboBox_21.setObjectName("comboBox_21")
        self.verticalLayout_48.addWidget(self.comboBox_21)
        self.comboBox_22 = QtWidgets.QComboBox(parent=self.horizontalWidget_11)
        self.comboBox_22.setObjectName("comboBox_22")
        self.verticalLayout_48.addWidget(self.comboBox_22)
        self.comboBox_23 = QtWidgets.QComboBox(parent=self.horizontalWidget_11)
        self.comboBox_23.setObjectName("comboBox_23")
        self.verticalLayout_48.addWidget(self.comboBox_23)
        self.comboBox_24 = QtWidgets.QComboBox(parent=self.horizontalWidget_11)
        self.comboBox_24.setObjectName("comboBox_24")
        self.verticalLayout_48.addWidget(self.comboBox_24)
        self.horizontalLayout_22.addLayout(self.verticalLayout_48)
        self.verticalLayout_47.addWidget(self.horizontalWidget_11)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_46.addWidget(self.scrollArea_6)
        self.horizontalLayout_7.addWidget(self.verticalWidget_19)
        self.verticalWidget_17 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_17.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_17.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_17.setObjectName("verticalWidget_17")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_17)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_5 = QtWidgets.QScrollArea(parent=self.verticalWidget_17)
        self.scrollArea_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_5.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 202, 735))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.horizontalWidget_9 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_5)
        self.horizontalWidget_9.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_9.setObjectName("horizontalWidget_9")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalWidget_9)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.graphicsView_5 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_9)
        self.graphicsView_5.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_5.setStyleSheet("")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.verticalLayout_41.addWidget(self.graphicsView_5)
        self.verticalLayout_41.addWidget(self.asignar_pokemon4())
        self.horizontalWidget_10 = QtWidgets.QWidget(parent=self.horizontalWidget_9)
        self.horizontalWidget_10.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_10.setObjectName("horizontalWidget_10")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalWidget_10)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_35 = QtWidgets.QLabel(parent=self.horizontalWidget_10)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_42.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(parent=self.horizontalWidget_10)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_42.addWidget(self.label_36)
        self.horizontalLayout_21.addLayout(self.verticalLayout_42)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.label_37 = QtWidgets.QLabel(parent=self.horizontalWidget_10)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_43.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(parent=self.horizontalWidget_10)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_43.addWidget(self.label_38)
        self.horizontalLayout_21.addLayout(self.verticalLayout_43)
        self.verticalLayout_41.addWidget(self.horizontalWidget_10)
        self.widget_4 = QtWidgets.QWidget(parent=self.horizontalWidget_9)
        self.widget_4.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_39 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_44.addWidget(self.label_39)
        self.comboBox_34 = QtWidgets.QComboBox(parent=self.widget_4)
        self.comboBox_34.setObjectName("comboBox_34")
        self.verticalLayout_44.addWidget(self.comboBox_34)
        self.verticalLayout_41.addWidget(self.widget_4)
        self.verticalWidget_18 = QtWidgets.QWidget(parent=self.horizontalWidget_9)
        self.verticalWidget_18.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_18.setObjectName("verticalWidget_18")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.verticalWidget_18)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_41 = QtWidgets.QLabel(parent=self.verticalWidget_18)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_45.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(parent=self.verticalWidget_18)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_45.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(parent=self.verticalWidget_18)
        self.label_43.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_45.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(parent=self.verticalWidget_18)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_45.addWidget(self.label_44)
        self.verticalLayout_41.addWidget(self.verticalWidget_18)
        self.comboBox_17 = QtWidgets.QComboBox(parent=self.horizontalWidget_9)
        self.comboBox_17.setObjectName("comboBox_17")
        self.verticalLayout_41.addWidget(self.comboBox_17)
        self.comboBox_18 = QtWidgets.QComboBox(parent=self.horizontalWidget_9)
        self.comboBox_18.setObjectName("comboBox_18")
        self.verticalLayout_41.addWidget(self.comboBox_18)
        self.comboBox_19 = QtWidgets.QComboBox(parent=self.horizontalWidget_9)
        self.comboBox_19.setObjectName("comboBox_19")
        self.verticalLayout_41.addWidget(self.comboBox_19)
        self.comboBox_20 = QtWidgets.QComboBox(parent=self.horizontalWidget_9)
        self.comboBox_20.setObjectName("comboBox_20")
        self.verticalLayout_41.addWidget(self.comboBox_20)
        self.horizontalLayout_20.addLayout(self.verticalLayout_41)
        self.verticalLayout_40.addWidget(self.horizontalWidget_9)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.addWidget(self.scrollArea_5)
        self.horizontalLayout_7.addWidget(self.verticalWidget_17)
        self.verticalWidget_11 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_11.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_11.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_11.setObjectName("verticalWidget_11")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_4 = QtWidgets.QScrollArea(parent=self.verticalWidget_11)
        self.scrollArea_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_4.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 203, 735))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalWidget_4 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_4)
        self.horizontalWidget_4.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.graphicsView_4 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_4)
        self.graphicsView_4.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_4.setStyleSheet("")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_31.addWidget(self.graphicsView_4)
        self.verticalLayout_31.addWidget(self.asignar_pokemon5())
        self.horizontalWidget_8 = QtWidgets.QWidget(parent=self.horizontalWidget_4)
        self.horizontalWidget_8.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_8.setObjectName("horizontalWidget_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_9 = QtWidgets.QLabel(parent=self.horizontalWidget_8)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_32.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.horizontalWidget_8)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_32.addWidget(self.label_10)
        self.horizontalLayout_15.addLayout(self.verticalLayout_32)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_15 = QtWidgets.QLabel(parent=self.horizontalWidget_8)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_33.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(parent=self.horizontalWidget_8)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_33.addWidget(self.label_16)
        self.horizontalLayout_15.addLayout(self.verticalLayout_33)
        self.verticalLayout_31.addWidget(self.horizontalWidget_8)
        self.widget_3 = QtWidgets.QWidget(parent=self.horizontalWidget_4)
        self.widget_3.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_17 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_34.addWidget(self.label_17)
        self.comboBox_35 = QtWidgets.QComboBox(parent=self.widget_3)
        self.comboBox_35.setObjectName("comboBox_35")
        self.verticalLayout_34.addWidget(self.comboBox_35)
        self.verticalLayout_31.addWidget(self.widget_3)
        self.verticalWidget_12 = QtWidgets.QWidget(parent=self.horizontalWidget_4)
        self.verticalWidget_12.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_12.setObjectName("verticalWidget_12")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.verticalWidget_12)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_31 = QtWidgets.QLabel(parent=self.verticalWidget_12)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_35.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(parent=self.verticalWidget_12)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_35.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(parent=self.verticalWidget_12)
        self.label_33.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_35.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(parent=self.verticalWidget_12)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_35.addWidget(self.label_34)
        self.verticalLayout_31.addWidget(self.verticalWidget_12)
        self.comboBox_13 = QtWidgets.QComboBox(parent=self.horizontalWidget_4)
        self.comboBox_13.setObjectName("comboBox_13")
        self.verticalLayout_31.addWidget(self.comboBox_13)
        self.comboBox_14 = QtWidgets.QComboBox(parent=self.horizontalWidget_4)
        self.comboBox_14.setObjectName("comboBox_14")
        self.verticalLayout_31.addWidget(self.comboBox_14)
        self.comboBox_15 = QtWidgets.QComboBox(parent=self.horizontalWidget_4)
        self.comboBox_15.setObjectName("comboBox_15")
        self.verticalLayout_31.addWidget(self.comboBox_15)
        self.comboBox_16 = QtWidgets.QComboBox(parent=self.horizontalWidget_4)
        self.comboBox_16.setObjectName("comboBox_16")
        self.verticalLayout_31.addWidget(self.comboBox_16)
        self.horizontalLayout_14.addLayout(self.verticalLayout_31)
        self.verticalLayout_30.addWidget(self.horizontalWidget_4)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.addWidget(self.scrollArea_4)
        self.horizontalLayout_7.addWidget(self.verticalWidget_11)
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalWidget_2.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.verticalWidget_2)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_2.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 202, 735))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalWidget_3 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.horizontalWidget_3.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.horizontalWidget_3)
        self.graphicsView_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.graphicsView_2.setStyleSheet("")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_11.addWidget(self.graphicsView_2)
        self.verticalLayout_11.addWidget(self.asignar_pokemon6())
        self.horizontalWidget_5 = QtWidgets.QWidget(parent=self.horizontalWidget_3)
        self.horizontalWidget_5.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.horizontalWidget_5.setObjectName("horizontalWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalWidget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalWidget_5)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(parent=self.horizontalWidget_5)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.horizontalWidget_5)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_13.addWidget(self.label_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addWidget(self.horizontalWidget_5)
        self.widget = QtWidgets.QWidget(parent=self.horizontalWidget_3)
        self.widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.widget.setObjectName("widget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.comboBox_36 = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox_36.setObjectName("comboBox_36")
        self.verticalLayout_14.addWidget(self.comboBox_36)
        self.verticalLayout_11.addWidget(self.widget)
        self.verticalWidget_5 = QtWidgets.QWidget(parent=self.horizontalWidget_3)
        self.verticalWidget_5.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_19 = QtWidgets.QLabel(parent=self.verticalWidget_5)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(parent=self.verticalWidget_5)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_15.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(parent=self.verticalWidget_5)
        self.label_21.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_15.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(parent=self.verticalWidget_5)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_15.addWidget(self.label_22)
        self.verticalLayout_11.addWidget(self.verticalWidget_5)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.horizontalWidget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout_11.addWidget(self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.horizontalWidget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.verticalLayout_11.addWidget(self.comboBox_6)
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.horizontalWidget_3)
        self.comboBox_7.setObjectName("comboBox_7")
        self.verticalLayout_11.addWidget(self.comboBox_7)
        self.comboBox_8 = QtWidgets.QComboBox(parent=self.horizontalWidget_3)
        self.comboBox_8.setObjectName("comboBox_8")
        self.verticalLayout_11.addWidget(self.comboBox_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_10.addWidget(self.horizontalWidget_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout_7.addWidget(self.verticalWidget_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.volverLobby.setText(_translate("MainWindow", "Volver a Lobby"))
        self.lineEdit_7.setText(_translate("MainWindow", "Equipo 1"))
        self.pushButton.setText(_translate("MainWindow", "Cambiar de equipo"))
        self.lineEdit_10.setText(_translate("MainWindow", "Equipo 2"))
        self.pushButton_2.setText(_translate("MainWindow", "Cambiar de equipo"))
        self.lineEdit_12.setText(_translate("MainWindow", "Equipo 3"))
        self.pushButton_3.setText(_translate("MainWindow", "Cambiar de equipo"))
        self.lineEdit_11.setText(_translate("MainWindow", "Equipo 4"))
        self.pushButton_4.setText(_translate("MainWindow", "Cambiar de equipo"))
        self.label_65.setText(_translate("MainWindow", "Level"))
        self.label_67.setText(_translate("MainWindow", "Type"))
        self.label_69.setText(_translate("MainWindow", "Ability"))
        self.label_71.setText(_translate("MainWindow", "HP: "))
        self.label_72.setText(_translate("MainWindow", "Ataque: "))
        self.label_73.setText(_translate("MainWindow", "Defensa: "))
        self.label_74.setText(_translate("MainWindow", "Velocidad: "))
        self.label_55.setText(_translate("MainWindow", "Level"))
        self.label_57.setText(_translate("MainWindow", "Type"))
        self.label_59.setText(_translate("MainWindow", "Ability"))
        self.label_61.setText(_translate("MainWindow", "HP: "))
        self.label_62.setText(_translate("MainWindow", "Ataque: "))
        self.label_63.setText(_translate("MainWindow", "Defensa: "))
        self.label_64.setText(_translate("MainWindow", "Velocidad: "))
        self.label_45.setText(_translate("MainWindow", "Level"))
        self.label_47.setText(_translate("MainWindow", "Type"))
        self.label_49.setText(_translate("MainWindow", "Ability"))
        self.label_51.setText(_translate("MainWindow", "HP: "))
        self.label_52.setText(_translate("MainWindow", "Ataque: "))
        self.label_53.setText(_translate("MainWindow", "Defensa: "))
        self.label_54.setText(_translate("MainWindow", "Velocidad: "))
        self.label_35.setText(_translate("MainWindow", "Level"))
        self.label_37.setText(_translate("MainWindow", "Type"))
        self.label_39.setText(_translate("MainWindow", "Ability"))
        self.label_41.setText(_translate("MainWindow", "HP: "))
        self.label_42.setText(_translate("MainWindow", "Ataque: "))
        self.label_43.setText(_translate("MainWindow", "Defensa: "))
        self.label_44.setText(_translate("MainWindow", "Velocidad: "))
        self.label_9.setText(_translate("MainWindow", "Level"))
        self.label_15.setText(_translate("MainWindow", "Type"))
        self.label_17.setText(_translate("MainWindow", "Ability"))
        self.label_31.setText(_translate("MainWindow", "HP: "))
        self.label_32.setText(_translate("MainWindow", "Ataque: "))
        self.label_33.setText(_translate("MainWindow", "Defensa: "))
        self.label_34.setText(_translate("MainWindow", "Velocidad: "))
        self.label_5.setText(_translate("MainWindow", "Level"))
        self.label_7.setText(_translate("MainWindow", "Type"))
        self.label_11.setText(_translate("MainWindow", "Ability"))
        self.label_19.setText(_translate("MainWindow", "HP: "))
        self.label_20.setText(_translate("MainWindow", "Ataque: "))
        self.label_21.setText(_translate("MainWindow", "Defensa: "))
        self.label_22.setText(_translate("MainWindow", "Velocidad: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

