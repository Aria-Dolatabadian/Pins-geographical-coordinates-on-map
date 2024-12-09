import folium
import pandas as pd

# Read the CSV file containing geographical coordinates
# Ensure your CSV has 'latitude' and 'longitude' columns
csv_file = 'locations.csv'  # Replace with your actual file path
data = pd.read_csv(csv_file)

# Example of CSV format:
# latitude,longitude
# 51.5074,-0.1278
# 48.8566,2.3522
# ...

# Define the center of the map (you can change it to the center of your selected country)
# Example: London, UK
latitude = 53.46
longitude = -97.97

# Create a folium map centered at the selected location
mymap = folium.Map(location=[latitude, longitude], zoom_start=5)

# Add a marker for each location from the CSV file
for index, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Lat: {row['latitude']}, Lon: {row['longitude']}"
    ).add_to(mymap)

# Save the map to an HTML file (you can view this in a browser)
mymap.save('map_with_markers.html')

# If you're using Jupyter, you can also display the map inline
# mymap
