#!/usr/bin/env python
from game.game import Game
import sqlite3

#database
conn = sqlite3.connect("database/rounds.db")
cursor = conn.cursor()

# Check if the table already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rounds'")
table_exists = cursor.fetchone()


rows = cursor.fetchall()

while True:
    choice = input("pick an option: 1. Play the game, 2. See previous results, 3. QUIT: ")
    try:
        choice = int(choice)
    except:
        print("Please choose a number")

    if choice in range(0,4):
        if choice == 1:
            if __name__ == '__main__':
                game = Game()
                game.play()
        if choice == 2:
            for row in rows:
                print(row)

        else:
            break
    else:
        print("please choose an option")