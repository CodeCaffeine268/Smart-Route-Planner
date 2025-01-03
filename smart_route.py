from geopy.distance import geodesic
import folium
from folium.plugins import MarkerCluster

# Sample coordinates list (latitude, longitude)
coordinates = [
    (12.9716, 77.5946),  # Bangalore
    (13.0827, 80.2707),  # Chennai
    (19.0760, 72.8777),  # Mumbai
    # Add more coordinates as needed
]

# Vehicle speeds in km/h
vehicle_speeds = {
    'car': 60,  # Car speed in km/h
    'bike': 40  # Bike speed in km/h
}

# Function to check if the coordinates are valid (latitude in [-90, 90] and longitude in [-180, 180])
def is_valid_coordinate(lat, lon):
    return -90 <= lat <= 90 and -180 <= lon <= 180

# Function to calculate travel time
def calculate_travel_time(distance_in_km, vehicle_type):
    speed = vehicle_speeds.get(vehicle_type, 60)  # Default to car speed
    time_in_hours = distance_in_km / speed
    return time_in_hours

# Ask the user for the vehicle type
vehicle_type = input("Enter vehicle type (car/bike): ").strip().lower()
if vehicle_type not in vehicle_speeds:
    print(f"Invalid vehicle type: {vehicle_type}. Defaulting to 'car'.")
    vehicle_type = 'car'

# Initialize total distance and travel time to 0
total_distance = 0
total_time = 0

# Create a map centered on the first coordinate
route_map = folium.Map(location=coordinates[0], zoom_start=6)
marker_cluster = MarkerCluster().add_to(route_map)

# Loop through the coordinates and calculate the distance and travel time between each pair
for i in range(len(coordinates) - 1):
    lat1, lon1 = coordinates[i]
    lat2, lon2 = coordinates[i + 1]

    # Print the coordinates for debugging
    print(f"Checking coordinates: {coordinates[i]} and {coordinates[i + 1]}")

    # Check if both coordinates are valid
    if not is_valid_coordinate(lat1, lon1) or not is_valid_coordinate(lat2, lon2):
        print(f"Invalid coordinates: {coordinates[i]} or {coordinates[i + 1]}")
    else:
        # Calculate the distance between the valid coordinates
        distance = geodesic(coordinates[i], coordinates[i + 1]).meters
        distance_in_km = distance / 1000  # Convert to kilometers
        travel_time = calculate_travel_time(distance_in_km, vehicle_type)

        print(f"Distance between {coordinates[i]} and {coordinates[i + 1]}: {distance:.2f} meters")
        print(f"Estimated travel time: {travel_time:.2f} hours")

        # Add distance and time to total
        total_distance += distance
        total_time += travel_time

        # Add markers to the map
        folium.Marker(location=[lat1, lon1], popup=f"Point {i+1}").add_to(marker_cluster)
        folium.Marker(location=[lat2, lon2], popup=f"Point {i+2}").add_to(marker_cluster)

# Add a line connecting the route on the map
folium.PolyLine(locations=coordinates, color="blue", weight=2.5, opacity=1).add_to(route_map)

# Print the total distance and travel time
print(f"Total distance: {total_distance:.2f} meters")
print(f"Total estimated travel time: {total_time:.2f} hours")

# Save the map as an HTML file
route_map.save("route_map.html")
print("Route map saved as 'route_map.html'. Open it in your browser to view.")
