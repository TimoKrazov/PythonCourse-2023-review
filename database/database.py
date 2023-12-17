import sqlite3

def add_stats(cur, names, line, popular, wins, bans, kdas, pentakills):
    cur.execute('''INSERT INTO league_of_legends(person, line, popularity_percent, winrate_percent, banrate_percent, kda, pentas_match)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',(names, line, popular, wins, bans, kdas, pentakills))
#Создание БД
def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS league_of_legends')

    cur.execute('''CREATE TABLE league_of_legends (
            id INTEGER PRIMARY KEY,
            person VARCHAR(255),
            line VARCHAR(255),
            popularity_percent INTEGER,
            winrate_percent INTEGER,
            banrate_percent INTEGER,
            kda VARCHAR,
            pentas_match INTEGER
        )
    ''')
    conn.commit()

with sqlite3.connect('./base/example.db') as conn:
    cur = conn.cursor()
    create_table(cur, conn)
