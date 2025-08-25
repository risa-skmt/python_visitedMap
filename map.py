import folium
import sqlite3


#DB初期化
conn = sqlite3.connect('visitedPlaces.db') 
cur = conn.cursor()

# テーブルを作成
cur.execute('''
CREATE TABLE IF NOT EXISTS visitedPlaces(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    lat REAL,
    lon REAL,
    country TEXT,
    prefecture TEXT,
    comment TEXT,
    visited_date TEXT
)
''')

# 初回のみサンプルデータを追加
sample_places = [
    ("東京タワー", 35.6586, 139.7454, "日本", "東京都", "夜景が綺麗", "2024-05-03"),
    ("大阪城", 34.6873, 135.5259, "日本", "大阪府", "歴史を感じた", "2023-11-12"),
    ("清水寺", 34.9949, 135.7850, "日本", "京都府", "紅葉が最高", "2022-10-25"),
    ("小樽運河", 43.199446, 141.001838, "日本", "北海道", "綺麗だった", "2022-10-25")
]

cur.executemany('INSERT INTO visitedPlaces (name, lat, lon, country, prefecture, comment, visited_date) VALUES (?,?,?,?,?,?,?)', sample_places)

# commitした時点でDBファイルが更新される
conn.commit()

# DBからデータを取得する
cur.execute('SELECT name, lat, lon, comment, visited_date FROM visitedPlaces')
rows = cur.fetchall()

conn.close()


# 東京周辺を中心に地図表示
m = folium.Map(location=[35.6895, 139.6917], zoom_start=5)




for spot in rows:
   name, lat, lon, comment, visited_date = spot
   popup_text = f'{name}<br>{comment}<br>訪問日：{visited_date}'
   folium.Marker(
    location =[lat, lon],
    popup = popup_text,
    tooltip = name,
    icon = folium.Icon(color='blue', icon='info-sign')
   ).add_to(m)

m.save('map.html')


# import leafmap
# import ipywidgets as widgets

# m = leafmap.Map(center=[35.6895, 139.6917], zoom=10)
# m.add_basemap(style='OpenStreetMap')

# popup = widgets.Label(value="東京駅")

# m.add_marker(
#     location=[35.6895, 139.6917],
#     popup=popup,
#     radius=20,
#     color="red",
#     fill_color="orange"
# )

# # 地図をHTMLとして保存
# m.to_html("tokyo_map.html")

