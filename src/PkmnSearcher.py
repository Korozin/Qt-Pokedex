import requests
from PyQt5 import QtWidgets, QtGui
from Classes import MainWindow, InfoPuller, ErrorWindow

class PkmnSearcher_Main(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(PkmnSearcher_Main, self).__init__()

        # Define placeholder image
        self.Placeholder_Sprite = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"

        # Set up base GUI parameters
        self.setupUi(self)
        self.Set_Functions()
        self.Change_Sprite(self.Placeholder_Sprite)

        # Initialize Error Window
        self.ErrorWindow = ErrorWindow.ErrorWindow()

    def Set_Functions(self):
        self.Search_Button.clicked.connect(self.Main)
        self.Clear_Button.clicked.connect(self.Clear_Form)

    def Change_Sprite(self, URL):
        # Load image from URL using requests module
        response = requests.get(URL)
        image = QtGui.QImage.fromData(response.content)

        # Set image to QLabel widget
        self.Sprite_Label.setPixmap(QtGui.QPixmap.fromImage(image))

    def Clear_Form(self):
        self.Input_Edit.clear()
        self.Output_Text.clear()
        self.Change_Sprite(self.Placeholder_Sprite)

    def Main(self):
        Pkmn_ID = self.Input_Edit.text()

        try:
            Pkmn_Info = InfoPuller.PokemonInfo(Pkmn_ID)
            Pkmn_Info.fetch_pokemon_data()
            Pkmn_Info.fetch_species_data()
            Pkmn_Output = Pkmn_Info.get_info()

            # Format the information as a string
            Output_String = f"ID: {Pkmn_Output['id']}\n"
            Output_String += f"NAME: {Pkmn_Output['name']}\n"
            Output_String += f"TYPE: {', '.join(Pkmn_Output['types'])}\n"
            Output_String += f"ABILITIES: {', '.join(Pkmn_Output['abilities'])}\n"
            Output_String += f"MOVES: {', '.join(Pkmn_Output['moves'])}\n"
            Output_String += f"EVOLUTION CHAIN: {' -> '.join(Pkmn_Output['evolution_chain'])}\n"
            Output_String += "STATS:\n"

            for stat, value in Pkmn_Output['stats'].items():
                Output_String += f"        {stat}: {value}\n"

            self.Change_Sprite(Pkmn_Output['sprite_url'])

            self.Output_Text.setPlainText(Output_String)
        except Exception as e:
            self.ErrorWindow.CreateWindow("Error!",
                                         f"{e}\n\n"
                                          "Invalid or empty JSON Data.\n\n"
                                          "Are you sure the Pokemon Name / ID entered was correct?",
                                         500, 200)
            self.ErrorWindow.show()


if __name__ == "__main__":
    import sys
    PkmnSearcher_App = QtWidgets.QApplication(sys.argv)
    PkmnSearcher_Var = PkmnSearcher_Main()
    PkmnSearcher_Var.show()
    sys.exit(PkmnSearcher_App.exec_())
