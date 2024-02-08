from PySide6 import QtCore, QtGui, QtWidgets

class PokemonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.setObjectName("pokemon_widget")

        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.info_layout = QtWidgets.QVBoxLayout()
        self.info_layout.setObjectName("info_layout")

        self.img_widget = QtWidgets.QWidget(parent=self)
        self.img_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.img_widget.setObjectName("img_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.img_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img_pokemon = QtWidgets.QGraphicsView(parent=self.img_widget)
        self.img_pokemon.setObjectName("img_pokemon")
        self.verticalLayout_4.addWidget(self.img_pokemon)
        self.info_layout.addWidget(self.img_widget)

        self.name_widget = QtWidgets.QWidget(parent=self)
        self.name_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.name_widget.setObjectName("name_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.name_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name_pokemon = QtWidgets.QComboBox(parent=self.name_widget)
        self.name_pokemon.setObjectName("name_pokemon")
        self.verticalLayout_3.addWidget(self.name_pokemon)
        self.info_layout.addWidget(self.name_widget)

        self.level_type_widget = QtWidgets.QWidget(parent=self)
        self.level_type_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.level_type_widget.setObjectName("level_type_widget")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.level_type_widget)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.level_widget = QtWidgets.QVBoxLayout()
        self.level_widget.setObjectName("level_widget")
        self.level = QtWidgets.QLabel(parent=self.level_type_widget)
        self.level.setObjectName("level")
        self.level_widget.addWidget(self.level)
        self.set_level = QtWidgets.QLabel(parent=self.level_type_widget)
        self.set_level.setText("")
        self.set_level.setObjectName("set_level")
        self.level_widget.addWidget(self.set_level)
        self.horizontalLayout_27.addLayout(self.level_widget)
        self.type_widget = QtWidgets.QVBoxLayout()
        self.type_widget.setObjectName("type_widget")
        self.type = QtWidgets.QLabel(parent=self.level_type_widget)
        self.type.setObjectName("type")
        self.type_widget.addWidget(self.type)
        self.set_type = QtWidgets.QLabel(parent=self.level_type_widget)
        self.set_type.setText("")
        self.set_type.setObjectName("set_type")
        self.type_widget.addWidget(self.set_type)
        self.horizontalLayout_27.addLayout(self.type_widget)
        self.info_layout.addWidget(self.level_type_widget)

        self.ability_widget = QtWidgets.QWidget(parent=self)
        self.ability_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.ability_widget.setObjectName("ability_widget")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.ability_widget)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.ability = QtWidgets.QLabel(parent=self.ability_widget)
        self.ability.setObjectName("ability")
        self.verticalLayout_65.addWidget(self.ability)
        self.ability_comboBox = QtWidgets.QComboBox(parent=self.ability_widget)
        self.ability_comboBox.setObjectName("ability_comboBox")
        self.verticalLayout_65.addWidget(self.ability_comboBox)
        self.info_layout.addWidget(self.ability_widget)

        self.stats_widget = QtWidgets.QWidget(parent=self)
        self.stats_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.stats_widget.setObjectName("stats_widget")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.stats_widget)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.health = QtWidgets.QLabel(parent=self.stats_widget)
        self.health.setObjectName("health")
        self.verticalLayout_66.addWidget(self.health)
        self.atack = QtWidgets.QLabel(parent=self.stats_widget)
        self.atack.setObjectName("atack")
        self.verticalLayout_66.addWidget(self.atack)
        self.defense = QtWidgets.QLabel(parent=self.stats_widget)
        self.defense.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.defense.setObjectName("defense")
        self.verticalLayout_66.addWidget(self.defense)
        self.move_speed = QtWidgets.QLabel(parent=self.stats_widget)
        self.move_speed.setObjectName("move_speed")
        self.verticalLayout_66.addWidget(self.move_speed)
        self.info_layout.addWidget(self.stats_widget)

        self.move_widget = QtWidgets.QWidget(parent=self)
        self.move_widget.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.move_widget.setObjectName("move_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.move_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.move_1 = QtWidgets.QComboBox(parent=self.move_widget)
        self.move_1.setObjectName("move_1")
        self.verticalLayout_2.addWidget(self.move_1)
        self.move_2 = QtWidgets.QComboBox(parent=self.move_widget)
        self.move_2.setObjectName("move_2")
        self.verticalLayout_2.addWidget(self.move_2)
        self.move_3 = QtWidgets.QComboBox(parent=self.move_widget)
        self.move_3.setObjectName("move_3")
        self.verticalLayout_2.addWidget(self.move_3)
        self.move_4 = QtWidgets.QComboBox(parent=self.move_widget)
        self.move_4.setObjectName("move_4")
        self.verticalLayout_2.addWidget(self.move_4)
        self.info_layout.addWidget(self.move_widget)

        self.verticalLayout_60.addLayout(self.info_layout)


class TeamInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.setObjectName("team_widget")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.back_lobby = QtWidgets.QPushButton(parent=self)
        self.back_lobby.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.back_lobby.setObjectName("back_lobby")
        self.verticalLayout_5.addWidget(self.back_lobby)

        self.team_info_widget = QtWidgets.QWidget(parent=self)
        self.team_info_widget.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.team_info_widget.setObjectName("team_info_widget")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.team_info_widget)
        self.verticalLayout_36.setObjectName("verticalLayout_36")

        self.team_edit = QtWidgets.QLineEdit(parent=self.team_info_widget)
        self.team_edit.setObjectName("team_edit")
        self.verticalLayout_36.addWidget(self.team_edit)

        self.change_team = QtWidgets.QPushButton(parent=self.team_info_widget)
        self.change_team.setObjectName("change_team")
        self.verticalLayout_36.addWidget(self.change_team)

        self.img_first_pokemon = QtWidgets.QGraphicsView(parent=self.team_info_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_first_pokemon.sizePolicy().hasHeightForWidth())
        self.img_first_pokemon.setSizePolicy(sizePolicy)
        self.img_first_pokemon.setStyleSheet("")
        self.img_first_pokemon.setObjectName("img_first_pokemon")
        self.verticalLayout_36.addWidget(self.img_first_pokemon)

        self.verticalLayout_5.addWidget(self.team_info_widget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 712)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 251, 207);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create instances of the extracted widgets
        self.team_widget = TeamInfoWidget(parent=self.centralwidget)
        self.team_widget2 = TeamInfoWidget(parent=self.centralwidget)
        self.pokemon_widget = PokemonWidget(parent=self.centralwidget)
        self.pokemon_widget2 = PokemonWidget(parent=self.centralwidget)

        # Rest of the code for layout setup goes here

        self.horizontalLayout.addWidget(self.team_widget)
        self.horizontalLayout.addWidget(self.team_widget2)

        self.horizontalLayout.addWidget(self.pokemon_widget)
        self.horizontalLayout.addWidget(self.pokemon_widget2)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.team_widget.back_lobby.setText(_translate("MainWindow", "Back to Lobby"))
        self.team_widget.team_edit.setText(_translate("MainWindow", "Equipo 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())