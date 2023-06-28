# Build a dataframe that includes average
# sales by platform, by region.

# Business Problem #1
# Which Publisher has the highest global
# sales

import pandas as pd
import matplotlib.pyplot as plt


file_name = 'vgsales.csv'


def business_problem(_topic):
    raw_df = pd.read_csv(file_name)
    publisher_df = raw_df.groupby([_topic])[['Global_Sales', 'JP_Sales']].sum().reset_index()
    publisher_df = publisher_df.sort_values('Global_Sales', ascending=False)
    return publisher_df

year_analysis = business_problem('Year')
platform_analysis = business_problem('Platform')


year_analysis = year_analysis.sort_values(['Year'])
fig, ax = plt.subplots()
ax.plot(year_analysis['Year'].values, year_analysis['Global_Sales'].values)  # Create a figure containing a single axes.
plt.show()
plt.savefig('videogame.png')