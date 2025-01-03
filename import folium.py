import folium

# Create a map centered at a specific location
my_map = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# Save the map to an HTML file
my_map.save("map.html")

print("Map has been created and saved as map.html")
