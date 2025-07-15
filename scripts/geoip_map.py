import geoip2.database
import folium

def generate_map(ip_counts, geo_db_path='scripts/GeoLite2-City.mmdb'):
    m = folium.Map(location=[20, 0], zoom_start=2)
    reader = geoip2.database.Reader(geo_db_path)

    for ip, count in ip_counts.items():
        try:
            response = reader.city(ip)
            lat = response.location.latitude
            lon = response.location.longitude
            folium.CircleMarker(
                location=[lat, lon],
                radius=5,
                popup=f"{ip} - {count} hits",
                color='red',
                fill=True,
                fill_opacity=0.7
            ).add_to(m)
        except:
            continue

    m.save('static/map.html')
