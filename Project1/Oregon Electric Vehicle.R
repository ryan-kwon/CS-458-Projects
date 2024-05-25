#https://code.visualstudio.com/docs/languages/r
# Load required libraries
library(tidyverse)
library(ggmap)  # Load ggmap package for geocoding
library(sf)     # Load sf package for spatial operations

# Register your Google Maps API key
register_google(key = "AIzaSyD9XNL3cfveoLRokhGuIiGASc-9U5QoFbI")

# Read the electric vehicle data from the CSV file
ev_data <- read.csv("Oregon-EV-Data.csv")

# Filter the data for Oregon
oregon_ev_data <- ev_data %>%
  filter(State == "OR")

# Count registrations for each make
make_counts <- oregon_ev_data %>%
  group_by(Make) %>%
  summarise(Count = n()) %>%
  ungroup()

# Calculate total registrations
total_registrations <- sum(make_counts$Count)

# Calculate the threshold for the top 90% of registrations
threshold <- quantile(make_counts$Count, probs = 0.90)

# Filter makes with registrations above the threshold
top_makes <- make_counts %>%
  filter(Count >= threshold)

# Join with original data to retain all information
oregon_ev_data <- oregon_ev_data %>%
  semi_join(top_makes, by = "Make")

# Group the data by make and city to count the number of EVs for each make in each city
make_city_counts <- oregon_ev_data %>%
  group_by(Make, City) %>%
  summarise(Count = n()) %>%
  ungroup()

# Geocode city locations
geocodes <- geocode(paste(make_city_counts$City, ", Oregon", sep = ""))

# Combine geocodes with make_city_counts dataframe
make_city_counts <- cbind(make_city_counts, geocodes)

# Read shapefile containing Oregon's borders
oregon_shapefile <- st_read("Oregon_State_Boundary.shp")

# Plot the scatter plot with Oregon's border
ggplot() +
  geom_sf(data = oregon_shapefile, fill = "transparent", color = "black") +
  geom_point(data = make_city_counts, aes(x = lon, y = lat, size = Count, color = Make)) +
  scale_size_continuous(range = c(1, 10)) +
  labs(title = "Locations of Top 90% EV Makes in Oregon Cities",
       x = "Longitude",
       y = "Latitude",
       size = "Count",
       color = "Make") +
  theme_minimal()