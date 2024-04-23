import pandas as pd
import matplotlib.pyplot as plt

# Read the electric vehicle data from the Excel file
ev_data = pd.read_csv("Oregon-EV-Data.csv")

# Read the CSV file containing population density data for each county
population_data = pd.read_csv("CensusTracts_6150646886027549075.csv")

# Extract relevant columns (county name and population) from population data
population_density_data = population_data[["COUNTY", "POP20"]]

# Rename columns for consistency
population_density_data = population_density_data.rename(columns={"COUNTY": "County", "POP20": "Population"})

# Group electric vehicle data by county and count the number of registrations in each county
ev_count_per_county = ev_data.groupby("County").size().reset_index(name="Electric Vehicle Registrations")

# Merge electric vehicle count data with population density data based on county name
merged_data = pd.merge(ev_count_per_county, population_density_data, on="County")

# Plot scatter plot of electric vehicle registrations vs. population density
plt.figure(figsize=(10, 6))
plt.scatter(merged_data["Population"], merged_data["Electric Vehicle Registrations"])
plt.title("Electric Vehicle Registrations vs. Population Density in Oregon Counties")
plt.xlabel("Population Density (2020)")
plt.ylabel("Electric Vehicle Registrations")
plt.grid(True)
plt.show()