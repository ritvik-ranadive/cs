import folium

m = folium.Map(location=[0.0, 0.0], zoom_start=3)
folium.Rectangle(bounds=[(28.6471948, 76.9531796), (19.0821978, 72.7411)], color='#ff7800', fill=True, fill_color='#ffff00', fill_opacity=0.2).add_to(m)
m.save("map.html")
