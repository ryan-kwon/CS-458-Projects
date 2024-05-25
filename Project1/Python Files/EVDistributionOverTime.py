import numpy as np 
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("Oregon-EV-Data.csv")


# Filter the data for electric vehicles in Oregon
oregon_ev_data = data[data["State"] == "OR"]

# Plot the histogram for distribution of electric vehicle model years
plt.figure(figsize=(10, 6))
oregon_ev_data["model_year"].hist(bins=range(2000, 2025), color='skyblue', edgecolor='black')
plt.title("Distribution of Electric Vehicle Model Years in Oregon")
plt.xlabel("Model Year")
plt.ylabel("Frequency")
plt.xticks(range(2000, 2025), rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()