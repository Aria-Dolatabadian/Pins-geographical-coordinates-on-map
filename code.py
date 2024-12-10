import folium
import pandas as pd

# Read the CSV file containing geographical coordinates
csv_file = 'locations.csv'  # Replace with your actual file path
data = pd.read_csv(csv_file)

# Define the center of the map (centered roughly based on the locations in Manitoba, Canada)
latitude = 53.46
longitude = -97.97

# Create a folium map centered at the selected location
mymap = folium.Map(location=[latitude, longitude], zoom_start=5)

# Define a list of colours for the pins
colors = [
    "red", "blue", "green", "purple", "orange",
    "darkred", "lightblue", "lightgreen", "pink", "cadetblue"
]

# Add a marker for each location from the CSV file with a different colour
for index, row in data.iterrows():
    color = colors[index % len(colors)]  # Cycle through the colours list
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['locations']}: Lat {row['latitude']}, Lon {row['longitude']}",
        icon=folium.Icon(color=color)
    ).add_to(mymap)

# Add a legend to the map
legend_html = """
<div style="
    position: fixed;
    bottom: 50px; left: 50px; width: 250px; height: auto;
    z-index:9999; font-size:14px;
    background-color:white; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
">
<b>Legend</b><br>
"""
for index, row in data.iterrows():
    color = colors[index % len(colors)]
    legend_html += f"<i style='background:{color};width:10px;height:10px;border-radius:50%;display:inline-block;'></i> {row['locations']}<br>"
legend_html += "</div>"

mymap.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
mymap.save('map_with_coloured_pins_and_legend.html')

print("Map with coloured pins and legend has been saved as 'map_with_coloured_pins_and_legend.html'.")
