import folium
m = folium.Map(location=[35.6895, 139.6917], zoom_start=5)

places = [
        {"name": "東京タワー", "lat": 35.6586, "lon": 139.7454, "comment": "夜景が綺麗"},
        {"name": "大阪城", "lat": 34.6873, "lon": 135.5259, "comment": "夜景が綺麗"},
        {"name": "清水寺", "lat": 34.9949, "lon": 135.7850, "comment": "夜景が綺麗"},
]

for spot in places:
    folium.Marker(
        location=[spot['lat'], spot['lon']],
        popup=f"{spot['name']}<br>{spot['comment']}",
        tooltip=spot['name'],
        icon = folium.Icon(color='blue', icon ='info-sign')
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

