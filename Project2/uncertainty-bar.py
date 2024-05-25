import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
data_file = "Electric_Vehicle_Population_Data.csv"
df = pd.read_csv(data_file)

# Calculate the average electric range and uncertainty for each car model
model_groups = df.groupby('Model')['Electric Range']

# Compute average and standard deviation
average_ranges = model_groups.mean()
uncertainties = model_groups.std()

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Bar graph with error bars
bars = ax.bar(average_ranges.index, average_ranges, yerr=uncertainties, capsize=5, color='skyblue', alpha=0.7, edgecolor='blue')

# Labels and title
ax.set_xlabel('Car Model')
ax.set_ylabel('Average Electric Range')
ax.set_title('Average Electric Range by Car Model with Uncertainty')

# Set ticks and tick labels
ax.set_xticks(range(len(average_ranges)))
ax.set_xticklabels(average_ranges.index, rotation=90)

# Show the plot
plt.tight_layout()
plt.show()
