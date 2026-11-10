import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataframe (replace with your actual data)
data = {
    'Year': [2017, 2017, 2017, 2017, 2018, 2018],
    'Month': ['August', 'September', 'October', 'November', 'January', 'February'],
    'Region': ['Bering', 'Bering', 'Bering', 'Bering', 'Bering', 'Bering'],
    'IceVolume': [None, 197.59, 3223.15, 8009.8, 125492.36, 149650.33]
}

df = pd.DataFrame(data)

# Filter only Bering Region
bering_df = df[df['Region'] == 'Bering']

# Convert month names to numbers for ordering
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
bering_df['MonthNum'] = bering_df['Month'].apply(lambda x: month_order.index(x) + 1)

# Pivot for heatmap
pivot = bering_df.pivot(index='MonthNum', columns='Year', values='IceVolume')

# Plot
plt.figure(figsize=(8, 6))
sns.heatmap(pivot, cmap="Blues", annot=True, fmt=".0f", cbar_kws={'label': 'Ice Volume'})
plt.title("Bering Strait Sea Ice Volume (Vertical Profile by Month)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.yticks(ticks=range(1,13), labels=month_order, rotation=0)
plt.tight_layout()
plt.show()

