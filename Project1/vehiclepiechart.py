import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("Oregon-EV-Data.csv")

# Filter the data for electric vehicles in Oregon
oregon_ev_data = data[data["State"] == "OR"]

# Count the occurrences of each EV type
ev_type_counts = oregon_ev_data["zev_type"].value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(ev_type_counts, labels=ev_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Electric Vehicle Types in Oregon")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
