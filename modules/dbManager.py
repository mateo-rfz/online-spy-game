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
        return "randomWordForTest"







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

