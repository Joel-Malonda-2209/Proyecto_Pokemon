from PySide6 import QtCore, QtGui, QtWidgets
import requests
import json


class PokemonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.setObjectName("pokemon_widget")
        layout = QtWidgets.QVBoxLayout(self)
        layout.setObjectName("pokemon_widget_layout")

        self.img_widget = QtWidgets.QWidget(self)
        self.img_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.img_widget.setObjectName("img_widget")
        self.img_widget_layout = QtWidgets.QVBoxLayout(self.img_widget)
        self.img_widget_layout.setObjectName("img_widget_layout")

        self.img_pokemon = QtWidgets.QGraphicsView(self.img_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.img_pokemon.sizePolicy().hasHeightForWidth())
        self.img_pokemon.setSizePolicy(sizePolicy)
        self.img_pokemon.setObjectName("img_pokemon")
        self.img_widget_layout.addWidget(self.img_pokemon)

        layout.addWidget(self.img_widget)

        self.name_widget = QtWidgets.QWidget(self)
        self.name_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.name_widget.setObjectName("name_widget")
        self.name_widget_layout = QtWidgets.QVBoxLayout(self.name_widget)
        self.name_widget_layout.setObjectName("name_widget_layout")
        self.name_pokemon = QtWidgets.QComboBox(self.name_widget)
        self.name_pokemon.setObjectName("name_pokemon")
        self.name_widget_layout.addWidget(self.name_pokemon)
        layout.addWidget(self.name_widget)

        self.level_type_widget = QtWidgets.QWidget(self)
        self.level_type_widget.setStyleSheet(
            "background-color: rgb(232, 232, 232);")
        self.level_type_widget.setObjectName("level_type_widget")
        self.level_type_layout = QtWidgets.QHBoxLayout(self.level_type_widget)
        self.level_type_layout.setObjectName("level_type_layout")
        self.level_widget = QtWidgets.QVBoxLayout()
        self.level_widget.setObjectName("level_widget")
        self.level = QtWidgets.QLabel(self.level_type_widget)
        self.level.setObjectName("level")
        self.level.setText("Nivel: ")
        self.level_widget.addWidget(self.level)
        self.set_level = QtWidgets.QLabel(self.level_type_widget)
        self.set_level.setText("")
        self.set_level.setObjectName("set_level")

        self.level_widget.addWidget(self.set_level)
        self.level_type_layout.addLayout(self.level_widget)
        self.type_widget = QtWidgets.QVBoxLayout()
        self.type_widget.setObjectName("type_widget")
        self.type = QtWidgets.QLabel(self.level_type_widget)
        self.type.setObjectName("type")
        self.type.setText("Tipo: ")
        self.type_widget.addWidget(self.type)
        self.set_type = QtWidgets.QLabel(self.level_type_widget)
        self.set_type.setText("")
        self.set_type.setObjectName("set_type")
        self.type_widget.addWidget(self.set_type)
        self.level_type_layout.addLayout(self.type_widget)
        layout.addWidget(self.level_type_widget)

        self.ability_widget = QtWidgets.QWidget(self)
        self.ability_widget.setStyleSheet(
            "background-color: rgb(232, 232, 232);")
        self.ability_widget.setObjectName("ability_widget")
        self.ability_layout = QtWidgets.QVBoxLayout(self.ability_widget)
        self.ability_layout.setObjectName("ability_layout")
        self.ability = QtWidgets.QLabel(self.ability_widget)
        self.ability.setObjectName("ability")
        self.ability.setText("Habilidad: ")
        self.ability_layout.addWidget(self.ability)
        self.ability_comboBox = QtWidgets.QComboBox(self.ability_widget)
        self.ability_comboBox.setObjectName("ability_comboBox")
        self.ability_layout.addWidget(self.ability_comboBox)
        layout.addWidget(self.ability_widget)

        self.stats_widget = QtWidgets.QWidget(self)
        self.stats_widget.setStyleSheet(
            "background-color: rgb(232, 232, 232);")
        self.stats_widget.setObjectName("stats_widget")
        self.stats_layout = QtWidgets.QVBoxLayout(self.stats_widget)
        self.stats_layout.setObjectName("stats_layout")
        self.health = QtWidgets.QLabel(self.stats_widget)
        self.health.setObjectName("health")
        self.health.setText("Hp: ")
        self.stats_layout.addWidget(self.health)
        self.atack = QtWidgets.QLabel(self.stats_widget)
        self.atack.setObjectName("atack")
        self.atack.setText("Ataque: ")
        self.stats_layout.addWidget(self.atack)
        self.defense = QtWidgets.QLabel(self.stats_widget)
        self.defense.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.defense.setObjectName("defense")
        self.defense.setText("Defensa: ")
        self.stats_layout.addWidget(self.defense)
        self.move_speed = QtWidgets.QLabel(self.stats_widget)
        self.move_speed.setText("Velocidad: ")
        self.move_speed.setObjectName("move_speed")
        self.stats_layout.addWidget(self.move_speed)
        layout.addWidget(self.stats_widget)

        self.move_widget = QtWidgets.QWidget(self)
        self.move_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.move_widget.setObjectName("move_widget")
        self.move_layout = QtWidgets.QVBoxLayout(self.move_widget)
        self.move_layout.setObjectName("move_layout")
        self.move_1 = QtWidgets.QComboBox(self.move_widget)
        self.move_1.setObjectName("move_1")
        self.move_layout.addWidget(self.move_1)
        self.move_2 = QtWidgets.QComboBox(self.move_widget)
        self.move_2.setObjectName("move_2")
        self.move_layout.addWidget(self.move_2)
        self.move_3 = QtWidgets.QComboBox(self.move_widget)
        self.move_3.setObjectName("move_3")
        self.move_layout.addWidget(self.move_3)
        self.move_4 = QtWidgets.QComboBox(self.move_widget)
        self.move_4.setObjectName("move_4")
        self.move_layout.addWidget(self.move_4)
        layout.addWidget(self.move_widget)


class TeamInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.setObjectName("team_info_widget")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setObjectName("team_info_layout")

        self.team_edit = QtWidgets.QLineEdit(self)
        self.team_edit.setObjectName("team_edit")
        self.team_edit.setText("Equipo")
        layout.addWidget(self.team_edit)

        self.change_team = QtWidgets.QPushButton("Cambiar equipo", self)
        self.change_team.setObjectName("change_team")
        layout.addWidget(self.change_team)

        self.img_first_pokemon = QtWidgets.QGraphicsView(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.img_first_pokemon.sizePolicy().hasHeightForWidth())
        self.img_first_pokemon.setSizePolicy(sizePolicy)
        self.img_first_pokemon.setStyleSheet("")
        self.img_first_pokemon.setObjectName("img_first_pokemon")
        layout.addWidget(self.img_first_pokemon)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 712)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 251, 207);")
        self.centralwidget.setObjectName("centralwidget")
        self.central_widget = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_widget.setObjectName("central_widget")

        self.team_widget = QtWidgets.QWidget(self.centralwidget)
        self.team_widget.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.team_widget.setObjectName("team_widget")
        self.team_layout = QtWidgets.QVBoxLayout(self.team_widget)
        self.team_layout.setObjectName("team_layout")

        self.back_lobby = QtWidgets.QPushButton(
            "Volver atrás", self.team_widget)
        self.back_lobby.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.back_lobby.setObjectName("back_lobby")
        self.back_lobby.clicked.connect(self.volver_a_partidas)
        self.team_layout.addWidget(self.back_lobby)

        self.save_button = QtWidgets.QPushButton(
            "Guardar equipo", self.team_widget)
        self.save_button.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_button_clicked)
        self.team_layout.addWidget(self.save_button)

        self.team_info_widget = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(self.team_info_widget)
        self.team_info_widget2 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(self.team_info_widget2)
        self.team_info_widget3 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(self.team_info_widget3)
        self.team_info_widget4 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(self.team_info_widget4)
        self.central_widget.addWidget(self.team_widget)

        self.pokemon_widget1 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget1)
        self.pokemon_widget2 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget2)
        self.pokemon_widget3 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget3)
        self.pokemon_widget4 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget4)
        self.pokemon_widget5 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget5)
        self.pokemon_widget6 = PokemonWidget(self.centralwidget)
        self.central_widget.addWidget(self.pokemon_widget6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def volver_a_partidas(self):
        self.MainWindow.close()    
        from seleccion_partida import SelPartida
        self.registro_window = SelPartida()
        self.registro_window.setupUi(self.MainWindow) 
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.load_pokemon_data()

    def load_pokemon_data(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_data = [(pokemon['name'].capitalize(), pokemon['url'])
                            for pokemon in data['results']]
            for i in range(6):
                combo_box = getattr(self, f"pokemon_widget{i+1}").name_pokemon
                combo_box.addItems([pokemon[0] for pokemon in pokemon_data])
                combo_box.currentIndexChanged.connect(
                    lambda index, widget_index=i+1: self.update_ability_and_image(index, widget_index, pokemon_data))
        else:
            print("Error al obtener los datos de los Pokémon")

    def update_ability_and_image(self, index, widget_index, pokemon_data):
        pokemon_name, pokemon_url = pokemon_data[index]
        ability_combobox = getattr(
            self, f"pokemon_widget{widget_index}").ability_comboBox
        ability_combobox.clear()
        abilities = self.get_pokemon_abilities(pokemon_url)
        ability_combobox.addItems(abilities)
        pokemon_image_url = self.get_pokemon_image_url(pokemon_url)
        self.load_pokemon_image(pokemon_image_url, widget_index)

        level_label = getattr(self, f"pokemon_widget{widget_index}").set_level
        level_label.setText("100")

        type_label = getattr(self, f"pokemon_widget{widget_index}").set_type
        pokemon_type = self.get_pokemon_type(pokemon_url)
        type_label.setText(pokemon_type)

        stats = self.get_pokemon_stats_at_level_100(pokemon_url)
        stats_widget = getattr(self, f"pokemon_widget{widget_index}")
        stats_widget.health.setText(f"Hp: {stats.get('Hp', 'N/A')}")
        stats_widget.atack.setText(f"Ataque: {stats.get('Attack', 'N/A')}")
        stats_widget.defense.setText(f"Defensa: {stats.get('Defense', 'N/A')}")
        stats_widget.move_speed.setText(
            f"Velocidad: {stats.get('Speed', 'N/A')}")

        response = requests.get(pokemon_url)
        if response.status_code == 200:
            data = response.json()
            self.get_pokemon_move(data, widget_index)
        else:
            print("Error al obtener los movimientos del Pokémon")

        # Asignar la imagen del primer Pokémon al img_first_pokemon en TeamInfoWidget
        if widget_index == 1:
            img_first_pokemon = self.team_info_widget.img_first_pokemon
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(requests.get(pokemon_image_url).content)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(pixmap)
            img_first_pokemon.setScene(scene)
            img_first_pokemon.fitInView(
                scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        else:
            print("")



    def get_pokemon_move(self, data, widget_index):
        moves = data.get("moves", [])
        move_widgets = [
            getattr(self, f"pokemon_widget{widget_index}").move_1,
            getattr(self, f"pokemon_widget{widget_index}").move_2,
            getattr(self, f"pokemon_widget{widget_index}").move_3,
            getattr(self, f"pokemon_widget{widget_index}").move_4,
        ]
        for move_widget, move_name in zip(move_widgets, moves):
            move_widget.clear()
            move_widget.addItems(
                [move["move"]["name"].capitalize() for move in moves])

    def get_pokemon_type(self, pokemon_url):
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            data = response.json()
            types = [type_info['type']['name'].capitalize()
                     for type_info in data['types']]
            return '/'.join(types)
        else:
            print("Error al obtener el tipo del Pokémon")
            return ""

    def get_pokemon_stats_at_level_100(self, pokemon_url):
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            data = response.json()
            stats = {}
            for stat in data['stats']:
                stat_name = stat['stat']['name'].capitalize()
                base_stat = stat['base_stat']
                level_100_stat = int(((2 * base_stat + 31) * 100 / 100) + 5)
                stats[stat_name] = level_100_stat
            return stats
        else:
            print("Error al obtener las estadísticas del Pokémon")
            return {}

    def get_pokemon_abilities(self, pokemon_url):
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            data = response.json()
            abilities = [ability['ability']['name'].capitalize()
                         for ability in data['abilities']]
            return abilities
        else:
            print("Error al obtener las habilidades del Pokémon")
            return []

    def get_pokemon_image_url(self, pokemon_url):
        response = requests.get(pokemon_url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            print("Error al obtener la URL de la imagen del Pokémon")
            return ""

    def load_pokemon_image(self, url, widget_index):
        if url:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(requests.get(url).content)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(pixmap)
            graphics_view = getattr(
                self, f"pokemon_widget{widget_index}").img_pokemon
            graphics_view.setScene(scene)
            graphics_view.fitInView(
                scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        else:
            print("No se pudo cargar la imagen del Pokémon")


        
    def save_button_clicked(self):
        team_name = self.team_info_widget.team_edit.text()
        team_data = {'team_name': team_name, 'pokemon_team': []}
        for i in range(1, 7):
            pokemon_widget = getattr(self, f"pokemon_widget{i}")
            pokemon_info = {
                'name': pokemon_widget.name_pokemon.currentText(),
                'ability': pokemon_widget.ability_comboBox.currentText(),
                'level': pokemon_widget.set_level.text(),
                'type': pokemon_widget.set_type.text(),
                'moves': [pokemon_widget.move_1.currentText(),
                        pokemon_widget.move_2.currentText(),
                        pokemon_widget.move_3.currentText(),
                        pokemon_widget.move_4.currentText()],
            }
            team_data['pokemon_team'].append(pokemon_info)

        with open('team_data.json', 'w') as file:
            json.dump(team_data, file)



    def save_team_data(self, team_data):
        with open('team_data.json', 'w') as file:
            json.dump(team_data, file)


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
