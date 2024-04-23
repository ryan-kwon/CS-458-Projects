import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Read the electric vehicle data from the CSV file
ev_data = pd.read_csv("Oregon-EV-Data.csv")

# Filter the data to include only years from 2010 to 2024
ev_data = ev_data[(ev_data["model_year"] >= 2010) & (ev_data["model_year"] <= 2024)]

# Group the data by make to calculate the total number of registrations for each make
make_counts = ev_data["Make"].value_counts().reset_index(name="Registrations")

# Calculate the total number of registrations
total_registrations = make_counts["Registrations"].sum()

# Calculate the cumulative sum of registrations
make_counts["Cumulative Percentage"] = make_counts["Registrations"].cumsum() / total_registrations

# Find the index where the cumulative percentage exceeds 90%
top_90_index = (make_counts["Cumulative Percentage"] <= 0.9).sum()

# Get the top 90% makes
top_90_makes = make_counts.iloc[:top_90_index]["index"]

# Group the remaining 10% of makes into an "Other" category
other_registrations = make_counts.iloc[top_90_index:]
other_registrations = pd.DataFrame({"index": ["Other"], "Registrations": [other_registrations["Registrations"].sum()]})

# Concatenate top 90% makes and "Other" category
make_counts = pd.concat([make_counts.iloc[:top_90_index], other_registrations])

# Plot the treemap
fig = px.treemap(make_counts, path=['index'], values='Registrations',
                 title="Top 90% Electric Vehicle Registrations by Make in Oregon (2010-2024)",
                 labels={'index': 'Make'})
fig.show()