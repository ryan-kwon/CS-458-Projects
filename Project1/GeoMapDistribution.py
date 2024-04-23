# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
# from geopy.geocoders import Nominatim

# # Read the CSV file
# data = pd.read_csv("Oregon-EV-Data.csv")

# # Filter the data for electric vehicles in Oregon
# oregon_ev_data = data[data["State"] == "OR"]

# # Initialize geocoder
# geolocator = Nominatim(user_agent="my_geocoder")

# # Geocode city and county to obtain latitude and longitude
# oregon_ev_data["Latitude"] = oregon_ev_data["City"].apply(lambda x: geolocator.geocode(x + ", Oregon").latitude)
# oregon_ev_data["Longitude"] = oregon_ev_data["City"].apply(lambda x: geolocator.geocode(x + ", Oregon").longitude)

# # Create a Basemap centered around Oregon
# plt.figure(figsize=(10, 10))
# m = Basemap(projection='merc', llcrnrlat=41, urcrnrlat=47, llcrnrlon=-125, urcrnrlon=-116, resolution='l')

# # Draw coastlines, states, and countries
# m.drawcoastlines()
# m.drawstates()
# m.drawcountries()

# # Plot EV registration locations
# x, y = m(oregon_ev_data["Longitude"].values, oregon_ev_data["Latitude"].values)
# m.scatter(x, y, color='red', s=10, alpha=0.5)

# # Add title and show the map
# plt.title("Electric Vehicle Distribution in Oregon")
# plt.show()


import pandas as pd
import folium
from geopy.geocoders import Nominatim

# Read the CSV file
data = pd.read_csv("Oregon-EV-Data.csv")

# Filter the data for electric vehicles in Oregon
oregon_ev_data = data[data["State"] == "OR"]

# Initialize the geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Create a map centered around Oregon
oregon_map = folium.Map(location=[44.0, -120.5], zoom_start=7)

# Add markers for each EV registration location
for index, row in oregon_ev_data.iterrows():
    location = geolocator.geocode(f"{row['City']}, {row['County']}, Oregon")
    if location:
        popup_text = f"{row['Make']} {row['Model']}\n{row['County']}, {row['City']}"
        folium.Marker([location.latitude, location.longitude], popup=popup_text).add_to(oregon_map)

# Save the map to an HTML file
oregon_map.save("electric_vehicle_distribution_map.html")
