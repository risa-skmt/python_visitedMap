from flask import Flask, request, redirect, render_template
import sqlite3
import json
from dotenv import load_dotenv
import os 
load_dotenv()


app = Flask(__name__)
DB = 'visitedPlaces.db'


# 初めのDB作成
def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS places(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        visited_date TEXT,
        address TEXT,
        lat REAL,
        lon REAL
    )
    ''')
    conn.commit()
    conn.close()

# アプリ起動時にDB初期化
init_db()

# フォームに入力されたスポットをDBへ登録
@app.route('/add_place', methods=['POST'])
def add_place():
    name = request.form.get('name')
    visited_date = request.form.get('visited_date')
    address = request.form.get('address')
    lat = request.form.get('lat')
    lon = request.form.get('lon')

    # dbに保存
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('INSERT INTO places (name, address, lat,lon, visited_date) VALUES (?,?,?,?,?)', (name, address, lat,lon, visited_date))
    conn.commit()
    conn.close()

    # 登録後トップページへ戻る
    return redirect('/')


# DBに登録済みのスポットを取得してtemplete(top.htmlにplacesで渡す)
# TOPページ表示用
@app.route('/')
def index():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('SELECT name, visited_date, address, lat, lon FROM places')
    rows = cur.fetchall()
    conn.close()

    print(rows)
    placesData = [{"name":r[0], "visited_date":r[1], "address":r[2], "lat":r[3], "lon":r[4]} for r in rows]
    places = json.dumps(placesData, ensure_ascii=False)

    return render_template('top.html', api_key=api_key , places= places)
   

if __name__ == "__main__":
    app.run(debug=True)