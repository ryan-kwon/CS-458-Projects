import pandas as pd
import folium
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

# Read the electric vehicle data from the CSV file
ev_data = pd.read_csv("Oregon-EV-Data.csv")

# # Filter the data for Oregon
# oregon_ev_data = ev_data[ev_data["State"] == "OR"]

# # Group the data by make and city to count the number of EVs for each make in each city
# make_city_counts = oregon_ev_data.groupby(["Make", "City"]).size().reset_index(name="Count")

# # Initialize a map centered around Oregon
# geolocator = Nominatim(user_agent="ev_map")
# oregon_location = geolocator.geocode("Oregon")
# map_osm = folium.Map(location=[oregon_location.latitude, oregon_location.longitude], zoom_start=7)

# # Add markers for each city
# for index, row in make_city_counts.iterrows():
#     # Get latitude and longitude coordinates for the city
#     city_location = geolocator.geocode(row["City"] + ", Oregon")
#     if city_location:
#         city_lat = city_location.latitude
#         city_lon = city_location.longitude
#         # Add marker for the city with the count as the popup
#         folium.Marker([city_lat, city_lon], popup=row["City"] + " - " + row["Make"] + ": " + str(row["Count"])).add_to(map_osm)

# # Save the map as an HTML file
# map_osm.save("ev_locations_map.html")

# Filter the data for Oregon
oregon_ev_data = ev_data[ev_data["State"] == "OR"]

# Group the data by make and city to count the number of EVs for each make in each city
make_city_counts = oregon_ev_data.groupby(["Make", "City"]).size().reset_index(name="Count")

# Initialize geolocator
geolocator = Nominatim(user_agent="ev_scatterplot")

# Create a scatter plot of latitude and longitude coordinates
plt.figure(figsize=(10, 8))
for index, row in make_city_counts.iterrows():
    # Get latitude and longitude coordinates for the city
    location = geolocator.geocode(row["City"] + ", Oregon")
    if location:
        city_lat = location.latitude
        city_lon = location.longitude
        # Plot the coordinates
        plt.scatter(city_lon, city_lat, s=row["Count"], label=row["Make"] + " - " + row["City"])

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Locations of EV Makes in Oregon Cities")

# Add legend
plt.legend()

# Show plot
plt.show()