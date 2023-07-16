# Qt-Pokedex

Qt-Pokedex is a simple Python GUI application that allows users to search for information about any Pokemon by entering its name or ID. The application uses the PokeAPI to retrieve data about the Pokemon and displays it in a user-friendly format.

## Installation

-    Clone the repository or download the latest release.
-    Run the application by executing the PkmnSearcher.py file (or EXE if one is availiable).

## Usage

-    Enter the name or ID of the Pokemon you want to search for in the input field.
-    Click the "🔍" button to retrieve information about the Pokemon.
-    The application will display the Pokemon's ID, name, type(s), abilities, moves, evolution chain, stats, and sprite image.

## Development

The application is divided into two main parts: the frontend and the backend.

The frontend is implemented using PyQt5, a Python framework for creating desktop applications. The MainWindow.py file contains the GUI schematic whcih is imported by the PkmnSearcher file..

The backend is implemented in Python and uses the requests library to make HTTP requests to the PokeAPI. The PokemonInfo class retrieves information about the Pokemon and formats it as a dictionary.

## Credits

-    [PokeAPI ↗](https://pokeapi.co/) for providing the Pokemon data used in the application.
-    [PyQt5 ↗](https://pypi.org/project/PyQt5/) for the Python bindings for the Qt framework used in the GUI.
-    [requests ↗](https://pypi.org/project/requests/) for the HTTP request library used to retrieve data from the PokeAPI.
