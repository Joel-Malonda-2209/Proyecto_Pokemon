from PySide6 import QtCore, QtGui, QtWidgets
import requests
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_pokemon.sizePolicy().hasHeightForWidth())
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
        self.level_type_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.level_type_widget.setObjectName("level_type_widget")
        self.level_type_layout = QtWidgets.QHBoxLayout(self.level_type_widget)
        self.level_type_layout.setObjectName("level_type_layout")
        self.level_widget = QtWidgets.QVBoxLayout()
        self.level_widget.setObjectName("level_widget")
        self.level = QtWidgets.QLabel(self.level_type_widget)
        self.level.setObjectName("level")
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
        self.type_widget.addWidget(self.type)
        self.set_type = QtWidgets.QLabel(self.level_type_widget)
        self.set_type.setText("")
        self.set_type.setObjectName("set_type")
        self.type_widget.addWidget(self.set_type)
        self.level_type_layout.addLayout(self.type_widget)
        layout.addWidget(self.level_type_widget)

        self.ability_widget = QtWidgets.QWidget(self)
        self.ability_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ability_widget.setObjectName("ability_widget")
        self.ability_layout = QtWidgets.QVBoxLayout(self.ability_widget)
        self.ability_layout.setObjectName("ability_layout")
        self.ability = QtWidgets.QLabel(self.ability_widget)
        self.ability.setObjectName("ability")
        self.ability_layout.addWidget(self.ability)
        self.ability_comboBox = QtWidgets.QComboBox(self.ability_widget)
        self.ability_comboBox.setObjectName("ability_comboBox")
        self.ability_layout.addWidget(self.ability_comboBox)
        layout.addWidget(self.ability_widget)

        self.stats_widget = QtWidgets.QWidget(self)
        self.stats_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.stats_widget.setObjectName("stats_widget")
        self.stats_layout = QtWidgets.QVBoxLayout(self.stats_widget)
        self.stats_layout.setObjectName("stats_layout")
        self.health = QtWidgets.QLabel(self.stats_widget)
        self.health.setObjectName("health")
        self.stats_layout.addWidget(self.health)
        self.atack = QtWidgets.QLabel(self.stats_widget)
        self.atack.setObjectName("atack")
        self.stats_layout.addWidget(self.atack)
        self.defense = QtWidgets.QLabel(self.stats_widget)
        self.defense.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.defense.setObjectName("defense")
        self.stats_layout.addWidget(self.defense)
        self.move_speed = QtWidgets.QLabel(self.stats_widget)
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
        layout.addWidget(self.team_edit)

        self.change_team = QtWidgets.QPushButton("Change Team", self)
        self.change_team.setObjectName("change_team")
        layout.addWidget(self.change_team)

        self.img_first_pokemon = QtWidgets.QGraphicsView(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_first_pokemon.sizePolicy().hasHeightForWidth())
        self.img_first_pokemon.setSizePolicy(sizePolicy)
        self.img_first_pokemon.setStyleSheet("")
        self.img_first_pokemon.setObjectName("img_first_pokemon")
        layout.addWidget(self.img_first_pokemon)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 712)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.centralwidget.setObjectName("centralwidget")
        self.central_widget = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_widget.setObjectName("central_widget")

        self.team_widget = QtWidgets.QWidget(self.centralwidget)
        self.team_widget.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.team_widget.setObjectName("team_widget")
        self.team_layout = QtWidgets.QVBoxLayout(self.team_widget)
        self.team_layout.setObjectName("team_layout")

        self.back_lobby = QtWidgets.QPushButton("Back to Lobby", self.team_widget)
        self.back_lobby.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.back_lobby.setObjectName("back_lobby")
        self.team_layout.addWidget(self.back_lobby)

        team_info_widget = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(team_info_widget)
        team_info_widget2 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(team_info_widget2)
        team_info_widget3 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(team_info_widget3)
        team_info_widget4 = TeamInfoWidget(self.team_widget)
        self.team_layout.addWidget(team_info_widget4)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Llamamos a la función que carga los nombres de los Pokémon en el ComboBox
        self.load_pokemon_names()

    def load_pokemon_names(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=151"  # Obtener solo los primeros 151 Pokémon
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_names = [pokemon['name'].capitalize() for pokemon in data['results']]
            for i in range(6):  # Suponiendo que hay 6 Pokémon en la interfaz
                combo_box = getattr(self, f"pokemon_widget{i+1}").name_pokemon
                combo_box.addItems(pokemon_names)

                # Conectar la señal currentIndexChanged del ComboBox de nombres de Pokémon con la función update_ability_combobox
                combo_box.currentIndexChanged.connect(lambda index, widget_index=i+1: self.update_ability_combobox(index, widget_index))

                # Cargar las habilidades del primer Pokémon en el ComboBox de habilidades
                abilities = self.get_pokemon_abilities(pokemon_names[0])
                ability_combobox = getattr(self, f"pokemon_widget{i+1}").ability_comboBox
                ability_combobox.addItems(abilities)
        else:
            print("Error al obtener los nombres de los Pokémon")

    def get_pokemon_abilities(self, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            abilities = [ability['ability']['name'].capitalize() for ability in data['abilities']]
            return abilities
        else:
            print(f"Error al obtener las habilidades del Pokémon {pokemon_name}")
            return []

    def update_ability_combobox(self, index, widget_index):
        # Obtener el nombre del Pokémon seleccionado en el ComboBox de nombres de Pokémon
        combo_box = getattr(self, f"pokemon_widget{widget_index}").name_pokemon
        pokemon_name = combo_box.currentText()

        # Obtener el ComboBox de habilidades correspondiente al widget Pokémon
        ability_combobox = getattr(self, f"pokemon_widget{widget_index}").ability_comboBox

        # Limpiar el ComboBox de habilidades
        ability_combobox.clear()

        # Cargar las habilidades del Pokémon seleccionado
        abilities = self.get_pokemon_abilities(pokemon_name)
        ability_combobox.addItems(abilities)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())