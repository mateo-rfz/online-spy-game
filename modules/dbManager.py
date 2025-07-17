import string
import sqlite3
import random
import json
from datetime import datetime

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("games.db")
        self.__createTable()






    def __randomWord(self):
        words = [
    "Bank", "School", "Airport", "Hospital", "Beach", "Restaurant", "Circus", "Train", "Operating Room",
    "Bus", "Prison", "Library", "Museum", "Sauna", "Gym", "Cafe", "Park", "Hotel", "Zoo",
    "Shop", "Cinema", "Theater", "Ship", "Spaceship", "Military Base", "Camp", "Cave", "House",
    "Garage", "University", "Laboratory", "Office", "Church", "Mosque", "Mountain", "Desert", "River",
    "Aquarium", "Bedroom", "Kitchen", "Factory", "Bridge", "Football Field", "Basketball Court",
    "Playground", "Supermarket", "Gas Station", "Fire Station", "Police Station", "Subway Station", "Train Station",
    "Elevator", "Tent", "Balcony", "Storage", "Well", "Battlefield", "Bunker", "Server Room", "Meeting Room",
    "Cemetery", "Cottage", "Wedding Hall", "Conference Room", "Runway", "Inside a Car", "Boat", "Freezer",
    "Greenhouse", "Clubhouse", "Forest Camp", "Oil Tanker", "Wood Workshop", "Painting Studio", "Carpentry", "Tailor Shop", "Backyard",
    "Music Room", "Swimming Pool", "Fitness Center", "Bakery", "Pastry Shop", "Bookstore", "Pharmacy",
    "Farm", "Flower Shop", "Bazaar", "Teahouse", "Law Office", "Notary Office", "Repair Shop", "Exhibition",
    "Studio", "Classroom", "Rooftop", "Clothing Store", "Car Wash", "Blacksmith", "Vegetable Market",
    "Post Office", "Insurance Office", "Telecom Center", "Shopping Mall", "Traditional Market", "TV Antenna", "Beauty Salon",
    "Barber Shop", "Arcade", "Secret Room", "Basement", "Abandoned Church", "Ice Cave", "Mountain Peak", "Nomad Tent",
    "Town Square", "Welding Workshop", "Space Station", "Bird Nest", "Slide Park", "Abandoned Island", "Port", "Fish Market",
    "Radio Station", "Hunting Cabin", "Military Camp", "Minefield", "Detective Office", "Inside a Suitcase", "Creepy Circus", "Metro Tunnel",
    "Morgue", "Fitting Room", "Toy Store", "Game Arcade", "Dark Cave", "Changing Room", "Bookshelf", "Under the Bridge", "Control Room", "Weather Station",
    "Airplane Cabin", "Departure Hall", "Meat Freezer", "Ammo Storage", "Haunted House", "Opera Hall", "Waiting Room",
    "Board Game Cafe", "Chemistry Lab", "Language Class", "Dorm Room", "Laundry Room", "Backyard Garden", "Barracks",
    "Taxi Station", "Backstage", "Security Room", "Pantry", "Workshop", "Attic", "Oil Well",
    "Emergency Stairs", "Reading Room", "Wooden House", "Tool Shop", "Art Gallery", "Rug Shop",
    "Auditorium", "Office Kitchen", "Film Archive", "Manager's Office", "Supervisor Room", "Book Storage", "Film Archive",
    "Solitary Cell", "School Hallway", "Fire Truck Ladder", "Biology Lab", "Locker Room", "Underground Shelter",
    "Animal Cage", "Late-Night Study Room", "Cow Farm", "Water Well", "Dissection Room", "Grass Field", "Bowling Alley",
    "Skating Rink", "Inside a Train", "Inside a Bus", "Driver's Cabin", "Porch", "Coast Guard Station",
    "Control Tower", "Power Station", "Telecom Tower", "Slide Hall", "Motorcycle Garage", "ER Station",
    "Billiard Hall", "Grandma’s House", "Down the Well", "Fencing Hall", "Baseball Field", "Mountain Cabin"
]

        random.shuffle(words)
        return random.choice(words)





    def __randomGameIdCreator(self, length=6):
        chars = string.ascii_letters + string.digits
        while True:
            gameId = ''.join(random.choices(chars, k=length))
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM games WHERE gameId=?", (gameId,))
            if not cursor.fetchone():
                return gameId







    def __createTable(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    gameId TEXT,
                    playerNumbers INTEGER,
                    spyNumbers INTEGER,
                    work TEXT,
                    startTime TEXT,
                    startDate TEXT,
                    rolesLeft TEXT
                )
            """)
            self.conn.commit()
            return True
        except Exception as e:
            return False







    def addGame(self, playerNumbers: int, spyNumbers: int) -> str | bool:
        try:
            cursor = self.conn.cursor()
            gameId = self.__randomGameIdCreator()
            word = self.__randomWord()

            roles = ["SPY"] * spyNumbers + [word] * playerNumbers
            random.shuffle(roles)
            roles_json = json.dumps(roles)

            now = datetime.now()
            startTime = now.strftime("%H:%M:%S")
            startDate = now.strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO games (gameId, playerNumbers, spyNumbers, work, startTime, startDate, rolesLeft)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (gameId, playerNumbers, spyNumbers, word, startTime, startDate, roles_json))

            self.conn.commit()
            return gameId
        except Exception as e:
            return e
            return False









    def getAct(self, gameId: str) -> str | bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT rolesLeft FROM games WHERE gameId=?", (gameId,))
            row = cursor.fetchone()

            if not row:
                return False

            roles = json.loads(row[0])
            if not roles:
                return "NO ROLES LEFT"

            act = roles.pop()
            new_roles_json = json.dumps(roles)

            cursor.execute("UPDATE games SET rolesLeft=? WHERE gameId=?", (new_roles_json, gameId))
            self.conn.commit()
            return act
        except Exception as e:
            return False

