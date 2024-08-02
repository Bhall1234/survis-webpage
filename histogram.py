import matplotlib.pyplot as plt
import numpy as np

# Data: years and their frequencies
years = [1956, 2008, 2015, 1991, 2007, 2006, 2012, 2006, 2015, 1999, 2014, 2009, 2023, 2021, 2019, 2023, 2019, 2022, 2024, 2024, 2020, 2022]

# Range of years to include (from 1956 to 2024)
all_years = np.arange(1956, 2025)

# Count occurrences of each year within the full range
year_counts = {year: 0 for year in all_years}
for year in years:
    year_counts[year] += 1

# Extract counts and sort by year
sorted_years = sorted(year_counts.keys())
sorted_counts = [year_counts[year] for year in sorted_years]

# Split data into two parts: one for 1956 and another for 1991 onwards
years_1956 = [1956]
counts_1956 = [year_counts[1956]]

years_1991_onwards = sorted_years[sorted_years.index(1991):]
counts_1991_onwards = sorted_counts[sorted_years.index(1991):]

# Use a colormap for better visual appeal
cmap = plt.get_cmap('tab20')
bar_colors_1956 = [cmap(0)]
bar_colors_1991_onwards = [cmap(i % cmap.N) for i in range(len(years_1991_onwards))]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(14, 8), gridspec_kw={'width_ratios': [1, 4]})

# Plot the histogram for 1956
bar_width = 0.8  # Set a consistent bar width
ax1.bar(years_1956, counts_1956, color=bar_colors_1956, edgecolor='black', width=bar_width)
ax1.set_xlim(1955, 1957)
ax1.set_xticks([1956])
ax1.set_xticklabels(['1956'], rotation=45, ha='right')

# Plot the histogram for 1991 onwards
bars = ax2.bar(years_1991_onwards, counts_1991_onwards, color=bar_colors_1991_onwards, edgecolor='black', width=bar_width)
ax2.set_xlim(1990, 2025)
ax2.set_xticks(years_1991_onwards)
ax2.set_xticklabels(years_1991_onwards, rotation=45, ha='right')

# Add titles and labels
fig.suptitle('Distribution of Published Papers by Year')
ax1.set_ylabel('Number of Papers Published')
ax2.set_xlabel('Publication Year')

# Set y-axis to display integer values only
ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Add grid lines
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')

# Add a break in the x-axis
d = .015  # how big to make the diagonal lines in axes coordinates
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((1-d, 1+d), (-d, +d), **kwargs)
ax1.plot((1-d, 1+d), (1-d, 1+d), **kwargs)

kwargs.update(transform=ax2.transAxes)
ax2.plot((-d, +d), (-d, +d), **kwargs)
ax2.plot((-d, +d), (1-d, 1+d), **kwargs)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to make room for titles
plt.subplots_adjust(wspace=0.05)  # Reduce space between subplots

# Save the plot as an image file
plt.savefig('papers_distribution.png', dpi=300)

# Show the plot
plt.show()
