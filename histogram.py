import matplotlib.pyplot as plt
import numpy as np

# Data: years and their frequencies
years = [2023, 2022, 2023, 2023, 2022, 2024, 2021, 2023, 2018, 2024]

# Range of years to include (from 2018 to 2024)
all_years = np.arange(2018, 2025)

# Count occurrences of each year within the full range
year_counts = {year: 0 for year in all_years}
for year in years:
    year_counts[year] += 1

# Extract counts and sort by year
sorted_years = sorted(year_counts.keys())
sorted_counts = [year_counts[year] for year in sorted_years]

# Define colors for each year
colors = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'brown', 'pink', 'grey', 'lime']
year_colors = {year: colors[i % len(colors)] for i, year in enumerate(sorted_years)}

# Create color list for each bar
bar_colors = [year_colors[year] for year in sorted_years]

# Plot the histogram
bars = plt.bar(sorted_years, sorted_counts, color=bar_colors, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Papers by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')

# Show the plot
plt.xticks(sorted_years)
plt.show()
