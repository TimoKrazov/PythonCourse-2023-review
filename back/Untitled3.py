import sqlite3
from parser import parser
from database.database import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')

def index():
    conn = sqlite3.connect('./base/example.db', check_same_thread=False)
    cur = conn.cursor()
    query = '''
        SELECT league_of_legends.person, league_of_legends.line, league_of_legends.popularity_percent, league_of_legends.winrate_percent,
        league_of_legends.banrate_percent, league_of_legends.kda, league_of_legends.pentas_match
        FROM league_of_legends
    '''
    cur.execute(query)
    data = cur.fetchall()
    conn.close()
    print(data)
    return render_template('code.html', data=data)
if __name__ == "__main__":
    parser(cur, conn)
    app.run(debug=True)