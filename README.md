# Spy Game Web Application

This project is a web-based social deduction game built using Flask and SQLite. Players can join or create games, receive random roles, and try to figure out who the spies are among them.

## Features
- **Create Game**: Allows users to create a new game by specifying the number of players and spies.
- **Join Game**: Players can join an existing game by entering the game ID.
- **Role Assignment**: Once a player joins a game, they are assigned a role randomly, either as a spy or as a civilian.
- **About**: Provides general information about the game.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>

    Install the necessary dependencies:

pip install -r requirements.txt

Run the Flask application:

    python app.py

    The web application will be available at http://0.0.0.0:5000/ (or http://localhost:5000/).

Files
app.py

The main application file for the Flask web server. It handles the routes for the game creation, joining, and role management.
modules/dbManager.py

Contains the database manager class DbManager that handles interactions with the SQLite database. It is responsible for creating tables, adding games, and retrieving roles for players.
Templates:

    home.html: The homepage of the application.

    createGame.html: The page where users can create a new game.

    gameInfo.html: Displays information about the created game.

    joinToGame.html: Allows players to join an existing game.

    releaseRole.html: Displays the role of the player after joining the game.

    about.html: Provides information about the game.

Database:

The database games.db stores information about the games, including the game ID, number of players, number of spies, the word, and the list of remaining roles.
Functionality

    Game Creation: Users can create a new game by specifying the number of players and spies. The system will automatically generate a unique game ID and shuffle the roles (players and spies). The roles are stored in the database as a JSON array.

    Join Game: Players can join an existing game by entering a valid game ID. If a player has not yet been assigned a role, they will be assigned one when they join.

    Role Assignment: When players join, they are assigned a random role (either as a spy or a civilian) based on the number of spies and players specified when the game was created.

Usage

    Create a Game: Visit /create_game, fill out the number of players and spies, and click to create a new game. You will be redirected to the game information page with a unique game ID.

    Join a Game: Visit /join_to_game, input the game ID provided by the game creator, and click to join the game. You will be redirected to your assigned role page.

    Game Page: After joining the game, you will be taken to a page that shows your role (either spy or a specific word) and can start playing.

    About Page: Visit /about for more information about the game.

License

This project is licensed under the MIT License - see the LICENSE file for details