import sqlite3

conn = sqlite3.connect('database/rounds.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rounds'")
table_exists = cursor.fetchone()

if not table_exists:
    cursor.execute("""CREATE TABLE rounds(
                      total_rounds INTEGER,
                      player_wins INTEGER,
                      computer_wins INTEGER)""")

conn.commit()
conn.close()
