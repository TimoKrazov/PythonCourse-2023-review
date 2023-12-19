import sqlite3

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
